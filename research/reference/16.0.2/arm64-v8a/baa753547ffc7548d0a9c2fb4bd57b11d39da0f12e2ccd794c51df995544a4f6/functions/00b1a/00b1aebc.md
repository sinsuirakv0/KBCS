# 00b1aebc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00b1aebc",
  "name": "FUN_00b1aebc",
  "size": 2140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0501b9f357d7a4b140ad513cac6fd16f7ba04452716fee90caf1ec9adc17b15b",
  "source_text_sha256": "0501b9f357d7a4b140ad513cac6fd16f7ba04452716fee90caf1ec9adc17b15b"
}
~~~

## 呼び出し元

- [00b1f4c4](../00b1f/00b1f4c4.md)

## 呼び出し先

- [00487aa4](../00487/00487aa4.md)
- [00487e60](../00487/00487e60.md)
- [004882ac](../00488/004882ac.md)
- [00488698](../00488/00488698.md)
- [0048ce94](../0048c/0048ce94.md)
- [00492e48](../00492/00492e48.md)
- [00a9c0d4](../00a9c/00a9c0d4.md)
- [00b11188](../00b11/00b11188.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58070](../00c58/00c58070.md)
- [00c58080](../00c58/00c58080.md)
- [00c58090](../00c58/00c58090.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/FirebaseApiNotAvailableException"
"Certificate is not yet valid"
"ED_Message_%@.csv"
"GatyaInit[E]_S"
"OP2_%@.csv"
"OP3_%@.csv"
"OPLegend_%@.csv"
"OP_%@.csv"
"Signature on OCSP response was found valid"
"evolveAnimation_ThirdForm.maanim"
"setVisible('clear_na000', %s)"
~~~

## 疑似コード / UTF-8 14663 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00b1aebc(long param_1)

{
  long lVar1;
  undefined *puVar2;
  ulong uVar3;
  byte *pbVar4;
  long lVar5;
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
  undefined1 auStack_f8 [160];
  long local_58;
  
                    /* try { // try from 00b1aed4 to 00c1b073 has its CatchHandler @ 00b22250 */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  FUN_00487e60(&local_1b0);
  local_1b0 = &PTR_FUN_00c64e08;
  FUN_00a9c0d4(param_1 + 0x44e1c8);
  local_1e0 = 0x22;
  local_20b = 0;
  uStack_1cf = 0x76;
  uStack_1d7 = (undefined2)s_ED_Message____csv_002c1a6c._8_8_;
  cStack_1d5 = SUB81(s_ED_Message____csv_002c1a6c._8_8_,2);
  uStack_1d4 = SUB84(s_ED_Message____csv_002c1a6c._8_8_,3);
  cStack_1d0 = SUB81(s_ED_Message____csv_002c1a6c._8_8_,7);
  local_1df = (undefined7)s_ED_Message____csv_002c1a6c._0_8_;
  cStack_1d8 = SUB81(s_ED_Message____csv_002c1a6c._0_8_,7);
  local_210 = 8;
  local_20f = 0x676e616c;
  FUN_0048ce94(local_1f8,&local_210);
  FUN_00492e48(&local_1c8,&local_1e0,local_1f8);
  uVar3 = FUN_00b11188(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
    _ZdlPv(local_1b8);
  }
  if ((local_1f8[0] & 1) != 0) {
    _ZdlPv(local_1e8);
  }
  if ((local_210 & 1) != 0) {
    _ZdlPv(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    _ZdlPv((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  if ((uVar3 & 1) != 0) {
    FUN_004882ac(&local_1b0,0x2c);
    FUN_00487aa4(&local_1c8,&local_1b0,0);
    pbVar4 = (byte *)((long)&fde_table_entry_0032f6d8.initial_loc + param_1);
    if ((*pbVar4 & 1) != 0) {
      _ZdlPv(*(void **)((long)&fde_table_entry_0032f6e8.initial_loc + param_1));
    }
    *(undefined8 *)((long)&fde_table_entry_0032f6e0.initial_loc + param_1) = uStack_1c0;
    *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&fde_table_entry_0032f6e8.initial_loc + param_1) = local_1b8;
    FUN_00487aa4(&local_1c8,&local_1b0,1);
    pbVar4 = (byte *)((long)&fde_table_entry_0032f6f0.initial_loc + param_1);
    if ((*pbVar4 & 1) != 0) {
      _ZdlPv(*(void **)((long)&fde_table_entry_0032f700.initial_loc + param_1));
    }
    *(undefined8 *)((long)&fde_table_entry_0032f6f8.initial_loc + param_1) = uStack_1c0;
    *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&fde_table_entry_0032f700.initial_loc + param_1) = local_1b8;
    FUN_00487aa4(&local_1c8,&local_1b0,2);
    pbVar4 = (byte *)((long)&fde_table_entry_0032f708.initial_loc + param_1);
    if ((*pbVar4 & 1) != 0) {
      _ZdlPv(*(void **)((long)&fde_table_entry_0032f718.initial_loc + param_1));
    }
    *(undefined8 *)((long)&fde_table_entry_0032f710.initial_loc + param_1) = uStack_1c0;
    *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&fde_table_entry_0032f718.initial_loc + param_1) = local_1b8;
                    /* try { // try from 00b1b088 to 00c1b0bb has its CatchHandler @ 00b22348 */
    FUN_00487aa4(&local_1c8,&local_1b0,3);
    pbVar4 = (byte *)((long)&fde_table_entry_0032f720.initial_loc + param_1);
    if ((*pbVar4 & 1) != 0) {
      _ZdlPv(*(void **)((long)&fde_table_entry_0032f730.initial_loc + param_1));
    }
    *(undefined8 *)((long)&fde_table_entry_0032f728.initial_loc + param_1) = uStack_1c0;
    *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&fde_table_entry_0032f730.initial_loc + param_1) = local_1b8;
    FUN_004882ac(&local_1b0,0x2c);
                    /* try { // try from 00b1b0cc to 00c1b15f has its CatchHandler @ 00b223c4 */
    FUN_00487aa4(&local_1c8,&local_1b0,0);
    pbVar4 = (byte *)((long)&fde_table_entry_0032f738.initial_loc + param_1);
    if ((*pbVar4 & 1) != 0) {
      _ZdlPv(*(void **)((long)&fde_table_entry_0032f748.initial_loc + param_1));
    }
    *(undefined8 *)((long)&fde_table_entry_0032f740.initial_loc + param_1) = uStack_1c0;
    *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&fde_table_entry_0032f748.initial_loc + param_1) = local_1b8;
    FUN_00487aa4(&local_1c8,&local_1b0,1);
    pbVar4 = (byte *)((long)&fde_table_entry_0032f750.initial_loc + param_1);
    if ((*pbVar4 & 1) != 0) {
      _ZdlPv(*(void **)((long)&fde_table_entry_0032f760.initial_loc + param_1));
    }
    *(undefined8 *)((long)&fde_table_entry_0032f758.initial_loc + param_1) = uStack_1c0;
    *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&fde_table_entry_0032f760.initial_loc + param_1) = local_1b8;
    FUN_00487aa4(&local_1c8,&local_1b0,2);
    pbVar4 = (byte *)((long)&fde_table_entry_0032f768.initial_loc + param_1);
    if ((*pbVar4 & 1) != 0) {
      _ZdlPv(*(void **)((long)&fde_table_entry_0032f778.initial_loc + param_1));
    }
    *(undefined8 *)((long)&fde_table_entry_0032f770.initial_loc + param_1) = uStack_1c0;
    *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&fde_table_entry_0032f778.initial_loc + param_1) = local_1b8;
    FUN_00487aa4(&local_1c8,&local_1b0,3);
    pbVar4 = (byte *)((long)&fde_table_entry_0032f780.initial_loc + param_1);
                    /* try { // try from 00b1b174 to 00c1b17b has its CatchHandler @ 00b22348 */
    if ((*pbVar4 & 1) != 0) {
      _ZdlPv(*(void **)((long)&fde_table_entry_0032f790.initial_loc + param_1));
    }
    *(undefined8 *)((long)&fde_table_entry_0032f788.initial_loc + param_1) = uStack_1c0;
    *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&fde_table_entry_0032f790.initial_loc + param_1) = local_1b8;
  }
  FUN_00488698(&local_1b0);
                    /* try { // try from 00b1b1a4 to 00c1b1ab has its CatchHandler @ 00b21e00 */
  local_1e0 = 0x12;
  uStack_1d7 = 0x76;
  local_1df = (undefined7)s_OP____csv_002a6f75._0_8_;
  cStack_1d8 = SUB81(s_OP____csv_002a6f75._0_8_,7);
  local_210 = 8;
  local_20f = 0x676e616c;
  local_20b = 0;
  FUN_0048ce94(local_228,&local_210);
  FUN_00492e48(&local_1c8,&local_1e0,local_228);
                    /* try { // try from 00b1b1ec to 00c1b26f has its CatchHandler @ 00b222f8 */
  uVar3 = FUN_00b11188(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
    _ZdlPv(local_1b8);
  }
  if ((local_228[0] & 1) != 0) {
    _ZdlPv(local_218);
                    /* try { // try from 00b1b340 to 00c1b347 has its CatchHandler @ 00b223cc */
  }
  if ((local_210 & 1) != 0) {
    _ZdlPv(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    _ZdlPv((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  pbVar4 = (byte *)("Signature on OCSP response was found valid" + param_1 + 0x24);
  if ((uVar3 & 1) != 0) {
    lVar5 = 0x49;
    do {
      FUN_004882ac(&local_1b0,0x2c);
                    /* try { // try from 00b1b270 to 00c1b303 has its CatchHandler @ 00b1a7a4 */
      FUN_00487aa4(&local_1c8,&local_1b0,0);
      if ((*pbVar4 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar4 + 0x10));
      }
      lVar5 = lVar5 + -1;
      *(undefined8 *)(pbVar4 + 8) = uStack_1c0;
      *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
      *(void **)(pbVar4 + 0x10) = local_1b8;
      pbVar4 = pbVar4 + 0x18;
    } while (lVar5 != 0);
  }
  FUN_00488698(&local_1b0);
  local_1e0 = 0x1e;
  cStack_1d0 = 0;
  local_1df._0_1_ = s_OPLegend____csv_002be3e6[0];
  local_1df._1_1_ = s_OPLegend____csv_002be3e6[1];
  local_1df._2_1_ = s_OPLegend____csv_002be3e6[2];
  local_1df._3_1_ = s_OPLegend____csv_002be3e6[3];
  local_1df._4_1_ = s_OPLegend____csv_002be3e6[4];
  local_1df._5_1_ = s_OPLegend____csv_002be3e6[5];
  local_1df._6_1_ = s_OPLegend____csv_002be3e6[6];
  cStack_1d8 = s_OPLegend____csv_002be3e6[7];
  uStack_1d7 = (undefined2)s_OPLegend____csv_002be3e6._8_7_;
  cStack_1d5 = SUB71(s_OPLegend____csv_002be3e6._8_7_,2);
  uStack_1d4 = SUB74(s_OPLegend____csv_002be3e6._8_7_,3);
  local_210 = 8;
  local_20f = 0x676e616c;
  local_20b = 0;
  FUN_0048ce94(local_240,&local_210);
  FUN_00492e48(&local_1c8,&local_1e0,local_240);
  uVar3 = FUN_00b11188(&local_1b0,&local_1c8,0,0);
                    /* try { // try from 00b1b304 to 00c1b30b has its CatchHandler @ 00b223d4 */
  if ((local_1c8 & 1) != 0) {
    _ZdlPv(local_1b8);
  }
  if ((local_240[0] & 1) != 0) {
    _ZdlPv(local_230);
  }
  if ((local_210 & 1) != 0) {
    _ZdlPv(local_200);
  }
  if ((local_1e0 & 1) != 0) {
                    /* try { // try from 00b1b390 to 00c1b397 has its CatchHandler @ 00b223ac */
    _ZdlPv((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  if ((uVar3 & 1) != 0) {
    pbVar4 = (byte *)("setVisible(\'clear_na000\', %s)" + param_1 + 3);
    lVar5 = 0x49;
    do {
      FUN_004882ac(&local_1b0,0x2c);
                    /* try { // try from 00b1b3cc to 00c1b3d3 has its CatchHandler @ 00b223a4 */
      FUN_00487aa4(&local_1c8,&local_1b0,0);
      if ((*pbVar4 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar4 + 0x10));
      }
      lVar5 = lVar5 + -1;
      *(undefined8 *)(pbVar4 + 8) = uStack_1c0;
      *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
      *(void **)(pbVar4 + 0x10) = local_1b8;
      pbVar4 = pbVar4 + 0x18;
    } while (lVar5 != 0);
  }
  FUN_00488698(&local_1b0);
  local_1e0 = 0x14;
  uStack_1d7 = 0x7673;
                    /* try { // try from 00b1b418 to 00c1b41f has its CatchHandler @ 00b2235c */
  local_1df = (undefined7)s_OP2____csv_002af222._0_8_;
  cStack_1d8 = SUB81(s_OP2____csv_002af222._0_8_,7);
  cStack_1d5 = 0;
  local_210 = 8;
  local_20f = 0x676e616c;
  local_20b = 0;
  FUN_0048ce94(local_258,&local_210);
  FUN_00492e48(&local_1c8,&local_1e0,local_258);
                    /* try { // try from 00b1b454 to 00c1b45b has its CatchHandler @ 00b22354 */
  uVar3 = FUN_00b11188(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
    _ZdlPv(local_1b8);
  }
  if ((local_258[0] & 1) != 0) {
    _ZdlPv(local_248);
  }
  if ((local_210 & 1) != 0) {
    _ZdlPv(local_200);
  }
                    /* try { // try from 00b1b4b4 to 00c1b4bb has its CatchHandler @ 00b223bc */
  if ((local_1e0 & 1) != 0) {
    _ZdlPv((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  if ((uVar3 & 1) != 0) {
    pbVar4 = (byte *)("%PG%com/google/firebase/FirebaseApiNotAvailableException" + param_1 + 0x28);
    lVar5 = 0x4d;
    do {
                    /* try { // try from 00b1b4f0 to 00c1b4f7 has its CatchHandler @ 00b223b4 */
      FUN_004882ac(&local_1b0,0x2c);
      FUN_00487aa4(&local_1c8,&local_1b0,0);
      if ((*pbVar4 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar4 + 0x10));
      }
      lVar5 = lVar5 + -1;
      *(undefined8 *)(pbVar4 + 8) = uStack_1c0;
      *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
      *(void **)(pbVar4 + 0x10) = local_1b8;
      pbVar4 = pbVar4 + 0x18;
    } while (lVar5 != 0);
  }
  FUN_00488698(&local_1b0);
                    /* try { // try from 00b1b530 to 00c1b53b has its CatchHandler @ 00b22224 */
  local_1e0 = 0x14;
  uStack_1d7 = 0x7673;
  local_1df = (undefined7)s_OP3____csv_002a18b7._0_8_;
  cStack_1d8 = SUB81(s_OP3____csv_002a18b7._0_8_,7);
  cStack_1d5 = 0;
  local_210 = 8;
  local_20f = 0x676e616c;
  local_20b = 0;
                    /* try { // try from 00b1b558 to 00c1b563 has its CatchHandler @ 00b22214 */
  FUN_0048ce94(local_270,&local_210);
  FUN_00492e48(&local_1c8,&local_1e0,local_270);
                    /* try { // try from 00b1b574 to 00c1b57f has its CatchHandler @ 00b2221c */
  uVar3 = FUN_00b11188(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
    _ZdlPv(local_1b8);
  }
  if ((local_270[0] & 1) != 0) {
    _ZdlPv(local_260);
                    /* try { // try from 00b1b5cc to 00c1b5d3 has its CatchHandler @ 00b21df8 */
  }
  if ((local_210 & 1) != 0) {
    _ZdlPv(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    _ZdlPv((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  if ((uVar3 & 1) != 0) {
    lVar5 = 0x4d;
    pbVar4 = (byte *)("GatyaInit[E]_S" + param_1 + 5);
                    /* try { // try from 00b1b5fc to 00c1b61f has its CatchHandler @ 00b22330 */
    do {
                    /* try { // try from 00b1b624 to 00c1b637 has its CatchHandler @ 00b21f88 */
      FUN_004882ac(&local_1b0,0x2c);
      FUN_00487aa4(&local_1c8,&local_1b0,0);
      if ((*pbVar4 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar4 + 0x10));
      }
      lVar5 = lVar5 + -1;
      *(undefined8 *)(pbVar4 + 8) = uStack_1c0;
      *(ulong *)pbVar4 = CONCAT71(uStack_1c7,local_1c8);
      *(void **)(pbVar4 + 0x10) = local_1b8;
      pbVar4 = pbVar4 + 0x18;
    } while (lVar5 != 0);
  }
                    /* try { // try from 00b1b64c to 00c1b653 has its CatchHandler @ 00b21df0 */
  FUN_00488698(&local_1b0);
  puVar2 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
  ;
                    /* try { // try from 00b1b664 to 00c1b66b has its CatchHandler @ 00b22298 */
  local_168 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
  ;
  local_1b0 = (undefined **)(PTR_DAT_00c9ac80 + 0x10);
  *(undefined8 *)((long)&local_168 + *(long *)(local_168 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88 +
        0x18);
                    /* try { // try from 00b1b690 to 00c1b6f7 has its CatchHandler @ 00b22328 */
  local_160[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac90
                 + 0x10;
  if ((local_120 & 1) != 0) {
    _ZdlPv(local_110);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_160);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_168,puVar2 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_f8);
  if ((local_190 & 1) != 0) {
    _ZdlPv(local_180);
  }
  if (local_1a8 != (void *)0x0) {
    local_1a0 = local_1a8;
    _ZdlPv(local_1a8);
  }
  if (*(long *)(lVar1 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
