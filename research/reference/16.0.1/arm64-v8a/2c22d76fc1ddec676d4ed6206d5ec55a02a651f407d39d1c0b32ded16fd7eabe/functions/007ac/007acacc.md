# 007acacc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "007acacc",
  "name": "FUN_007acacc",
  "size": 1264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb9043d0a726b0f39b04bdb0ea5b81ba1a4a16110f413c1b6b726253fdc6e615",
  "source_text_sha256": "eb9043d0a726b0f39b04bdb0ea5b81ba1a4a16110f413c1b6b726253fdc6e615"
}
~~~

## 呼び出し元

- [007ac3c0](../007ac/007ac3c0.md)

## 呼び出し先

- [0045179c](../00451/0045179c.md)
- [004519d8](../00451/004519d8.md)
- [0045bdf8](../0045b/0045bdf8.md)
- [0048ce54](../0048c/0048ce54.md)
- [00597a8c](../00597/00597a8c.md)
- [00597e48](../00597/00597e48.md)
- [00748fb8](../00748/00748fb8.md)
- [00b0e934](../00b0e/00b0e934.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57fa0](../00c57/00c57fa0.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c581b0](../00c58/00c581b0.md)
- [00c581e0](../00c58/00c581e0.md)
- [00c581f0](../00c58/00c581f0.md)

## 関連文字列（未確認候補）

~~~text
"Invitefriends_message2"
~~~

## 疑似コード / UTF-8 7084 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_007acacc(long param_1)

