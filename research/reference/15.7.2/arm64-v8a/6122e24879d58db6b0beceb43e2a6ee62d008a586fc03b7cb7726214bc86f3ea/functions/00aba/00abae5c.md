# 00abae5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00abae5c.md)

## 関数情報

~~~json
{
  "address": "00abae5c",
  "name": "FUN_00abae5c",
  "size": 2140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fad2bcbf2f4905600bda7487475b4ac480cef32dba9c513896b9a80b6933cb7d",
  "source_text_sha256": "fad2bcbf2f4905600bda7487475b4ac480cef32dba9c513896b9a80b6933cb7d"
}
~~~
## 呼び出し元

- [00abf464](../00abf/00abf464.md)

## 呼び出し先

- [00464b8c](../00464/00464b8c.md)
- [00464f48](../00464/00464f48.md)
- [00465394](../00465/00465394.md)
- [00465780](../00465/00465780.md)
- [00469f7c](../00469/00469f7c.md)
- [0046ff30](../0046f/0046ff30.md)
- [00a3df28](../00a3d/00a3df28.md)
- [00ab1128](../00ab1/00ab1128.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb050](../00bdb/00bdb050.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb070](../00bdb/00bdb070.md)

## 関連文字列（未確認候補）

~~~text
"%s/v1/notices?platform=%s&clientVersion=%d&clearedStageJapan=%d&clearedStageFuture=%d&clearedStageUniverse=%d&clearedStages=%d&clientTime=%d&timeDifference=%d&countryCode=%s"
"(Ljava/lang/String;I)Landroid/content/SharedPreferences$Editor;"
"(Ljava/lang/String;Ljava/lang/String;)Lcom/google/android/gms/tasks/Task;"
"(Ljava/lang/String;Z)Landroid/content/SharedPreferences$Editor;"
"/v2/transfers/"
"ED_Message_%@.csv"
"OP2_%@.csv"
"OP3_%@.csv"
"OPLegend_%@.csv"
"OP_%@.csv"
"receiptSignature"
~~~
## 疑似コード 1/1 / UTF-8 14455 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00abae5c(long param_1)

