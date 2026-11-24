# 007acacc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `007aca8c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007aca8c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0038.md#compare-e4984cbd041ede0e0a700b053d4b5adb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `007acb24`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007acb24.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0039.md#compare-1aae3fadc5bc7b11d00159be04be62d1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "eb9043d0a726b0f39b04bdb0ea5b81ba1a4a16110f413c1b6b726253fdc6e615",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007acacc",
        "007acfb7"
      ],
      [
        "007ad100",
        "007ad103"
      ]
    ],
    "bytes_sha256": "7d026229900393c819957f58faea92bca7e104896cb1ff3eab4868e015d69e5e",
    "instruction_count": 316,
    "instruction_bytes": 1264,
    "body_bytes": 1264,
    "indirect": 1,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007acacc"></a> `007acacc` | `ff 03 07 d1` | sub sp,sp,#0x1c0 | `FALL_THROUGH`
<a id="insn-007acad0"></a> `007acad0` | `e8 b3 00 fd` | str d8,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-007acad4"></a> `007acad4` | `fd 7b 17 a9` | stp x29,x30,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-007acad8"></a> `007acad8` | `fc 67 18 a9` | stp x28,x25,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-007acadc"></a> `007acadc` | `f8 5f 19 a9` | stp x24,x23,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-007acae0"></a> `007acae0` | `f6 57 1a a9` | stp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-007acae4"></a> `007acae4` | `f4 4f 1b a9` | stp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-007acae8"></a> `007acae8` | `fd c3 05 91` | add x29,sp,#0x170 | `FALL_THROUGH`
<a id="insn-007acaec"></a> `007acaec` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-007acaf0"></a> `007acaf0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007acaf4"></a> `007acaf4` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-007acaf8"></a> `007acaf8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-007acafc"></a> `007acafc` | `a8 83 1e f8` | stur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-007acb00"></a> `007acb00` | `e4 ac 12 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-007acb04"></a> `007acb04` | `e8 00 80 52` | mov w8,#0x7 | `FALL_THROUGH`
<a id="insn-007acb08"></a> `007acb08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007acb0c"></a> `007acb0c` | `1f 10 00 f9` | str xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-007acb10"></a> `007acb10` | `08 08 00 b9` | str w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-007acb14"></a> `007acb14` | `a8 25 00 f0` | adrp x8,0xc63000 | `FALL_THROUGH`
<a id="insn-007acb18"></a> `007acb18` | `08 81 2b 91` | add x8,x8,#0xae0 | `FALL_THROUGH`
<a id="insn-007acb1c"></a> `007acb1c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-007acb20"></a> `007acb20` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-007acb24"></a> `007acb24` | `1f 8d 01 f8` | str xzr,[x8, #0x18]! | `FALL_THROUGH`
<a id="insn-007acb28"></a> `007acb28` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-007acb2c"></a> `007acb2c` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007acb30"></a> `007acb30` | `c6 ac f7 97` | bl 0x00597e48 | `UNCONDITIONAL_CALL`
<a id="insn-007acb34"></a> `007acb34` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007acb38"></a> `007acb38` | `d5 ab f7 97` | bl 0x00597a8c | `UNCONDITIONAL_CALL`
<a id="insn-007acb3c"></a> `007acb3c` | `00 00 62 9e` | scvtf d0,x0 | `FALL_THROUGH`
<a id="insn-007acb40"></a> `007acb40` | `81 0a 40 fd` | ldr d1,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-007acb44"></a> `007acb44` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-007acb48"></a> `007acb48` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acb4c"></a> `007acb4c` | `88 2c 8c 52` | mov w8,#0x6164 | `FALL_THROUGH`
<a id="insn-007acb50"></a> `007acb50` | `a9 d8 ff 90` | adrp x9,0x2c0000 | `FALL_THROUGH`
<a id="insn-007acb54"></a> `007acb54` | `29 39 0d 91` | add x9,x9,#0x34e | `FALL_THROUGH`
<a id="insn-007acb58"></a> `007acb58` | `28 0f a0 72` | movk w8,#0x79, LSL #16 | `FALL_THROUGH`
<a id="insn-007acb5c"></a> `007acb5c` | `ff 7f 00 39` | strb wzr,[sp, #0x1f] | `FALL_THROUGH`
<a id="insn-007acb60"></a> `007acb60` | `e8 13 05 b8` | stur w8,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-007acb64"></a> `007acb64` | `88 05 80 52` | mov w8,#0x2c | `FALL_THROUGH`
<a id="insn-007acb68"></a> `007acb68` | `22 01 c0 3d` | ldr q2,[x9] | `FALL_THROUGH`
<a id="insn-007acb6c"></a> `007acb6c` | `20 38 60 1e` | fsub d0,d1,d0 | `FALL_THROUGH`
<a id="insn-007acb70"></a> `007acb70` | `01 e4 00 2f` | movi d1,#0x0 | `FALL_THROUGH`
<a id="insn-007acb74"></a> `007acb74` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007acb78"></a> `007acb78` | `28 e1 40 f8` | ldur x8,[x9, #0xe] | `FALL_THROUGH`
<a id="insn-007acb7c"></a> `007acb7c` | `e2 93 80 3c` | stur q2,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-007acb80"></a> `007acb80` | `e8 73 01 f8` | stur x8,[sp, #0x17] | `FALL_THROUGH`
<a id="insn-007acb84"></a> `007acb84` | `08 20 60 1e` | fcmp d0,#0.0 | `FALL_THROUGH`
<a id="insn-007acb88"></a> `007acb88` | `28 4c 60 1e` | fcsel d8,d1,d0,mi | `FALL_THROUGH`
<a id="insn-007acb8c"></a> `007acb8c` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007acb90"></a> `007acb90` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-007acb94"></a> `007acb94` | `b0 80 f3 97` | bl 0x0048ce54 | `UNCONDITIONAL_CALL`
<a id="insn-007acb98"></a> `007acb98` | `08 00 c3 d2` | mov x8,#0x180000000000 | `FALL_THROUGH`
<a id="insn-007acb9c"></a> `007acb9c` | `a8 1e e8 f2` | movk x8,#0x40f5, LSL #48 | `FALL_THROUGH`
<a id="insn-007acba0"></a> `007acba0` | `00 01 67 9e` | fmov d0,x8 | `FALL_THROUGH`
<a id="insn-007acba4"></a> `007acba4` | `00 19 60 1e` | fdiv d0,d8,d0 | `FALL_THROUGH`
<a id="insn-007acba8"></a> `007acba8` | `14 00 78 9e` | fcvtzs x20,d0 | `FALL_THROUGH`
<a id="insn-007acbac"></a> `007acbac` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-007acbb0"></a> `007acbb0` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007acbb4"></a> `007acbb4` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-007acbb8"></a> `007acbb8` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-007acbbc"></a> `007acbbc` | `ff 70 fe 97` | bl 0x00748fb8 | `UNCONDITIONAL_CALL`
<a id="insn-007acbc0"></a> `007acbc0` | `e1 43 01 91` | add x1,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007acbc4"></a> `007acbc4` | `e2 e3 00 91` | add x2,sp,#0x38 | `FALL_THROUGH`
<a id="insn-007acbc8"></a> `007acbc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007acbcc"></a> `007acbcc` | `f4 92 f2 97` | bl 0x0045179c | `UNCONDITIONAL_CALL`
<a id="insn-007acbd0"></a> `007acbd0` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-007acbd4"></a> `007acbd4` | `28 1a 00 37` | tbnz w8,#0x0,0x007acf18 | `CONDITIONAL_JUMP`
<a id="insn-007acbd8"></a> `007acbd8` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007acbdc"></a> `007acbdc` | `68 1a 00 37` | tbnz w8,#0x0,0x007acf28 | `CONDITIONAL_JUMP`
<a id="insn-007acbe0"></a> `007acbe0` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007acbe4"></a> `007acbe4` | `a8 1a 00 37` | tbnz w8,#0x0,0x007acf38 | `CONDITIONAL_JUMP`
<a id="insn-007acbe8"></a> `007acbe8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acbec"></a> `007acbec` | `68 00 00 36` | tbz w8,#0x0,0x007acbf8 | `CONDITIONAL_JUMP`
<a id="insn-007acbf0"></a> `007acbf0` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007acbf4"></a> `007acbf4` | `af ac 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acbf8"></a> `007acbf8` | `08 30 8a 52` | mov w8,#0x5180 | `FALL_THROUGH`
<a id="insn-007acbfc"></a> `007acbfc` | `09 ed 8d 52` | mov w9,#0x6f68 | `FALL_THROUGH`
<a id="insn-007acc00"></a> `007acc00` | `b6 04 86 52` | mov w22,#0x3025 | `FALL_THROUGH`
<a id="insn-007acc04"></a> `007acc04` | `28 00 a0 72` | movk w8,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-007acc08"></a> `007acc08` | `a9 4e ae 72` | movk w9,#0x7275, LSL #16 | `FALL_THROUGH`
<a id="insn-007acc0c"></a> `007acc0c` | `56 86 ac 72` | movk w22,#0x6432, LSL #16 | `FALL_THROUGH`
<a id="insn-007acc10"></a> `007acc10` | `88 7e 08 9b` | mul x8,x20,x8 | `FALL_THROUGH`
<a id="insn-007acc14"></a> `007acc14` | `e9 13 05 b8` | stur w9,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-007acc18"></a> `007acc18` | `ff 57 01 39` | strb wzr,[sp, #0x55] | `FALL_THROUGH`
<a id="insn-007acc1c"></a> `007acc1c` | `f6 13 02 b8` | stur w22,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-007acc20"></a> `007acc20` | `ff 97 00 39` | strb wzr,[sp, #0x25] | `FALL_THROUGH`
<a id="insn-007acc24"></a> `007acc24` | `00 01 62 9e` | scvtf d0,x8 | `FALL_THROUGH`
<a id="insn-007acc28"></a> `007acc28` | `08 00 c4 d2` | mov x8,#0x200000000000 | `FALL_THROUGH`
<a id="insn-007acc2c"></a> `007acc2c` | `88 15 e8 f2` | movk x8,#0x40ac, LSL #48 | `FALL_THROUGH`
<a id="insn-007acc30"></a> `007acc30` | `08 39 60 1e` | fsub d8,d8,d0 | `FALL_THROUGH`
<a id="insn-007acc34"></a> `007acc34` | `00 01 67 9e` | fmov d0,x8 | `FALL_THROUGH`
<a id="insn-007acc38"></a> `007acc38` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-007acc3c"></a> `007acc3c` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acc40"></a> `007acc40` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007acc44"></a> `007acc44` | `00 19 60 1e` | fdiv d0,d8,d0 | `FALL_THROUGH`
<a id="insn-007acc48"></a> `007acc48` | `14 00 78 9e` | fcvtzs x20,d0 | `FALL_THROUGH`
<a id="insn-007acc4c"></a> `007acc4c` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-007acc50"></a> `007acc50` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007acc54"></a> `007acc54` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-007acc58"></a> `007acc58` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-007acc5c"></a> `007acc5c` | `d7 70 fe 97` | bl 0x00748fb8 | `UNCONDITIONAL_CALL`
<a id="insn-007acc60"></a> `007acc60` | `e1 43 01 91` | add x1,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007acc64"></a> `007acc64` | `e2 e3 00 91` | add x2,sp,#0x38 | `FALL_THROUGH`
<a id="insn-007acc68"></a> `007acc68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007acc6c"></a> `007acc6c` | `cc 92 f2 97` | bl 0x0045179c | `UNCONDITIONAL_CALL`
<a id="insn-007acc70"></a> `007acc70` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-007acc74"></a> `007acc74` | `c8 16 00 37` | tbnz w8,#0x0,0x007acf4c | `CONDITIONAL_JUMP`
<a id="insn-007acc78"></a> `007acc78` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007acc7c"></a> `007acc7c` | `08 17 00 37` | tbnz w8,#0x0,0x007acf5c | `CONDITIONAL_JUMP`
<a id="insn-007acc80"></a> `007acc80` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acc84"></a> `007acc84` | `68 00 00 36` | tbz w8,#0x0,0x007acc90 | `CONDITIONAL_JUMP`
<a id="insn-007acc88"></a> `007acc88` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007acc8c"></a> `007acc8c` | `89 ac 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acc90"></a> `007acc90` | `08 c2 81 52` | mov w8,#0xe10 | `FALL_THROUGH`
<a id="insn-007acc94"></a> `007acc94` | `f6 13 02 b8` | stur w22,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-007acc98"></a> `007acc98` | `88 7e 08 9b` | mul x8,x20,x8 | `FALL_THROUGH`
<a id="insn-007acc9c"></a> `007acc9c` | `ff 97 00 39` | strb wzr,[sp, #0x25] | `FALL_THROUGH`
<a id="insn-007acca0"></a> `007acca0` | `00 01 62 9e` | scvtf d0,x8 | `FALL_THROUGH`
<a id="insn-007acca4"></a> `007acca4` | `c8 09 e8 d2` | mov x8,#0x404e000000000000 | `FALL_THROUGH`
<a id="insn-007acca8"></a> `007acca8` | `08 39 60 1e` | fsub d8,d8,d0 | `FALL_THROUGH`
<a id="insn-007accac"></a> `007accac` | `00 01 67 9e` | fmov d0,x8 | `FALL_THROUGH`
<a id="insn-007accb0"></a> `007accb0` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-007accb4"></a> `007accb4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007accb8"></a> `007accb8` | `a8 2d 8d 52` | mov w8,#0x696d | `FALL_THROUGH`
<a id="insn-007accbc"></a> `007accbc` | `c8 0d a0 72` | movk w8,#0x6e, LSL #16 | `FALL_THROUGH`
<a id="insn-007accc0"></a> `007accc0` | `e8 13 05 b8` | stur w8,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-007accc4"></a> `007accc4` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-007accc8"></a> `007accc8` | `00 19 60 1e` | fdiv d0,d8,d0 | `FALL_THROUGH`
<a id="insn-007acccc"></a> `007acccc` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007accd0"></a> `007accd0` | `14 00 78 9e` | fcvtzs x20,d0 | `FALL_THROUGH`
<a id="insn-007accd4"></a> `007accd4` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-007accd8"></a> `007accd8` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007accdc"></a> `007accdc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-007acce0"></a> `007acce0` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-007acce4"></a> `007acce4` | `b5 70 fe 97` | bl 0x00748fb8 | `UNCONDITIONAL_CALL`
<a id="insn-007acce8"></a> `007acce8` | `e1 43 01 91` | add x1,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007accec"></a> `007accec` | `e2 e3 00 91` | add x2,sp,#0x38 | `FALL_THROUGH`
<a id="insn-007accf0"></a> `007accf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007accf4"></a> `007accf4` | `aa 92 f2 97` | bl 0x0045179c | `UNCONDITIONAL_CALL`
<a id="insn-007accf8"></a> `007accf8` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-007accfc"></a> `007accfc` | `a8 13 00 37` | tbnz w8,#0x0,0x007acf70 | `CONDITIONAL_JUMP`
<a id="insn-007acd00"></a> `007acd00` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007acd04"></a> `007acd04` | `e8 13 00 37` | tbnz w8,#0x0,0x007acf80 | `CONDITIONAL_JUMP`
<a id="insn-007acd08"></a> `007acd08` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acd0c"></a> `007acd0c` | `68 00 00 36` | tbz w8,#0x0,0x007acd18 | `CONDITIONAL_JUMP`
<a id="insn-007acd10"></a> `007acd10` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007acd14"></a> `007acd14` | `67 ac 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acd18"></a> `007acd18` | `88 e6 7a d3` | lsl x8,x20,#0x6 | `FALL_THROUGH`
<a id="insn-007acd1c"></a> `007acd1c` | `f6 13 02 b8` | stur w22,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-007acd20"></a> `007acd20` | `ff 97 00 39` | strb wzr,[sp, #0x25] | `FALL_THROUGH`
<a id="insn-007acd24"></a> `007acd24` | `08 09 14 cb` | sub x8,x8,x20, LSL #0x2 | `FALL_THROUGH`
<a id="insn-007acd28"></a> `007acd28` | `00 01 62 9e` | scvtf d0,x8 | `FALL_THROUGH`
<a id="insn-007acd2c"></a> `007acd2c` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-007acd30"></a> `007acd30` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acd34"></a> `007acd34` | `68 ae 8c 52` | mov w8,#0x6573 | `FALL_THROUGH`
<a id="insn-007acd38"></a> `007acd38` | `68 0c a0 72` | movk w8,#0x63, LSL #16 | `FALL_THROUGH`
<a id="insn-007acd3c"></a> `007acd3c` | `e8 13 05 b8` | stur w8,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-007acd40"></a> `007acd40` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-007acd44"></a> `007acd44` | `00 39 60 1e` | fsub d0,d8,d0 | `FALL_THROUGH`
<a id="insn-007acd48"></a> `007acd48` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007acd4c"></a> `007acd4c` | `02 00 78 9e` | fcvtzs x2,d0 | `FALL_THROUGH`
<a id="insn-007acd50"></a> `007acd50` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-007acd54"></a> `007acd54` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007acd58"></a> `007acd58` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-007acd5c"></a> `007acd5c` | `97 70 fe 97` | bl 0x00748fb8 | `UNCONDITIONAL_CALL`
<a id="insn-007acd60"></a> `007acd60` | `e1 43 01 91` | add x1,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007acd64"></a> `007acd64` | `e2 e3 00 91` | add x2,sp,#0x38 | `FALL_THROUGH`
<a id="insn-007acd68"></a> `007acd68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007acd6c"></a> `007acd6c` | `8c 92 f2 97` | bl 0x0045179c | `UNCONDITIONAL_CALL`
<a id="insn-007acd70"></a> `007acd70` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-007acd74"></a> `007acd74` | `08 11 00 37` | tbnz w8,#0x0,0x007acf94 | `CONDITIONAL_JUMP`
<a id="insn-007acd78"></a> `007acd78` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007acd7c"></a> `007acd7c` | `48 11 00 37` | tbnz w8,#0x0,0x007acfa4 | `CONDITIONAL_JUMP`
<a id="insn-007acd80"></a> `007acd80` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acd84"></a> `007acd84` | `68 00 00 36` | tbz w8,#0x0,0x007acd90 | `CONDITIONAL_JUMP`
<a id="insn-007acd88"></a> `007acd88` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007acd8c"></a> `007acd8c` | `49 ac 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acd90"></a> `007acd90` | `78 27 00 d0` | adrp x24,0xc9a000 | `FALL_THROUGH`
<a id="insn-007acd94"></a> `007acd94` | `77 27 00 d0` | adrp x23,0xc9a000 | `FALL_THROUGH`
<a id="insn-007acd98"></a> `007acd98` | `f6 43 01 91` | add x22,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007acd9c"></a> `007acd9c` | `18 47 46 f9` | ldr x24,[x24, #0xc88] | `FALL_THROUGH`
<a id="insn-007acda0"></a> `007acda0` | `f7 de 45 f9` | ldr x23,[x23, #0xbb8] | `FALL_THROUGH`
<a id="insn-007acda4"></a> `007acda4` | `ff 7b 00 f9` | str xzr,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-007acda8"></a> `007acda8` | `e8 a6 40 a9` | ldp x8,x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-007acdac"></a> `007acdac` | `19 03 01 91` | add x25,x24,#0x40 | `FALL_THROUGH`
<a id="insn-007acdb0"></a> `007acdb0` | `f9 63 00 f9` | str x25,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-007acdb4"></a> `007acdb4` | `e8 2b 00 f9` | str x8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acdb8"></a> `007acdb8` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-007acdbc"></a> `007acdbc` | `c9 6a 28 f8` | str x9,[x22, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007acdc0"></a> `007acdc0` | `e8 2b 40 f9` | ldr x8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acdc4"></a> `007acdc4` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-007acdc8"></a> `007acdc8` | `d4 02 08 8b` | add x20,x22,x8 | `FALL_THROUGH`
<a id="insn-007acdcc"></a> `007acdcc` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-007acdd0"></a> `007acdd0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007acdd4"></a> `007acdd4` | `03 ad 12 94` | bl 0x00c581e0 | `UNCONDITIONAL_CALL`
<a id="insn-007acdd8"></a> `007acdd8` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-007acddc"></a> `007acddc` | `09 63 00 91` | add x9,x24,#0x18 | `FALL_THROUGH`
<a id="insn-007acde0"></a> `007acde0` | `9f 46 00 f9` | str xzr,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-007acde4"></a> `007acde4` | `88 92 00 b9` | str w8,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-007acde8"></a> `007acde8` | `e9 2b 00 f9` | str x9,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acdec"></a> `007acdec` | `f9 63 00 f9` | str x25,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-007acdf0"></a> `007acdf0` | `c0 22 00 91` | add x0,x22,#0x8 | `FALL_THROUGH`
<a id="insn-007acdf4"></a> `007acdf4` | `ff ac 12 94` | bl 0x00c581f0 | `UNCONDITIONAL_CALL`
<a id="insn-007acdf8"></a> `007acdf8` | `74 27 00 d0` | adrp x20,0xc9a000 | `FALL_THROUGH`
<a id="insn-007acdfc"></a> `007acdfc` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-007ace00"></a> `007ace00` | `e9 43 01 91` | add x9,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007ace04"></a> `007ace04` | `94 e2 45 f9` | ldr x20,[x20, #0xbc0] | `FALL_THROUGH`
<a id="insn-007ace08"></a> `007ace08` | `88 42 00 91` | add x8,x20,#0x10 | `FALL_THROUGH`
<a id="insn-007ace0c"></a> `007ace0c` | `e8 2f 00 f9` | str x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-007ace10"></a> `007ace10` | `08 02 80 52` | mov w8,#0x10 | `FALL_THROUGH`
<a id="insn-007ace14"></a> `007ace14` | `20 81 84 3c` | stur q0,[x9, #0x48] | `FALL_THROUGH`
<a id="insn-007ace18"></a> `007ace18` | `20 81 85 3c` | stur q0,[x9, #0x58] | `FALL_THROUGH`
<a id="insn-007ace1c"></a> `007ace1c` | `e8 bb 00 b9` | str w8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-007ace20"></a> `007ace20` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007ace24"></a> `007ace24` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-007ace28"></a> `007ace28` | `ec 92 f2 97` | bl 0x004519d8 | `UNCONDITIONAL_CALL`
<a id="insn-007ace2c"></a> `007ace2c` | `c8 01 80 52` | mov w8,#0xe | `FALL_THROUGH`
<a id="insn-007ace30"></a> `007ace30` | `69 ae 8c 52` | mov w9,#0x6573 | `FALL_THROUGH`
<a id="insn-007ace34"></a> `007ace34` | `ff 03 01 39` | strb wzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007ace38"></a> `007ace38` | `e8 e3 00 39` | strb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-007ace3c"></a> `007ace3c` | `88 2a 8d 52` | mov w8,#0x6954 | `FALL_THROUGH`
<a id="insn-007ace40"></a> `007ace40` | `89 8e aa 72` | movk w9,#0x5474, LSL #16 | `FALL_THROUGH`
<a id="insn-007ace44"></a> `007ace44` | `a8 ad ac 72` | movk w8,#0x656d, LSL #16 | `FALL_THROUGH`
<a id="insn-007ace48"></a> `007ace48` | `e9 93 03 b8` | stur w9,[sp, #0x39] | `FALL_THROUGH`
<a id="insn-007ace4c"></a> `007ace4c` | `e8 3f 00 b9` | str w8,[sp, #0x3c] | `FALL_THROUGH`
<a id="insn-007ace50"></a> `007ace50` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007ace54"></a> `007ace54` | `c0 22 00 91` | add x0,x22,#0x8 | `FALL_THROUGH`
<a id="insn-007ace58"></a> `007ace58` | `d6 ac 12 94` | bl 0x00c581b0 | `UNCONDITIONAL_CALL`
<a id="insn-007ace5c"></a> `007ace5c` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-007ace60"></a> `007ace60` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007ace64"></a> `007ace64` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-007ace68"></a> `007ace68` | `b3 86 0d 94` | bl 0x00b0e934 | `UNCONDITIONAL_CALL`
<a id="insn-007ace6c"></a> `007ace6c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007ace70"></a> `007ace70` | `68 00 00 36` | tbz w8,#0x0,0x007ace7c | `CONDITIONAL_JUMP`
<a id="insn-007ace74"></a> `007ace74` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007ace78"></a> `007ace78` | `0e ac 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007ace7c"></a> `007ace7c` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-007ace80"></a> `007ace80` | `68 00 00 36` | tbz w8,#0x0,0x007ace8c | `CONDITIONAL_JUMP`
<a id="insn-007ace84"></a> `007ace84` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-007ace88"></a> `007ace88` | `0a ac 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007ace8c"></a> `007ace8c` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-007ace90"></a> `007ace90` | `e9 0e 40 f9` | ldr x9,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-007ace94"></a> `007ace94` | `ea 43 01 91` | add x10,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007ace98"></a> `007ace98` | `e8 2b 00 f9` | str x8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007ace9c"></a> `007ace9c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-007acea0"></a> `007acea0` | `49 69 28 f8` | str x9,[x10, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007acea4"></a> `007acea4` | `89 42 00 91` | add x9,x20,#0x10 | `FALL_THROUGH`
<a id="insn-007acea8"></a> `007acea8` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-007aceac"></a> `007aceac` | `e9 2f 00 f9` | str x9,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-007aceb0"></a> `007aceb0` | `68 00 00 36` | tbz w8,#0x0,0x007acebc | `CONDITIONAL_JUMP`
<a id="insn-007aceb4"></a> `007aceb4` | `e0 57 40 f9` | ldr x0,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-007aceb8"></a> `007aceb8` | `fe ab 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acebc"></a> `007acebc` | `c0 22 00 91` | add x0,x22,#0x8 | `FALL_THROUGH`
<a id="insn-007acec0"></a> `007acec0` | `38 ac 12 94` | bl 0x00c57fa0 | `UNCONDITIONAL_CALL`
<a id="insn-007acec4"></a> `007acec4` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007acec8"></a> `007acec8` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-007acecc"></a> `007acecc` | `39 ac 12 94` | bl 0x00c57fb0 | `UNCONDITIONAL_CALL`
<a id="insn-007aced0"></a> `007aced0` | `c0 c2 01 91` | add x0,x22,#0x70 | `FALL_THROUGH`
<a id="insn-007aced4"></a> `007aced4` | `3b ac 12 94` | bl 0x00c57fc0 | `UNCONDITIONAL_CALL`
<a id="insn-007aced8"></a> `007aced8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-007acedc"></a> `007acedc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007acee0"></a> `007acee0` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-007acee4"></a> `007acee4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007acee8"></a> `007acee8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-007aceec"></a> `007aceec` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-007acef0"></a> `007acef0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007acef4"></a> `007acef4` | `61 10 00 54` | b.ne 0x007ad100 | `CONDITIONAL_JUMP`
<a id="insn-007acef8"></a> `007acef8` | `f4 4f 5b a9` | ldp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-007acefc"></a> `007acefc` | `e8 b3 40 fd` | ldr d8,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-007acf00"></a> `007acf00` | `f6 57 5a a9` | ldp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-007acf04"></a> `007acf04` | `f8 5f 59 a9` | ldp x24,x23,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-007acf08"></a> `007acf08` | `fc 67 58 a9` | ldp x28,x25,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-007acf0c"></a> `007acf0c` | `fd 7b 57 a9` | ldp x29,x30,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-007acf10"></a> `007acf10` | `ff 03 07 91` | add sp,sp,#0x1c0 | `FALL_THROUGH`
<a id="insn-007acf14"></a> `007acf14` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007acf18"></a> `007acf18` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-007acf1c"></a> `007acf1c` | `e5 ab 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acf20"></a> `007acf20` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007acf24"></a> `007acf24` | `e8 e5 07 36` | tbz w8,#0x0,0x007acbe0 | `CONDITIONAL_JUMP`
<a id="insn-007acf28"></a> `007acf28` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007acf2c"></a> `007acf2c` | `e1 ab 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acf30"></a> `007acf30` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007acf34"></a> `007acf34` | `a8 e5 07 36` | tbz w8,#0x0,0x007acbe8 | `CONDITIONAL_JUMP`
<a id="insn-007acf38"></a> `007acf38` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007acf3c"></a> `007acf3c` | `dd ab 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acf40"></a> `007acf40` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acf44"></a> `007acf44` | `68 e5 07 37` | tbnz w8,#0x0,0x007acbf0 | `CONDITIONAL_JUMP`
<a id="insn-007acf48"></a> `007acf48` | `2c ff ff 17` | b 0x007acbf8 | `UNCONDITIONAL_JUMP`
<a id="insn-007acf4c"></a> `007acf4c` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-007acf50"></a> `007acf50` | `d8 ab 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acf54"></a> `007acf54` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007acf58"></a> `007acf58` | `48 e9 07 36` | tbz w8,#0x0,0x007acc80 | `CONDITIONAL_JUMP`
<a id="insn-007acf5c"></a> `007acf5c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007acf60"></a> `007acf60` | `d4 ab 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acf64"></a> `007acf64` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acf68"></a> `007acf68` | `08 e9 07 37` | tbnz w8,#0x0,0x007acc88 | `CONDITIONAL_JUMP`
<a id="insn-007acf6c"></a> `007acf6c` | `49 ff ff 17` | b 0x007acc90 | `UNCONDITIONAL_JUMP`
<a id="insn-007acf70"></a> `007acf70` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-007acf74"></a> `007acf74` | `cf ab 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acf78"></a> `007acf78` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007acf7c"></a> `007acf7c` | `68 ec 07 36` | tbz w8,#0x0,0x007acd08 | `CONDITIONAL_JUMP`
<a id="insn-007acf80"></a> `007acf80` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007acf84"></a> `007acf84` | `cb ab 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acf88"></a> `007acf88` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acf8c"></a> `007acf8c` | `28 ec 07 37` | tbnz w8,#0x0,0x007acd10 | `CONDITIONAL_JUMP`
<a id="insn-007acf90"></a> `007acf90` | `62 ff ff 17` | b 0x007acd18 | `UNCONDITIONAL_JUMP`
<a id="insn-007acf94"></a> `007acf94` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-007acf98"></a> `007acf98` | `c6 ab 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acf9c"></a> `007acf9c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007acfa0"></a> `007acfa0` | `08 ef 07 36` | tbz w8,#0x0,0x007acd80 | `CONDITIONAL_JUMP`
<a id="insn-007acfa4"></a> `007acfa4` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007acfa8"></a> `007acfa8` | `c2 ab 12 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-007acfac"></a> `007acfac` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007acfb0"></a> `007acfb0` | `c8 ee 07 37` | tbnz w8,#0x0,0x007acd88 | `CONDITIONAL_JUMP`
<a id="insn-007acfb4"></a> `007acfb4` | `77 ff ff 17` | b 0x007acd90 | `UNCONDITIONAL_JUMP`
<a id="insn-007ad100"></a> `007ad100` | `78 ab 12 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007acacc`](#insn-007acacc) 範囲 `[['007acacc', '007acbd7']]`
  - `CONDITIONAL_JUMP` [`007acbd4`](#insn-007acbd4) → [`007acf18`](#insn-007acf18)
  - `FALL_THROUGH` [`007acbd4`](#insn-007acbd4) → [`007acbd8`](#insn-007acbd8)
- ブロック [`007acbd8`](#insn-007acbd8) 範囲 `[['007acbd8', '007acbdf']]`
  - `CONDITIONAL_JUMP` [`007acbdc`](#insn-007acbdc) → [`007acf28`](#insn-007acf28)
  - `FALL_THROUGH` [`007acbdc`](#insn-007acbdc) → [`007acbe0`](#insn-007acbe0)
- ブロック [`007acbe0`](#insn-007acbe0) 範囲 `[['007acbe0', '007acbe7']]`
  - `CONDITIONAL_JUMP` [`007acbe4`](#insn-007acbe4) → [`007acf38`](#insn-007acf38)
  - `FALL_THROUGH` [`007acbe4`](#insn-007acbe4) → [`007acbe8`](#insn-007acbe8)
- ブロック [`007acbe8`](#insn-007acbe8) 範囲 `[['007acbe8', '007acbef']]`
  - `CONDITIONAL_JUMP` [`007acbec`](#insn-007acbec) → [`007acbf8`](#insn-007acbf8)
  - `FALL_THROUGH` [`007acbec`](#insn-007acbec) → [`007acbf0`](#insn-007acbf0)
- ブロック [`007acbf0`](#insn-007acbf0) 範囲 `[['007acbf0', '007acbf7']]`
  - `FALL_THROUGH` [`007acbf4`](#insn-007acbf4) → [`007acbf8`](#insn-007acbf8)
- ブロック [`007acbf8`](#insn-007acbf8) 範囲 `[['007acbf8', '007acc77']]`
  - `CONDITIONAL_JUMP` [`007acc74`](#insn-007acc74) → [`007acf4c`](#insn-007acf4c)
  - `FALL_THROUGH` [`007acc74`](#insn-007acc74) → [`007acc78`](#insn-007acc78)
- ブロック [`007acc78`](#insn-007acc78) 範囲 `[['007acc78', '007acc7f']]`
  - `CONDITIONAL_JUMP` [`007acc7c`](#insn-007acc7c) → [`007acf5c`](#insn-007acf5c)
  - `FALL_THROUGH` [`007acc7c`](#insn-007acc7c) → [`007acc80`](#insn-007acc80)
- ブロック [`007acc80`](#insn-007acc80) 範囲 `[['007acc80', '007acc87']]`
  - `CONDITIONAL_JUMP` [`007acc84`](#insn-007acc84) → [`007acc90`](#insn-007acc90)
  - `FALL_THROUGH` [`007acc84`](#insn-007acc84) → [`007acc88`](#insn-007acc88)
- ブロック [`007acc88`](#insn-007acc88) 範囲 `[['007acc88', '007acc8f']]`
  - `FALL_THROUGH` [`007acc8c`](#insn-007acc8c) → [`007acc90`](#insn-007acc90)
- ブロック [`007acc90`](#insn-007acc90) 範囲 `[['007acc90', '007accff']]`
  - `CONDITIONAL_JUMP` [`007accfc`](#insn-007accfc) → [`007acf70`](#insn-007acf70)
  - `FALL_THROUGH` [`007accfc`](#insn-007accfc) → [`007acd00`](#insn-007acd00)
- ブロック [`007acd00`](#insn-007acd00) 範囲 `[['007acd00', '007acd07']]`
  - `CONDITIONAL_JUMP` [`007acd04`](#insn-007acd04) → [`007acf80`](#insn-007acf80)
  - `FALL_THROUGH` [`007acd04`](#insn-007acd04) → [`007acd08`](#insn-007acd08)
- ブロック [`007acd08`](#insn-007acd08) 範囲 `[['007acd08', '007acd0f']]`
  - `CONDITIONAL_JUMP` [`007acd0c`](#insn-007acd0c) → [`007acd18`](#insn-007acd18)
  - `FALL_THROUGH` [`007acd0c`](#insn-007acd0c) → [`007acd10`](#insn-007acd10)
- ブロック [`007acd10`](#insn-007acd10) 範囲 `[['007acd10', '007acd17']]`
  - `FALL_THROUGH` [`007acd14`](#insn-007acd14) → [`007acd18`](#insn-007acd18)
- ブロック [`007acd18`](#insn-007acd18) 範囲 `[['007acd18', '007acd77']]`
  - `CONDITIONAL_JUMP` [`007acd74`](#insn-007acd74) → [`007acf94`](#insn-007acf94)
  - `FALL_THROUGH` [`007acd74`](#insn-007acd74) → [`007acd78`](#insn-007acd78)
- ブロック [`007acd78`](#insn-007acd78) 範囲 `[['007acd78', '007acd7f']]`
  - `CONDITIONAL_JUMP` [`007acd7c`](#insn-007acd7c) → [`007acfa4`](#insn-007acfa4)
  - `FALL_THROUGH` [`007acd7c`](#insn-007acd7c) → [`007acd80`](#insn-007acd80)
- ブロック [`007acd80`](#insn-007acd80) 範囲 `[['007acd80', '007acd87']]`
  - `CONDITIONAL_JUMP` [`007acd84`](#insn-007acd84) → [`007acd90`](#insn-007acd90)
  - `FALL_THROUGH` [`007acd84`](#insn-007acd84) → [`007acd88`](#insn-007acd88)
- ブロック [`007acd88`](#insn-007acd88) 範囲 `[['007acd88', '007acd8f']]`
  - `FALL_THROUGH` [`007acd8c`](#insn-007acd8c) → [`007acd90`](#insn-007acd90)
- ブロック [`007acd90`](#insn-007acd90) 範囲 `[['007acd90', '007ace73']]`
  - `CONDITIONAL_JUMP` [`007ace70`](#insn-007ace70) → [`007ace7c`](#insn-007ace7c)
  - `FALL_THROUGH` [`007ace70`](#insn-007ace70) → [`007ace74`](#insn-007ace74)
- ブロック [`007ace74`](#insn-007ace74) 範囲 `[['007ace74', '007ace7b']]`
  - `FALL_THROUGH` [`007ace78`](#insn-007ace78) → [`007ace7c`](#insn-007ace7c)
- ブロック [`007ace7c`](#insn-007ace7c) 範囲 `[['007ace7c', '007ace83']]`
  - `CONDITIONAL_JUMP` [`007ace80`](#insn-007ace80) → [`007ace8c`](#insn-007ace8c)
  - `FALL_THROUGH` [`007ace80`](#insn-007ace80) → [`007ace84`](#insn-007ace84)
- ブロック [`007ace84`](#insn-007ace84) 範囲 `[['007ace84', '007ace8b']]`
  - `FALL_THROUGH` [`007ace88`](#insn-007ace88) → [`007ace8c`](#insn-007ace8c)
- ブロック [`007ace8c`](#insn-007ace8c) 範囲 `[['007ace8c', '007aceb3']]`
  - `CONDITIONAL_JUMP` [`007aceb0`](#insn-007aceb0) → [`007acebc`](#insn-007acebc)
  - `FALL_THROUGH` [`007aceb0`](#insn-007aceb0) → [`007aceb4`](#insn-007aceb4)
- ブロック [`007aceb4`](#insn-007aceb4) 範囲 `[['007aceb4', '007acebb']]`
  - `FALL_THROUGH` [`007aceb8`](#insn-007aceb8) → [`007acebc`](#insn-007acebc)
- ブロック [`007acebc`](#insn-007acebc) 範囲 `[['007acebc', '007acef7']]`
  - `CONDITIONAL_JUMP` [`007acef4`](#insn-007acef4) → [`007ad100`](#insn-007ad100)
  - `FALL_THROUGH` [`007acef4`](#insn-007acef4) → [`007acef8`](#insn-007acef8)
- ブロック [`007acef8`](#insn-007acef8) 範囲 `[['007acef8', '007acf17']]`
- ブロック [`007acf18`](#insn-007acf18) 範囲 `[['007acf18', '007acf27']]`
  - `CONDITIONAL_JUMP` [`007acf24`](#insn-007acf24) → [`007acbe0`](#insn-007acbe0)
  - `FALL_THROUGH` [`007acf24`](#insn-007acf24) → [`007acf28`](#insn-007acf28)
- ブロック [`007acf28`](#insn-007acf28) 範囲 `[['007acf28', '007acf37']]`
  - `CONDITIONAL_JUMP` [`007acf34`](#insn-007acf34) → [`007acbe8`](#insn-007acbe8)
  - `FALL_THROUGH` [`007acf34`](#insn-007acf34) → [`007acf38`](#insn-007acf38)
- ブロック [`007acf38`](#insn-007acf38) 範囲 `[['007acf38', '007acf47']]`
  - `CONDITIONAL_JUMP` [`007acf44`](#insn-007acf44) → [`007acbf0`](#insn-007acbf0)
  - `FALL_THROUGH` [`007acf44`](#insn-007acf44) → [`007acf48`](#insn-007acf48)
- ブロック [`007acf48`](#insn-007acf48) 範囲 `[['007acf48', '007acf4b']]`
  - `UNCONDITIONAL_JUMP` [`007acf48`](#insn-007acf48) → [`007acbf8`](#insn-007acbf8)
- ブロック [`007acf4c`](#insn-007acf4c) 範囲 `[['007acf4c', '007acf5b']]`
  - `CONDITIONAL_JUMP` [`007acf58`](#insn-007acf58) → [`007acc80`](#insn-007acc80)
  - `FALL_THROUGH` [`007acf58`](#insn-007acf58) → [`007acf5c`](#insn-007acf5c)
- ブロック [`007acf5c`](#insn-007acf5c) 範囲 `[['007acf5c', '007acf6b']]`
  - `CONDITIONAL_JUMP` [`007acf68`](#insn-007acf68) → [`007acc88`](#insn-007acc88)
  - `FALL_THROUGH` [`007acf68`](#insn-007acf68) → [`007acf6c`](#insn-007acf6c)
- ブロック [`007acf6c`](#insn-007acf6c) 範囲 `[['007acf6c', '007acf6f']]`
  - `UNCONDITIONAL_JUMP` [`007acf6c`](#insn-007acf6c) → [`007acc90`](#insn-007acc90)
- ブロック [`007acf70`](#insn-007acf70) 範囲 `[['007acf70', '007acf7f']]`
  - `CONDITIONAL_JUMP` [`007acf7c`](#insn-007acf7c) → [`007acd08`](#insn-007acd08)
  - `FALL_THROUGH` [`007acf7c`](#insn-007acf7c) → [`007acf80`](#insn-007acf80)
- ブロック [`007acf80`](#insn-007acf80) 範囲 `[['007acf80', '007acf8f']]`
  - `CONDITIONAL_JUMP` [`007acf8c`](#insn-007acf8c) → [`007acd10`](#insn-007acd10)
  - `FALL_THROUGH` [`007acf8c`](#insn-007acf8c) → [`007acf90`](#insn-007acf90)
- ブロック [`007acf90`](#insn-007acf90) 範囲 `[['007acf90', '007acf93']]`
  - `UNCONDITIONAL_JUMP` [`007acf90`](#insn-007acf90) → [`007acd18`](#insn-007acd18)
- ブロック [`007acf94`](#insn-007acf94) 範囲 `[['007acf94', '007acfa3']]`
  - `CONDITIONAL_JUMP` [`007acfa0`](#insn-007acfa0) → [`007acd80`](#insn-007acd80)
  - `FALL_THROUGH` [`007acfa0`](#insn-007acfa0) → [`007acfa4`](#insn-007acfa4)
- ブロック [`007acfa4`](#insn-007acfa4) 範囲 `[['007acfa4', '007acfb3']]`
  - `CONDITIONAL_JUMP` [`007acfb0`](#insn-007acfb0) → [`007acd88`](#insn-007acd88)
  - `FALL_THROUGH` [`007acfb0`](#insn-007acfb0) → [`007acfb4`](#insn-007acfb4)
- ブロック [`007acfb4`](#insn-007acfb4) 範囲 `[['007acfb4', '007acfb7']]`
  - `UNCONDITIONAL_JUMP` [`007acfb4`](#insn-007acfb4) → [`007acd90`](#insn-007acd90)
- ブロック [`007ad100`](#insn-007ad100) 範囲 `[['007ad100', '007ad103']]`

## 命令位置別の参照

- [`007acad0`](#insn-007acad0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acad4`](#insn-007acad4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acad8`](#insn-007acad8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acadc`](#insn-007acadc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acae0`](#insn-007acae0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acae4`](#insn-007acae4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acafc`](#insn-007acafc) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acb00`](#insn-007acb00) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`007acb1c`](#insn-007acb1c) → `00c63ae0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007acb30`](#insn-007acb30) → [`00597e48`](../00597/00597e48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00597e48` · 推定シンボル `None` · 推定型 `None`
- [`007acb38`](#insn-007acb38) → [`00597a8c`](../00597/00597a8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00597a8c` · 推定シンボル `None` · 推定型 `None`
- [`007acb48`](#insn-007acb48) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acb5c`](#insn-007acb5c) → `Stack[-0x1a1]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acb60`](#insn-007acb60) → `Stack[-0x16f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acb68`](#insn-007acb68) → `002c034e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007acb74`](#insn-007acb74) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acb78`](#insn-007acb78) → `002c035c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007acb7c`](#insn-007acb7c) → `Stack[-0x1b7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acb80`](#insn-007acb80) → `Stack[-0x1a9]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acb94`](#insn-007acb94) → [`0048ce54`](../0048c/0048ce54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce54` · 推定シンボル `None` · 推定型 `None`
- [`007acbbc`](#insn-007acbbc) → [`00748fb8`](../00748/00748fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00748fb8` · 推定シンボル `None` · 推定型 `None`
- [`007acbcc`](#insn-007acbcc) → [`0045179c`](../00451/0045179c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045179c` · 推定シンボル `None` · 推定型 `None`
- [`007acbd0`](#insn-007acbd0) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acbd4`](#insn-007acbd4) → [`007acf18`](#insn-007acf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acbd8`](#insn-007acbd8) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acbdc`](#insn-007acbdc) → [`007acf28`](#insn-007acf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acbe0`](#insn-007acbe0) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acbe4`](#insn-007acbe4) → [`007acf38`](#insn-007acf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acbe8`](#insn-007acbe8) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acbec`](#insn-007acbec) → [`007acbf8`](#insn-007acbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acbf0`](#insn-007acbf0) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acbf4`](#insn-007acbf4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acc14`](#insn-007acc14) → `Stack[-0x16f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc18`](#insn-007acc18) → `Stack[-0x16b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc1c`](#insn-007acc1c) → `Stack[-0x19f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc20`](#insn-007acc20) → `Stack[-0x19b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc3c`](#insn-007acc3c) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc40`](#insn-007acc40) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc5c`](#insn-007acc5c) → [`00748fb8`](../00748/00748fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00748fb8` · 推定シンボル `None` · 推定型 `None`
- [`007acc6c`](#insn-007acc6c) → [`0045179c`](../00451/0045179c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045179c` · 推定シンボル `None` · 推定型 `None`
- [`007acc70`](#insn-007acc70) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc74`](#insn-007acc74) → [`007acf4c`](#insn-007acf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc78`](#insn-007acc78) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc7c`](#insn-007acc7c) → [`007acf5c`](#insn-007acf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc80`](#insn-007acc80) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc84`](#insn-007acc84) → [`007acc90`](#insn-007acc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc88`](#insn-007acc88) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc8c`](#insn-007acc8c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acc94`](#insn-007acc94) → `Stack[-0x19f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acc9c`](#insn-007acc9c) → `Stack[-0x19b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007accb4`](#insn-007accb4) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007accc0`](#insn-007accc0) → `Stack[-0x16f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acccc`](#insn-007acccc) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acce4`](#insn-007acce4) → [`00748fb8`](../00748/00748fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00748fb8` · 推定シンボル `None` · 推定型 `None`
- [`007accf4`](#insn-007accf4) → [`0045179c`](../00451/0045179c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045179c` · 推定シンボル `None` · 推定型 `None`
- [`007accf8`](#insn-007accf8) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007accfc`](#insn-007accfc) → [`007acf70`](#insn-007acf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd00`](#insn-007acd00) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd04`](#insn-007acd04) → [`007acf80`](#insn-007acf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd08`](#insn-007acd08) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd0c`](#insn-007acd0c) → [`007acd18`](#insn-007acd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd10`](#insn-007acd10) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd14`](#insn-007acd14) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acd1c`](#insn-007acd1c) → `Stack[-0x19f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd20`](#insn-007acd20) → `Stack[-0x19b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd30`](#insn-007acd30) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd3c`](#insn-007acd3c) → `Stack[-0x16f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd48`](#insn-007acd48) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd5c`](#insn-007acd5c) → [`00748fb8`](../00748/00748fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00748fb8` · 推定シンボル `None` · 推定型 `None`
- [`007acd6c`](#insn-007acd6c) → [`0045179c`](../00451/0045179c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045179c` · 推定シンボル `None` · 推定型 `None`
- [`007acd70`](#insn-007acd70) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd74`](#insn-007acd74) → [`007acf94`](#insn-007acf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd78`](#insn-007acd78) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd7c`](#insn-007acd7c) → [`007acfa4`](#insn-007acfa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd80`](#insn-007acd80) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd84`](#insn-007acd84) → [`007acd90`](#insn-007acd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd88`](#insn-007acd88) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acd8c`](#insn-007acd8c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acd9c`](#insn-007acd9c) → `00c9ac88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007acda0`](#insn-007acda0) → `00c9abb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007acda4`](#insn-007acda4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acda8`](#insn-007acda8) → `00c93208`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`007acda8`](#insn-007acda8) → `00c93210`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`007acdb0`](#insn-007acdb0) → `00c91038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007acdb0`](#insn-007acdb0) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acdb4`](#insn-007acdb4) → `00c91060`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007acdb4`](#insn-007acdb4) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acdb8`](#insn-007acdb8) → `00c91048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTCNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE0_NS_13basic_ostreamIcS2_EE` · 推定型 `undefined8`
- [`007acdbc`](#insn-007acdbc) → `00c91088`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007acdc0`](#insn-007acdc0) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acdc4`](#insn-007acdc4) → `00c91048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTCNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE0_NS_13basic_ostreamIcS2_EE` · 推定型 `undefined8`
- [`007acdd4`](#insn-007acdd4) → [`00c581e0`](../00c58/00c581e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581e0` · 推定シンボル `None` · 推定型 `None`
- [`007acde0`](#insn-007acde0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acde4`](#insn-007acde4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acde8`](#insn-007acde8) → `00c91010`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007acde8`](#insn-007acde8) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acdec`](#insn-007acdec) → `00c91038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007acdec`](#insn-007acdec) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acdf4`](#insn-007acdf4) → [`00c581f0`](../00c58/00c581f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581f0` · 推定シンボル `None` · 推定型 `None`
- [`007ace04`](#insn-007ace04) → `00c9abc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007ace0c`](#insn-007ace0c) → `00c90c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`007ace0c`](#insn-007ace0c) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace14`](#insn-007ace14) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace18`](#insn-007ace18) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace1c`](#insn-007ace1c) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace28`](#insn-007ace28) → [`004519d8`](../00451/004519d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004519d8` · 推定シンボル `None` · 推定型 `None`
- [`007ace34`](#insn-007ace34) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace38`](#insn-007ace38) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace48`](#insn-007ace48) → `Stack[-0x187]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace4c`](#insn-007ace4c) → `Stack[-0x184]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace58`](#insn-007ace58) → [`00c581b0`](../00c58/00c581b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581b0` · 推定シンボル `None` · 推定型 `None`
- [`007ace68`](#insn-007ace68) → [`00b0e934`](../00b0e/00b0e934.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0e934` · 推定シンボル `None` · 推定型 `None`
- [`007ace6c`](#insn-007ace6c) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace70`](#insn-007ace70) → [`007ace7c`](#insn-007ace7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace74`](#insn-007ace74) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace78`](#insn-007ace78) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007ace7c`](#insn-007ace7c) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace80`](#insn-007ace80) → [`007ace8c`](#insn-007ace8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace84`](#insn-007ace84) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace88`](#insn-007ace88) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007ace8c`](#insn-007ace8c) → `00c93200`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`007ace90`](#insn-007ace90) → `00c93218`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`007ace98`](#insn-007ace98) → `00c91010`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007ace98`](#insn-007ace98) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ace9c`](#insn-007ace9c) → `00c90ff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`007acea0`](#insn-007acea0) → `00c91038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007acea8`](#insn-007acea8) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aceac`](#insn-007aceac) → `00c90c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`007aceac`](#insn-007aceac) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aceb0`](#insn-007aceb0) → [`007acebc`](#insn-007acebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aceb4`](#insn-007aceb4) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aceb8`](#insn-007aceb8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acec0`](#insn-007acec0) → [`00c57fa0`](../00c57/00c57fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fa0` · 推定シンボル `None` · 推定型 `None`
- [`007acec8`](#insn-007acec8) → `00c93208`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`007acecc`](#insn-007acecc) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`
- [`007aced4`](#insn-007aced4) → [`00c57fc0`](../00c57/00c57fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fc0` · 推定シンボル `None` · 推定型 `None`
- [`007acee0`](#insn-007acee0) → `00c63ae8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007acee4`](#insn-007acee4) → [`0045bdf8`](../0045b/0045bdf8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0045bdf8` · 推定シンボル `None` · 推定型 `None`
- [`007aceec`](#insn-007aceec) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acef4`](#insn-007acef4) → [`007ad100`](#insn-007ad100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acef8`](#insn-007acef8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acefc`](#insn-007acefc) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf00`](#insn-007acf00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf04`](#insn-007acf04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf08`](#insn-007acf08) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf0c`](#insn-007acf0c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf18`](#insn-007acf18) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf1c`](#insn-007acf1c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acf20`](#insn-007acf20) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf24`](#insn-007acf24) → [`007acbe0`](#insn-007acbe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf28`](#insn-007acf28) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf2c`](#insn-007acf2c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acf30`](#insn-007acf30) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf34`](#insn-007acf34) → [`007acbe8`](#insn-007acbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf38`](#insn-007acf38) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf3c`](#insn-007acf3c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acf40`](#insn-007acf40) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf44`](#insn-007acf44) → [`007acbf0`](#insn-007acbf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf48`](#insn-007acf48) → [`007acbf8`](#insn-007acbf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf4c`](#insn-007acf4c) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf50`](#insn-007acf50) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acf54`](#insn-007acf54) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf58`](#insn-007acf58) → [`007acc80`](#insn-007acc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf5c`](#insn-007acf5c) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf60`](#insn-007acf60) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acf64`](#insn-007acf64) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf68`](#insn-007acf68) → [`007acc88`](#insn-007acc88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf6c`](#insn-007acf6c) → [`007acc90`](#insn-007acc90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf70`](#insn-007acf70) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf74`](#insn-007acf74) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acf78`](#insn-007acf78) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf7c`](#insn-007acf7c) → [`007acd08`](#insn-007acd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf80`](#insn-007acf80) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf84`](#insn-007acf84) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acf88`](#insn-007acf88) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf8c`](#insn-007acf8c) → [`007acd10`](#insn-007acd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf90`](#insn-007acf90) → [`007acd18`](#insn-007acd18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf94`](#insn-007acf94) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acf98`](#insn-007acf98) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acf9c`](#insn-007acf9c) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acfa0`](#insn-007acfa0) → [`007acd80`](#insn-007acd80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acfa4`](#insn-007acfa4) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acfa8`](#insn-007acfa8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`007acfac`](#insn-007acfac) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acfb0`](#insn-007acfb0) → [`007acd88`](#insn-007acd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007acfb4`](#insn-007acfb4) → [`007acd90`](#insn-007acd90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ad100`](#insn-007ad100) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007acad0`](#insn-007acad0)

~~~json
{
  "source": "007acad0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acad4`](#insn-007acad4)

~~~json
{
  "source": "007acad4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acad8`](#insn-007acad8)

~~~json
{
  "source": "007acad8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acadc`](#insn-007acadc)

~~~json
{
  "source": "007acadc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acae0`](#insn-007acae0)

~~~json
{
  "source": "007acae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acae4`](#insn-007acae4)

~~~json
{
  "source": "007acae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acafc`](#insn-007acafc)

~~~json
{
  "source": "007acafc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acb00`](#insn-007acb00)

~~~json
{
  "source": "007acb00",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acb1c`](#insn-007acb1c)

~~~json
{
  "source": "007acb1c",
  "target": "00c63ae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63ae0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acb30`](#insn-007acb30)

~~~json
{
  "source": "007acb30",
  "target": "00597e48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acb38`](#insn-007acb38)

~~~json
{
  "source": "007acb38",
  "target": "00597a8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acb48`](#insn-007acb48)

~~~json
{
  "source": "007acb48",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acb5c`](#insn-007acb5c)

~~~json
{
  "source": "007acb5c",
  "target": "Stack[-0x1a1]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acb60`](#insn-007acb60)

~~~json
{
  "source": "007acb60",
  "target": "Stack[-0x16f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acb68`](#insn-007acb68)

~~~json
{
  "source": "007acb68",
  "target": "002c034e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c034e",
  "offset": 0,
  "size": 23,
  "datatype": "string",
  "bytes": "496e76697465667269656e64735f6d6573736167653200",
  "capture_start": "002c034e",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007acb74`](#insn-007acb74)

~~~json
{
  "source": "007acb74",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acb78`](#insn-007acb78)

~~~json
{
  "source": "007acb78",
  "target": "002c035c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c034e",
  "offset": 14,
  "size": 23,
  "datatype": "string",
  "bytes": "496e76697465667269656e64735f6d6573736167653200",
  "capture_start": "002c034e",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007acb7c`](#insn-007acb7c)

~~~json
{
  "source": "007acb7c",
  "target": "Stack[-0x1b7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acb80`](#insn-007acb80)

~~~json
{
  "source": "007acb80",
  "target": "Stack[-0x1a9]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acb94`](#insn-007acb94)

~~~json
{
  "source": "007acb94",
  "target": "0048ce54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acbbc`](#insn-007acbbc)

~~~json
{
  "source": "007acbbc",
  "target": "00748fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acbcc`](#insn-007acbcc)

~~~json
{
  "source": "007acbcc",
  "target": "0045179c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acbd0`](#insn-007acbd0)

~~~json
{
  "source": "007acbd0",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acbd4`](#insn-007acbd4)

~~~json
{
  "source": "007acbd4",
  "target": "007acf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acbd8`](#insn-007acbd8)

~~~json
{
  "source": "007acbd8",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acbdc`](#insn-007acbdc)

~~~json
{
  "source": "007acbdc",
  "target": "007acf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acbe0`](#insn-007acbe0)

~~~json
{
  "source": "007acbe0",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acbe4`](#insn-007acbe4)

~~~json
{
  "source": "007acbe4",
  "target": "007acf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acbe8`](#insn-007acbe8)

~~~json
{
  "source": "007acbe8",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acbec`](#insn-007acbec)

~~~json
{
  "source": "007acbec",
  "target": "007acbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acbf0`](#insn-007acbf0)

~~~json
{
  "source": "007acbf0",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acbf4`](#insn-007acbf4)

~~~json
{
  "source": "007acbf4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acc14`](#insn-007acc14)

~~~json
{
  "source": "007acc14",
  "target": "Stack[-0x16f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc18`](#insn-007acc18)

~~~json
{
  "source": "007acc18",
  "target": "Stack[-0x16b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc1c`](#insn-007acc1c)

~~~json
{
  "source": "007acc1c",
  "target": "Stack[-0x19f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc20`](#insn-007acc20)

~~~json
{
  "source": "007acc20",
  "target": "Stack[-0x19b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc3c`](#insn-007acc3c)

~~~json
{
  "source": "007acc3c",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc40`](#insn-007acc40)

~~~json
{
  "source": "007acc40",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc5c`](#insn-007acc5c)

~~~json
{
  "source": "007acc5c",
  "target": "00748fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acc6c`](#insn-007acc6c)

~~~json
{
  "source": "007acc6c",
  "target": "0045179c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acc70`](#insn-007acc70)

~~~json
{
  "source": "007acc70",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc74`](#insn-007acc74)

~~~json
{
  "source": "007acc74",
  "target": "007acf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc78`](#insn-007acc78)

~~~json
{
  "source": "007acc78",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc7c`](#insn-007acc7c)

~~~json
{
  "source": "007acc7c",
  "target": "007acf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc80`](#insn-007acc80)

~~~json
{
  "source": "007acc80",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc84`](#insn-007acc84)

~~~json
{
  "source": "007acc84",
  "target": "007acc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc88`](#insn-007acc88)

~~~json
{
  "source": "007acc88",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc8c`](#insn-007acc8c)

~~~json
{
  "source": "007acc8c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acc94`](#insn-007acc94)

~~~json
{
  "source": "007acc94",
  "target": "Stack[-0x19f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acc9c`](#insn-007acc9c)

~~~json
{
  "source": "007acc9c",
  "target": "Stack[-0x19b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007accb4`](#insn-007accb4)

~~~json
{
  "source": "007accb4",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007accc0`](#insn-007accc0)

~~~json
{
  "source": "007accc0",
  "target": "Stack[-0x16f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acccc`](#insn-007acccc)

~~~json
{
  "source": "007acccc",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acce4`](#insn-007acce4)

~~~json
{
  "source": "007acce4",
  "target": "00748fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007accf4`](#insn-007accf4)

~~~json
{
  "source": "007accf4",
  "target": "0045179c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007accf8`](#insn-007accf8)

~~~json
{
  "source": "007accf8",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007accfc`](#insn-007accfc)

~~~json
{
  "source": "007accfc",
  "target": "007acf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd00`](#insn-007acd00)

~~~json
{
  "source": "007acd00",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd04`](#insn-007acd04)

~~~json
{
  "source": "007acd04",
  "target": "007acf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd08`](#insn-007acd08)

~~~json
{
  "source": "007acd08",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd0c`](#insn-007acd0c)

~~~json
{
  "source": "007acd0c",
  "target": "007acd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd10`](#insn-007acd10)

~~~json
{
  "source": "007acd10",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd14`](#insn-007acd14)

~~~json
{
  "source": "007acd14",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acd1c`](#insn-007acd1c)

~~~json
{
  "source": "007acd1c",
  "target": "Stack[-0x19f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd20`](#insn-007acd20)

~~~json
{
  "source": "007acd20",
  "target": "Stack[-0x19b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd30`](#insn-007acd30)

~~~json
{
  "source": "007acd30",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd3c`](#insn-007acd3c)

~~~json
{
  "source": "007acd3c",
  "target": "Stack[-0x16f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd48`](#insn-007acd48)

~~~json
{
  "source": "007acd48",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd5c`](#insn-007acd5c)

~~~json
{
  "source": "007acd5c",
  "target": "00748fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acd6c`](#insn-007acd6c)

~~~json
{
  "source": "007acd6c",
  "target": "0045179c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acd70`](#insn-007acd70)

~~~json
{
  "source": "007acd70",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd74`](#insn-007acd74)

~~~json
{
  "source": "007acd74",
  "target": "007acf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd78`](#insn-007acd78)

~~~json
{
  "source": "007acd78",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd7c`](#insn-007acd7c)

~~~json
{
  "source": "007acd7c",
  "target": "007acfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd80`](#insn-007acd80)

~~~json
{
  "source": "007acd80",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd84`](#insn-007acd84)

~~~json
{
  "source": "007acd84",
  "target": "007acd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd88`](#insn-007acd88)

~~~json
{
  "source": "007acd88",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acd8c`](#insn-007acd8c)

~~~json
{
  "source": "007acd8c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acd9c`](#insn-007acd9c)

~~~json
{
  "source": "007acd9c",
  "target": "00c9ac88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acda0`](#insn-007acda0)

~~~json
{
  "source": "007acda0",
  "target": "00c9abb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acda4`](#insn-007acda4)

~~~json
{
  "source": "007acda4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acda8`](#insn-007acda8)

~~~json
{
  "source": "007acda8",
  "target": "00c93208",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93208",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acda8`](#insn-007acda8)

~~~json
{
  "source": "007acda8",
  "target": "00c93210",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93210",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acdb0`](#insn-007acdb0)

~~~json
{
  "source": "007acdb0",
  "target": "00c91038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91038",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acdb0`](#insn-007acdb0)

~~~json
{
  "source": "007acdb0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acdb4`](#insn-007acdb4)

~~~json
{
  "source": "007acdb4",
  "target": "00c91060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acdb4`](#insn-007acdb4)

~~~json
{
  "source": "007acdb4",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acdb8`](#insn-007acdb8)

~~~json
{
  "source": "007acdb8",
  "target": "00c91048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91048",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c91048",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007acdbc`](#insn-007acdbc)

~~~json
{
  "source": "007acdbc",
  "target": "00c91088",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91088",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acdc0`](#insn-007acdc0)

~~~json
{
  "source": "007acdc0",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acdc4`](#insn-007acdc4)

~~~json
{
  "source": "007acdc4",
  "target": "00c91048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91048",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c91048",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007acdd4`](#insn-007acdd4)

~~~json
{
  "source": "007acdd4",
  "target": "00c581e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acde0`](#insn-007acde0)

~~~json
{
  "source": "007acde0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acde4`](#insn-007acde4)

~~~json
{
  "source": "007acde4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acde8`](#insn-007acde8)

~~~json
{
  "source": "007acde8",
  "target": "00c91010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91010",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acde8`](#insn-007acde8)

~~~json
{
  "source": "007acde8",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acdec`](#insn-007acdec)

~~~json
{
  "source": "007acdec",
  "target": "00c91038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91038",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acdec`](#insn-007acdec)

~~~json
{
  "source": "007acdec",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acdf4`](#insn-007acdf4)

~~~json
{
  "source": "007acdf4",
  "target": "00c581f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ace04`](#insn-007ace04)

~~~json
{
  "source": "007ace04",
  "target": "00c9abc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007ace0c`](#insn-007ace0c)

~~~json
{
  "source": "007ace0c",
  "target": "00c90c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90bf8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`007ace0c`](#insn-007ace0c)

~~~json
{
  "source": "007ace0c",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace14`](#insn-007ace14)

~~~json
{
  "source": "007ace14",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace18`](#insn-007ace18)

~~~json
{
  "source": "007ace18",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace1c`](#insn-007ace1c)

~~~json
{
  "source": "007ace1c",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace28`](#insn-007ace28)

~~~json
{
  "source": "007ace28",
  "target": "004519d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ace34`](#insn-007ace34)

~~~json
{
  "source": "007ace34",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace38`](#insn-007ace38)

~~~json
{
  "source": "007ace38",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace48`](#insn-007ace48)

~~~json
{
  "source": "007ace48",
  "target": "Stack[-0x187]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace4c`](#insn-007ace4c)

~~~json
{
  "source": "007ace4c",
  "target": "Stack[-0x184]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace58`](#insn-007ace58)

~~~json
{
  "source": "007ace58",
  "target": "00c581b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ace68`](#insn-007ace68)

~~~json
{
  "source": "007ace68",
  "target": "00b0e934",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ace6c`](#insn-007ace6c)

~~~json
{
  "source": "007ace6c",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace70`](#insn-007ace70)

~~~json
{
  "source": "007ace70",
  "target": "007ace7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace74`](#insn-007ace74)

~~~json
{
  "source": "007ace74",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace78`](#insn-007ace78)

~~~json
{
  "source": "007ace78",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ace7c`](#insn-007ace7c)

~~~json
{
  "source": "007ace7c",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace80`](#insn-007ace80)

~~~json
{
  "source": "007ace80",
  "target": "007ace8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace84`](#insn-007ace84)

~~~json
{
  "source": "007ace84",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace88`](#insn-007ace88)

~~~json
{
  "source": "007ace88",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ace8c`](#insn-007ace8c)

~~~json
{
  "source": "007ace8c",
  "target": "00c93200",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93200",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007ace90`](#insn-007ace90)

~~~json
{
  "source": "007ace90",
  "target": "00c93218",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93218",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007ace98`](#insn-007ace98)

~~~json
{
  "source": "007ace98",
  "target": "00c91010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91010",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007ace98`](#insn-007ace98)

~~~json
{
  "source": "007ace98",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ace9c`](#insn-007ace9c)

~~~json
{
  "source": "007ace9c",
  "target": "00c90ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90ff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c90ff8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007acea0`](#insn-007acea0)

~~~json
{
  "source": "007acea0",
  "target": "00c91038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91038",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acea8`](#insn-007acea8)

~~~json
{
  "source": "007acea8",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aceac`](#insn-007aceac)

~~~json
{
  "source": "007aceac",
  "target": "00c90c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90bf8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`007aceac`](#insn-007aceac)

~~~json
{
  "source": "007aceac",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aceb0`](#insn-007aceb0)

~~~json
{
  "source": "007aceb0",
  "target": "007acebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aceb4`](#insn-007aceb4)

~~~json
{
  "source": "007aceb4",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aceb8`](#insn-007aceb8)

~~~json
{
  "source": "007aceb8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acec0`](#insn-007acec0)

~~~json
{
  "source": "007acec0",
  "target": "00c57fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acec8`](#insn-007acec8)

~~~json
{
  "source": "007acec8",
  "target": "00c93208",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93208",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acecc`](#insn-007acecc)

~~~json
{
  "source": "007acecc",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007aced4`](#insn-007aced4)

~~~json
{
  "source": "007aced4",
  "target": "00c57fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acee0`](#insn-007acee0)

~~~json
{
  "source": "007acee0",
  "target": "00c63ae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63ae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007acee4`](#insn-007acee4)

~~~json
{
  "source": "007acee4",
  "target": "0045bdf8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007aceec`](#insn-007aceec)

~~~json
{
  "source": "007aceec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acef4`](#insn-007acef4)

~~~json
{
  "source": "007acef4",
  "target": "007ad100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acef8`](#insn-007acef8)

~~~json
{
  "source": "007acef8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acefc`](#insn-007acefc)

~~~json
{
  "source": "007acefc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf00`](#insn-007acf00)

~~~json
{
  "source": "007acf00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf04`](#insn-007acf04)

~~~json
{
  "source": "007acf04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf08`](#insn-007acf08)

~~~json
{
  "source": "007acf08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf0c`](#insn-007acf0c)

~~~json
{
  "source": "007acf0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf18`](#insn-007acf18)

~~~json
{
  "source": "007acf18",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf1c`](#insn-007acf1c)

~~~json
{
  "source": "007acf1c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acf20`](#insn-007acf20)

~~~json
{
  "source": "007acf20",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf24`](#insn-007acf24)

~~~json
{
  "source": "007acf24",
  "target": "007acbe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf28`](#insn-007acf28)

~~~json
{
  "source": "007acf28",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf2c`](#insn-007acf2c)

~~~json
{
  "source": "007acf2c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acf30`](#insn-007acf30)

~~~json
{
  "source": "007acf30",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf34`](#insn-007acf34)

~~~json
{
  "source": "007acf34",
  "target": "007acbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf38`](#insn-007acf38)

~~~json
{
  "source": "007acf38",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf3c`](#insn-007acf3c)

~~~json
{
  "source": "007acf3c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acf40`](#insn-007acf40)

~~~json
{
  "source": "007acf40",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf44`](#insn-007acf44)

~~~json
{
  "source": "007acf44",
  "target": "007acbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf48`](#insn-007acf48)

~~~json
{
  "source": "007acf48",
  "target": "007acbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf4c`](#insn-007acf4c)

~~~json
{
  "source": "007acf4c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf50`](#insn-007acf50)

~~~json
{
  "source": "007acf50",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acf54`](#insn-007acf54)

~~~json
{
  "source": "007acf54",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf58`](#insn-007acf58)

~~~json
{
  "source": "007acf58",
  "target": "007acc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf5c`](#insn-007acf5c)

~~~json
{
  "source": "007acf5c",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf60`](#insn-007acf60)

~~~json
{
  "source": "007acf60",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acf64`](#insn-007acf64)

~~~json
{
  "source": "007acf64",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf68`](#insn-007acf68)

~~~json
{
  "source": "007acf68",
  "target": "007acc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf6c`](#insn-007acf6c)

~~~json
{
  "source": "007acf6c",
  "target": "007acc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf70`](#insn-007acf70)

~~~json
{
  "source": "007acf70",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf74`](#insn-007acf74)

~~~json
{
  "source": "007acf74",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acf78`](#insn-007acf78)

~~~json
{
  "source": "007acf78",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf7c`](#insn-007acf7c)

~~~json
{
  "source": "007acf7c",
  "target": "007acd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf80`](#insn-007acf80)

~~~json
{
  "source": "007acf80",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf84`](#insn-007acf84)

~~~json
{
  "source": "007acf84",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acf88`](#insn-007acf88)

~~~json
{
  "source": "007acf88",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf8c`](#insn-007acf8c)

~~~json
{
  "source": "007acf8c",
  "target": "007acd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf90`](#insn-007acf90)

~~~json
{
  "source": "007acf90",
  "target": "007acd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf94`](#insn-007acf94)

~~~json
{
  "source": "007acf94",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acf98`](#insn-007acf98)

~~~json
{
  "source": "007acf98",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acf9c`](#insn-007acf9c)

~~~json
{
  "source": "007acf9c",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acfa0`](#insn-007acfa0)

~~~json
{
  "source": "007acfa0",
  "target": "007acd80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acfa4`](#insn-007acfa4)

~~~json
{
  "source": "007acfa4",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acfa8`](#insn-007acfa8)

~~~json
{
  "source": "007acfa8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007acfac`](#insn-007acfac)

~~~json
{
  "source": "007acfac",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acfb0`](#insn-007acfb0)

~~~json
{
  "source": "007acfb0",
  "target": "007acd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007acfb4`](#insn-007acfb4)

~~~json
{
  "source": "007acfb4",
  "target": "007acd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ad100`](#insn-007ad100)

~~~json
{
  "source": "007ad100",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