{
  undefined *puVar1;
  long lVar2;
  undefined *puVar3;
  undefined *puVar4;
  long *plVar5;
  long lVar6;
  double dVar7;
  double dVar8;
  byte local_1b8;
  char local_1b7 [8];
  char acStack_1af [6];
  char cStack_1a9;
  char cStack_1a8;
  char acStack_1a7 [6];
  undefined1 uStack_1a1;
  byte local_1a0;
  undefined4 local_19f;
  undefined1 local_19b;
  void *local_190;
  byte local_188 [16];
  void *local_178;
  void *local_170 [9];
  ulong local_128;
  undefined8 uStack_120;
  void *local_118;
  undefined8 uStack_110;
  undefined4 local_108;
  undefined *local_100 [3];
  undefined8 uStack_e8;
  undefined4 auStack_e0 [4];
  undefined8 local_d0;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  plVar5 = (long *)_Znwm(0x28);
  plVar5[4] = 0;
  *(undefined4 *)(plVar5 + 1) = 7;
  *plVar5 = (long)&PTR_FUN_00c63ae0;
  plVar5[3] = 0;
  plVar5[2] = (long)(plVar5 + 3);
  FUN_00597e48(local_170);
  lVar6 = FUN_00597a8c(local_170);
  uStack_1a1 = 0;
  local_170[0] = (void *)CONCAT35(local_170[0]._5_3_,0x79616406);
  dVar7 = *(double *)(param_1 + 0x10) - (double)lVar6;
  local_1b8 = 0x2c;
  acStack_1af[0] = s_Invitefriends_message2_002c034e[8];
  acStack_1af[1] = s_Invitefriends_message2_002c034e[9];
  acStack_1af[2] = s_Invitefriends_message2_002c034e[10];
  acStack_1af[3] = s_Invitefriends_message2_002c034e[0xb];
  acStack_1af[4] = s_Invitefriends_message2_002c034e[0xc];
  acStack_1af[5] = s_Invitefriends_message2_002c034e[0xd];
  local_1b7[0] = s_Invitefriends_message2_002c034e[0];
  local_1b7[1] = s_Invitefriends_message2_002c034e[1];
  local_1b7[2] = s_Invitefriends_message2_002c034e[2];
  local_1b7[3] = s_Invitefriends_message2_002c034e[3];
  local_1b7[4] = s_Invitefriends_message2_002c034e[4];
  local_1b7[5] = s_Invitefriends_message2_002c034e[5];
  local_1b7[6] = s_Invitefriends_message2_002c034e[6];
  local_1b7[7] = s_Invitefriends_message2_002c034e[7];
  cStack_1a9 = (char)s_Invitefriends_message2_002c034e._14_2_;
  cStack_1a8 = SUB21(s_Invitefriends_message2_002c034e._14_2_,1);
  acStack_1a7[0] = s_Invitefriends_message2_002c034e[0x10];
  acStack_1a7[1] = s_Invitefriends_message2_002c034e[0x11];
  acStack_1a7[2] = s_Invitefriends_message2_002c034e[0x12];
  acStack_1a7[3] = s_Invitefriends_message2_002c034e[0x13];
  acStack_1a7[4] = s_Invitefriends_message2_002c034e[0x14];
  acStack_1a7[5] = s_Invitefriends_message2_002c034e[0x15];
  dVar8 = 0.0;
  if (0.0 <= dVar7) {
    dVar8 = dVar7;
  }
  FUN_0048ce54(&local_1a0,&local_1b8);
  FUN_00748fb8(local_188,&local_1a0,0,(long)(dVar8 / 86400.0));
  FUN_0045179c(plVar5,local_170,local_188);
  if ((local_188[0] & 1) != 0) {
    _ZdlPv(local_178);
  }
  if ((local_1a0 & 1) != 0) {
    _ZdlPv(local_190);
  }
  if ((local_1b8 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_1a1,CONCAT61(acStack_1a7,cStack_1a8)));
  }
  if (((ulong)local_170[0] & 1) != 0) {
    _ZdlPv(local_170[2]);
  }
  local_170[0] = (void *)CONCAT26(local_170[0]._6_2_,0x72756f6800);
  local_19f = 0x64323025;
  local_19b = 0;
  dVar8 = dVar8 - (double)((long)(dVar8 / 86400.0) * 0x15180);
  local_170[0] = (void *)CONCAT71(local_170[0]._1_7_,8);
  local_1a0 = 8;
  lVar6 = (long)(dVar8 / 3600.0);
  FUN_00748fb8(local_188,&local_1a0,0,lVar6);
  FUN_0045179c(plVar5,local_170,local_188);
  if ((local_188[0] & 1) != 0) {
    _ZdlPv(local_178);
  }
  if ((local_1a0 & 1) != 0) {
    _ZdlPv(local_190);
  }
  if (((ulong)local_170[0] & 1) != 0) {
    _ZdlPv(local_170[2]);
  }
  local_19f = 0x64323025;
  local_19b = 0;
  dVar8 = dVar8 - (double)(lVar6 * 0xe10);
  local_170[0] = (void *)CONCAT35(local_170[0]._5_3_,0x6e696d06);
  local_1a0 = 8;
  lVar6 = (long)(dVar8 / 60.0);
  FUN_00748fb8(local_188,&local_1a0,0,lVar6);
  FUN_0045179c(plVar5,local_170,local_188);
  if ((local_188[0] & 1) != 0) {
    _ZdlPv(local_178);
  }
  if ((local_1a0 & 1) != 0) {
    _ZdlPv(local_190);
  }
  if (((ulong)local_170[0] & 1) != 0) {
    _ZdlPv(local_170[2]);
  }
  local_19f = 0x64323025;
  local_19b = 0;
  local_170[0] = (void *)CONCAT35(local_170[0]._5_3_,0x63657306);
  local_1a0 = 8;
  FUN_00748fb8(local_188,&local_1a0,0,(long)(dVar8 - (double)(lVar6 * 0x3c)));
  FUN_0045179c(plVar5,local_170,local_188);
  if ((local_188[0] & 1) != 0) {
    _ZdlPv(local_178);
  }
  if ((local_1a0 & 1) != 0) {
    _ZdlPv(local_190);
  }
  if (((ulong)local_170[0] & 1) != 0) {
    _ZdlPv(local_170[2]);
  }
  puVar4 = PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
  ;
  puVar3 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
  ;
  local_d0 = 0;
  local_170[0] = *(void **)(
                           PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
                           + 8);
  puVar1 = PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
           + 0x40;
  local_100[0] = puVar1;
  *(undefined8 *)((long)local_170 + *(long *)((long)local_170[0] + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8 +
        0x10);
  lVar6 = *(long *)((long)local_170[0] + -0x18);
  _ZNSt6__ndk18ios_base4initEPv((long)local_170 + lVar6,local_170 + 1);
  local_170[0] = puVar4 + 0x18;
  *(undefined8 *)((long)&uStack_e8 + lVar6) = 0;
  *(undefined4 *)((long)auStack_e0 + lVar6) = 0xffffffff;
  local_100[0] = puVar1;
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev(local_170 + 1);
  puVar1 = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0;
  local_170[1] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0
                 + 0x10;
  uStack_120 = 0;
  local_128 = 0;
  uStack_110 = 0;
  local_118 = (void *)0x0;
  local_108 = 0x10;
  FUN_004519d8(local_170,plVar5);
  local_188[8] = 0;
  local_188[0] = 0xe;
  local_188[1] = 0x73;
  local_188[2] = 0x65;
  local_188[3] = 0x74;
  local_188[4] = 0x54;
  local_188[5] = 0x69;
  local_188[6] = 0x6d;
  local_188[7] = 0x65;
  _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
            (&local_1a0,local_170 + 1);
  FUN_00b0e934(local_188,&local_1a0,1);
  if ((local_1a0 & 1) != 0) {
    _ZdlPv(local_190);
  }
  if ((local_188[0] & 1) != 0) {
    _ZdlPv(local_178);
  }
  local_170[0] = *(void **)puVar3;
  *(undefined8 *)((long)local_170 + *(long *)((long)local_170[0] + -0x18)) =
       *(undefined8 *)(puVar3 + 0x18);
  local_170[1] = puVar1 + 0x10;
  if ((local_128 & 1) != 0) {
    _ZdlPv(local_118);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_170 + 1);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(local_170,puVar3 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(local_100);
  (**(code **)(*plVar5 + 8))(plVar5);
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