{
  long lVar1;
  ulong uVar2;
  long lVar3;
  byte *pbVar4;
  byte local_270 [16];
  void *local_260;
  byte local_258 [16];
  void *local_248;
  byte local_240 [16];
  void *local_230;
  byte local_228 [16];
  void *local_218;
  byte local_210;
  undefined4 local_20f;
  undefined1 local_20b;
  void *local_200;
  byte local_1f8 [16];
  void *local_1e8;
  byte local_1e0;
  undefined7 local_1df;
  char cStack_1d8;
  undefined2 uStack_1d7;
  char cStack_1d5;
  undefined4 uStack_1d4;
  char cStack_1d0;
  undefined2 uStack_1cf;
  undefined5 uStack_1cd;
  byte local_1c8;
  undefined7 uStack_1c7;
  undefined8 uStack_1c0;
  void *local_1b8;
  undefined **local_1b0;
  void *local_1a8;
  void *local_1a0;
  byte local_190;
  void *local_180;
  long local_168;
  undefined *local_160 [8];
  byte local_120;
  void *local_110;
  basic_ios<char,std::__ndk1::char_traits<char>> abStack_f8 [160];
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  FUN_00464f48(&local_1b0);
  local_1b0 = &PTR_FUN_00be7c78;
  FUN_00a3df28(param_1 + 0x449338);
  local_1e0 = 0x22;
  local_20b = 0;
  uStack_1cf = 0x76;
  uStack_1d7 = (undefined2)s_ED_Message____csv_002b03d6._8_8_;
  cStack_1d5 = SUB81(s_ED_Message____csv_002b03d6._8_8_,2);
  uStack_1d4 = SUB84(s_ED_Message____csv_002b03d6._8_8_,3);
  cStack_1d0 = SUB81(s_ED_Message____csv_002b03d6._8_8_,7);
  local_1df = (undefined7)s_ED_Message____csv_002b03d6._0_8_;
  cStack_1d8 = SUB81(s_ED_Message____csv_002b03d6._0_8_,7);
  local_210 = 8;
  local_20f = 0x676e616c;
  FUN_00469f7c(local_1f8,&local_210);
  FUN_0046ff30(&local_1c8,&local_1e0,local_1f8);
                    /* try { // try from 00abaf04 to 00bbaf0f has its CatchHandler @ 00abd330 */
  uVar2 = FUN_00ab1128(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
    operator_delete(local_1b8);
  }
  if ((local_1f8[0] & 1) != 0) {
    operator_delete(local_1e8);
  }
  if ((local_210 & 1) != 0) {
    operator_delete(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    operator_delete((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  if ((uVar2 & 1) != 0) {
    FUN_00465394(&local_1b0,0x2c);
    FUN_00464b8c(&local_1c8,&local_1b0,0);
    if ((BYTE_ARRAY_0032b6a9[param_1 + 7] & 1) != 0) {
                    /* try { // try from 00abafac to 00bbafcf has its CatchHandler @ 00abd474 */
      operator_delete(*(void **)(BYTE_ARRAY_0032b6a9 + param_1 + 0x17));
    }
    *(undefined8 *)(BYTE_ARRAY_0032b6a9 + param_1 + 0xf) = uStack_1c0;
    *(ulong *)(BYTE_ARRAY_0032b6a9 + param_1 + 7) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)(BYTE_ARRAY_0032b6a9 + param_1 + 0x17) = local_1b8;
    FUN_00464b8c(&local_1c8,&local_1b0,1);
    if ((BYTE_ARRAY_0032b6a9[param_1 + 0x1f] & 1) != 0) {
                    /* try { // try from 00abafdc to 00bbb027 has its CatchHandler @ 00abd4bc */
      operator_delete(*(void **)((long)&DWORD_0032b6d8 + param_1));
    }
    *(undefined8 *)((long)&fde_0032b6d0 + param_1) = uStack_1c0;
    *(ulong *)(BYTE_ARRAY_0032b6a9 + param_1 + 0x1f) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&DWORD_0032b6d8 + param_1) = local_1b8;
    FUN_00464b8c(&local_1c8,&local_1b0,2);
    pbVar4 = (byte *)((long)&QWORD_0032b6dc + param_1 + 4);
    if ((*pbVar4 & 1) != 0) {
      operator_delete(*(void **)((long)&QWORD_0032b6f0 + param_1));
    }
    *(undefined8 *)((long)&DWORD_0032b6e8 + param_1) = uStack_1c0;
    *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&QWORD_0032b6f0 + param_1) = local_1b8;
    FUN_00464b8c(&local_1c8,&local_1b0,3);
    if ((*(byte *)((long)&fde_0032b6f8 + param_1) & 1) != 0) {
      operator_delete(*(void **)((long)&QWORD_0032b704 + param_1 + 4));
    }
    *(undefined8 *)((long)&DWORD_0032b700 + param_1) = uStack_1c0;
    *(ulong *)((long)&fde_0032b6f8 + param_1) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&QWORD_0032b704 + param_1 + 4) = local_1b8;
                    /* try { // try from 00abb05c to 00bbb06f has its CatchHandler @ 00abd410 */
    FUN_00465394(&local_1b0,0x2c);
    FUN_00464b8c(&local_1c8,&local_1b0,0);
    if ((*(byte *)((long)&DWORD_0032b710 + param_1) & 1) != 0) {
      operator_delete(*(void **)((long)&fde_0032b720 + param_1));
    }
    *(undefined8 *)((long)&QWORD_0032b718 + param_1) = uStack_1c0;
    *(ulong *)((long)&DWORD_0032b710 + param_1) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&fde_0032b720 + param_1) = local_1b8;
                    /* try { // try from 00abb0a8 to 00bbb0bb has its CatchHandler @ 00abd4e0 */
    FUN_00464b8c(&local_1c8,&local_1b0,1);
    if ((*(byte *)((long)&DWORD_0032b728 + param_1) & 1) != 0) {
      operator_delete(*(void **)((long)&DWORD_0032b738 + param_1));
    }
    *(undefined8 *)((long)&QWORD_0032b72c + param_1 + 4) = uStack_1c0;
    *(ulong *)((long)&DWORD_0032b728 + param_1) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&DWORD_0032b738 + param_1) = local_1b8;
    FUN_00464b8c(&local_1c8,&local_1b0,2);
    if ((*(byte *)((long)&QWORD_0032b740 + param_1) & 1) != 0) {
      operator_delete(*(void **)((long)&DWORD_0032b750 + param_1));
    }
    *(undefined8 *)((long)&fde_0032b748 + param_1) = uStack_1c0;
    *(ulong *)((long)&QWORD_0032b740 + param_1) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&DWORD_0032b750 + param_1) = local_1b8;
    FUN_00464b8c(&local_1c8,&local_1b0,3);
                    /* try { // try from 00abb114 to 00bbb127 has its CatchHandler @ 00abd40c */
    if (((&uleb128_0032b758)[param_1] & 1) != 0) {
      operator_delete(*(void **)(BYTE_ARRAY_0032b759 + param_1 + 0xf));
    }
    *(undefined8 *)(BYTE_ARRAY_0032b759 + param_1 + 7) = uStack_1c0;
    *(ulong *)(&uleb128_0032b758 + param_1) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)(BYTE_ARRAY_0032b759 + param_1 + 0xf) = local_1b8;
  }
  FUN_00465780(&local_1b0);
  local_1e0 = 0x12;
  uStack_1d7 = 0x76;
  local_1df = (undefined7)s_OP____csv_00297354._0_8_;
  cStack_1d8 = SUB81(s_OP____csv_00297354._0_8_,7);
  local_210 = 8;
                    /* try { // try from 00abb168 to 00bbb17b has its CatchHandler @ 00abd408 */
  local_20f = 0x676e616c;
  local_20b = 0;
  FUN_00469f7c(local_228,&local_210);
  FUN_0046ff30(&local_1c8,&local_1e0,local_228);
  uVar2 = FUN_00ab1128(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
                    /* try { // try from 00abb2c8 to 00bbb2db has its CatchHandler @ 00abd3fc */
    operator_delete(local_1b8);
  }
  if ((local_228[0] & 1) != 0) {
    operator_delete(local_218);
  }
  if ((local_210 & 1) != 0) {
    operator_delete(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    operator_delete((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  pbVar4 = (byte *)("receiptSignature" + param_1 + 3);
  if ((uVar2 & 1) != 0) {
    lVar3 = 0x49;
    do {
      FUN_00465394(&local_1b0,0x2c);
                    /* try { // try from 00abb210 to 00bbb223 has its CatchHandler @ 00abd400 */
      FUN_00464b8c(&local_1c8,&local_1b0,0);
      if ((*pbVar4 & 1) != 0) {
        operator_delete(*(void **)(pbVar4 + 0x10));
      }
      lVar3 = lVar3 + -1;
      *(undefined8 *)(pbVar4 + 8) = uStack_1c0;
      *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
      *(void **)(pbVar4 + 0x10) = local_1b8;
      pbVar4 = pbVar4 + 0x18;
    } while (lVar3 != 0);
  }
  FUN_00465780(&local_1b0);
  local_1e0 = 0x1e;
  cStack_1d0 = 0;
  local_1df._0_1_ = s_OPLegend____csv_002ad1ab[0];
  local_1df._1_1_ = s_OPLegend____csv_002ad1ab[1];
  local_1df._2_1_ = s_OPLegend____csv_002ad1ab[2];
  local_1df._3_1_ = s_OPLegend____csv_002ad1ab[3];
  local_1df._4_1_ = s_OPLegend____csv_002ad1ab[4];
  local_1df._5_1_ = s_OPLegend____csv_002ad1ab[5];
  local_1df._6_1_ = s_OPLegend____csv_002ad1ab[6];
                    /* try { // try from 00abb25c to 00bbb26f has its CatchHandler @ 00abd4dc */
  cStack_1d8 = s_OPLegend____csv_002ad1ab[7];
  uStack_1d7 = (undefined2)s_OPLegend____csv_002ad1ab._8_7_;
  cStack_1d5 = SUB71(s_OPLegend____csv_002ad1ab._8_7_,2);
  uStack_1d4 = SUB74(s_OPLegend____csv_002ad1ab._8_7_,3);
  local_210 = 8;
  local_20f = 0x676e616c;
  local_20b = 0;
  FUN_00469f7c(local_240,&local_210);
  FUN_0046ff30(&local_1c8,&local_1e0,local_240);
  uVar2 = FUN_00ab1128(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
    operator_delete(local_1b8);
  }
  if ((local_240[0] & 1) != 0) {
    operator_delete(local_230);
  }
  if ((local_210 & 1) != 0) {
                    /* try { // try from 00abb31c to 00bbb337 has its CatchHandler @ 00abd3f8 */
    operator_delete(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    operator_delete((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  if ((uVar2 & 1) != 0) {
    pbVar4 = (byte *)(
                     "%s/v1/notices?platform=%s&clientVersion=%d&clearedStageJapan=%d&clearedStageFuture=%d&clearedStageUniverse=%d&clearedStages=%d&clientTime=%d&timeDifference=%d&countryCode=%s"
                     + param_1 + 0x7b);
    lVar3 = 0x49;
    do {
      FUN_00465394(&local_1b0,0x2c);
      FUN_00464b8c(&local_1c8,&local_1b0,0);
      if ((*pbVar4 & 1) != 0) {
        operator_delete(*(void **)(pbVar4 + 0x10));
      }
      lVar3 = lVar3 + -1;
      *(undefined8 *)(pbVar4 + 8) = uStack_1c0;
      *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
                    /* try { // try from 00abb354 to 00bbb35b has its CatchHandler @ 00abd4cc */
      *(void **)(pbVar4 + 0x10) = local_1b8;
      pbVar4 = pbVar4 + 0x18;
    } while (lVar3 != 0);
  }
  FUN_00465780(&local_1b0);
  local_1e0 = 0x14;
                    /* try { // try from 00abb3b4 to 00bbb3d3 has its CatchHandler @ 00abd3f0 */
  uStack_1d7 = 0x7673;
  local_1df = (undefined7)s_OP2____csv_0029ed03._0_8_;
  cStack_1d8 = SUB81(s_OP2____csv_0029ed03._0_8_,7);
  cStack_1d5 = 0;
  local_210 = 8;
  local_20f = 0x676e616c;
  local_20b = 0;
  FUN_00469f7c(local_258,&local_210);
                    /* try { // try from 00abb3e0 to 00bbb3eb has its CatchHandler @ 00abd4c8 */
  FUN_0046ff30(&local_1c8,&local_1e0,local_258);
  uVar2 = FUN_00ab1128(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
    operator_delete(local_1b8);
                    /* try { // try from 00abb430 to 00bbb47f has its CatchHandler @ 00abd4bc */
  }
  if ((local_258[0] & 1) != 0) {
    operator_delete(local_248);
  }
  if ((local_210 & 1) != 0) {
    operator_delete(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    operator_delete((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  if ((uVar2 & 1) != 0) {
    pbVar4 = (byte *)("(Ljava/lang/String;Ljava/lang/String;)Lcom/google/android/gms/tasks/Task;" +
                     param_1 + 0x10);
    lVar3 = 0x4d;
    do {
      FUN_00465394(&local_1b0,0x2c);
                    /* try { // try from 00abb4a4 to 00bbb4e7 has its CatchHandler @ 00abd46c */
      FUN_00464b8c(&local_1c8,&local_1b0,0);
      if ((*pbVar4 & 1) != 0) {
        operator_delete(*(void **)(pbVar4 + 0x10));
      }
      lVar3 = lVar3 + -1;
      *(undefined8 *)(pbVar4 + 8) = uStack_1c0;
      *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
      *(void **)(pbVar4 + 0x10) = local_1b8;
      pbVar4 = pbVar4 + 0x18;
    } while (lVar3 != 0);
  }
  FUN_00465780(&local_1b0);
  local_1e0 = 0x14;
  uStack_1d7 = 0x7673;
  local_1df = (undefined7)s_OP3____csv_00292226._0_8_;
  cStack_1d8 = SUB81(s_OP3____csv_00292226._0_8_,7);
  cStack_1d5 = 0;
  local_210 = 8;
  local_20f = 0x676e616c;
  local_20b = 0;
  FUN_00469f7c(local_270,&local_210);
                    /* try { // try from 00abb50c to 00bbb51f has its CatchHandler @ 00abd4bc */
  FUN_0046ff30(&local_1c8,&local_1e0,local_270);
  uVar2 = FUN_00ab1128(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
    operator_delete(local_1b8);
  }
  if ((local_270[0] & 1) != 0) {
    operator_delete(local_260);
  }
  if ((local_210 & 1) != 0) {
    operator_delete(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    operator_delete((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  if ((uVar2 & 1) != 0) {
    lVar3 = 0x4d;
    pbVar4 = (byte *)("(Ljava/lang/String;Z)Landroid/content/SharedPreferences$Editor;" +
                     param_1 + 0x37);
    do {
      FUN_00465394(&local_1b0,0x2c);
      FUN_00464b8c(&local_1c8,&local_1b0,0);
      if ((*pbVar4 & 1) != 0) {
        operator_delete(*(void **)(pbVar4 + 0x10));
      }
      lVar3 = lVar3 + -1;
      *(undefined8 *)(pbVar4 + 8) = uStack_1c0;
      *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
                    /* try { // try from 00abb5b0 to 00bbb5cf has its CatchHandler @ 00abd4bc */
      *(void **)(pbVar4 + 0x10) = local_1b8;
      pbVar4 = pbVar4 + 0x18;
    } while (lVar3 != 0);
  }
  FUN_00465780(&local_1b0);
                    /* try { // try from 00abb604 to 00bbb64f has its CatchHandler @ 00abd518 */
  local_168 = *(long *)PTR_VTT_00c1acc8;
  local_1b0 = (undefined **)(PTR_DAT_00c1acc0 + 0x10);
  *(undefined8 *)
   ((basic_ostream<char,std::__ndk1::char_traits<char>> *)&local_168 + *(long *)(local_168 + -0x18))
       = *(undefined8 *)(PTR_VTT_00c1acc8 + 0x18);
  local_160[0] = PTR_vtable_00c1acd0 + 0x10;
  if ((local_120 & 1) != 0) {
    operator_delete(local_110);
  }
  std::__ndk1::basic_streambuf<char,std::__ndk1::char_traits<char>>::~basic_streambuf
            ((basic_streambuf<char,std::__ndk1::char_traits<char>> *)local_160);
  std::__ndk1::basic_ostream<char,std::__ndk1::char_traits<char>>::~basic_ostream
            ((basic_ostream<char,std::__ndk1::char_traits<char>> *)&local_168);
  std::__ndk1::basic_ios<char,std::__ndk1::char_traits<char>>::~basic_ios(abStack_f8);
  if ((local_190 & 1) != 0) {
    operator_delete(local_180);
  }
  if (local_1a8 != (void *)0x0) {
    local_1a0 = local_1a8;
    operator_delete(local_1a8);
  }
                    /* try { // try from 00abb68c to 00bbb69f has its CatchHandler @ 00abd4bc */
  if (*(long *)(lVar1 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
