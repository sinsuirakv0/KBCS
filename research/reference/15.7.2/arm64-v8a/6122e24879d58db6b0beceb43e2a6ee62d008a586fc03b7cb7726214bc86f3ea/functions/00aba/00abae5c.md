# 00abae5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00abaf24`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aba/00abaf24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-1c3eb51ec502f5472a4e3d76b4fc1101)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_sha256": "437b47b14bb1120f136519655957df441071c1b1833851809eb7fc4966b1abaf",
  "source_text_sha256": "437b47b14bb1120f136519655957df441071c1b1833851809eb7fc4966b1abaf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abae5c",
        "00abb6b3"
      ],
      [
        "00abb820",
        "00abb823"
      ]
    ],
    "bytes_sha256": "99a08bdd346702dbb88d9320835b8571c26540226a9b33b2249c9e2cf59f4758",
    "instruction_count": 535,
    "instruction_bytes": 2140,
    "body_bytes": 2140,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 13883 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00abae5c(long param_1)

{
  long lVar1;
  undefined *puVar2;
  ulong uVar3;
  long lVar4;
  byte *pbVar5;
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
  uVar3 = FUN_00ab1128(&local_1b0,&local_1c8,0,0);
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
    FUN_00465394(&local_1b0,0x2c);
    FUN_00464b8c(&local_1c8,&local_1b0,0);
    if ((BYTE_ARRAY_0032b6a9[param_1 + 7] & 1) != 0) {
                    /* try { // try from 00abafac to 00bbafcf has its CatchHandler @ 00abd474 */
      _ZdlPv(*(void **)(BYTE_ARRAY_0032b6a9 + param_1 + 0x17));
    }
    *(undefined8 *)(BYTE_ARRAY_0032b6a9 + param_1 + 0xf) = uStack_1c0;
    *(ulong *)(BYTE_ARRAY_0032b6a9 + param_1 + 7) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)(BYTE_ARRAY_0032b6a9 + param_1 + 0x17) = local_1b8;
    FUN_00464b8c(&local_1c8,&local_1b0,1);
    if ((BYTE_ARRAY_0032b6a9[param_1 + 0x1f] & 1) != 0) {
                    /* try { // try from 00abafdc to 00bbb027 has its CatchHandler @ 00abd4bc */
      _ZdlPv(*(void **)((long)&DWORD_0032b6d8 + param_1));
    }
    *(undefined8 *)((long)&fde_0032b6d0 + param_1) = uStack_1c0;
    *(ulong *)(BYTE_ARRAY_0032b6a9 + param_1 + 0x1f) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&DWORD_0032b6d8 + param_1) = local_1b8;
    FUN_00464b8c(&local_1c8,&local_1b0,2);
    pbVar5 = (byte *)((long)&QWORD_0032b6dc + param_1 + 4);
    if ((*pbVar5 & 1) != 0) {
      _ZdlPv(*(void **)((long)&QWORD_0032b6f0 + param_1));
    }
    *(undefined8 *)((long)&DWORD_0032b6e8 + param_1) = uStack_1c0;
    *(ulong *)pbVar5 = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&QWORD_0032b6f0 + param_1) = local_1b8;
    FUN_00464b8c(&local_1c8,&local_1b0,3);
    if ((*(byte *)((long)&fde_0032b6f8 + param_1) & 1) != 0) {
      _ZdlPv(*(void **)((long)&QWORD_0032b704 + param_1 + 4));
    }
    *(undefined8 *)((long)&DWORD_0032b700 + param_1) = uStack_1c0;
    *(ulong *)((long)&fde_0032b6f8 + param_1) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&QWORD_0032b704 + param_1 + 4) = local_1b8;
                    /* try { // try from 00abb05c to 00bbb06f has its CatchHandler @ 00abd410 */
    FUN_00465394(&local_1b0,0x2c);
    FUN_00464b8c(&local_1c8,&local_1b0,0);
    if ((*(byte *)((long)&DWORD_0032b710 + param_1) & 1) != 0) {
      _ZdlPv(*(void **)((long)&fde_0032b720 + param_1));
    }
    *(undefined8 *)((long)&QWORD_0032b718 + param_1) = uStack_1c0;
    *(ulong *)((long)&DWORD_0032b710 + param_1) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&fde_0032b720 + param_1) = local_1b8;
                    /* try { // try from 00abb0a8 to 00bbb0bb has its CatchHandler @ 00abd4e0 */
    FUN_00464b8c(&local_1c8,&local_1b0,1);
    if ((*(byte *)((long)&DWORD_0032b728 + param_1) & 1) != 0) {
      _ZdlPv(*(void **)((long)&DWORD_0032b738 + param_1));
    }
    *(undefined8 *)((long)&QWORD_0032b72c + param_1 + 4) = uStack_1c0;
    *(ulong *)((long)&DWORD_0032b728 + param_1) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&DWORD_0032b738 + param_1) = local_1b8;
    FUN_00464b8c(&local_1c8,&local_1b0,2);
    if ((*(byte *)((long)&QWORD_0032b740 + param_1) & 1) != 0) {
      _ZdlPv(*(void **)((long)&DWORD_0032b750 + param_1));
    }
    *(undefined8 *)((long)&fde_0032b748 + param_1) = uStack_1c0;
    *(ulong *)((long)&QWORD_0032b740 + param_1) = CONCAT71(uStack_1c7,local_1c8);
    *(void **)((long)&DWORD_0032b750 + param_1) = local_1b8;
    FUN_00464b8c(&local_1c8,&local_1b0,3);
                    /* try { // try from 00abb114 to 00bbb127 has its CatchHandler @ 00abd40c */
    if (((&uleb128_0032b758)[param_1] & 1) != 0) {
      _ZdlPv(*(void **)(BYTE_ARRAY_0032b759 + param_1 + 0xf));
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
  uVar3 = FUN_00ab1128(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
                    /* try { // try from 00abb2c8 to 00bbb2db has its CatchHandler @ 00abd3fc */
    _ZdlPv(local_1b8);
  }
  if ((local_228[0] & 1) != 0) {
    _ZdlPv(local_218);
  }
  if ((local_210 & 1) != 0) {
    _ZdlPv(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    _ZdlPv((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  pbVar5 = (byte *)("receiptSignature" + param_1 + 3);
  if ((uVar3 & 1) != 0) {
    lVar4 = 0x49;
    do {
      FUN_00465394(&local_1b0,0x2c);
                    /* try { // try from 00abb210 to 00bbb223 has its CatchHandler @ 00abd400 */
      FUN_00464b8c(&local_1c8,&local_1b0,0);
      if ((*pbVar5 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar5 + 0x10));
      }
      lVar4 = lVar4 + -1;
      *(undefined8 *)(pbVar5 + 8) = uStack_1c0;
      *(ulong *)pbVar5 = CONCAT71(uStack_1c7,local_1c8);
      *(void **)(pbVar5 + 0x10) = local_1b8;
      pbVar5 = pbVar5 + 0x18;
    } while (lVar4 != 0);
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
  uVar3 = FUN_00ab1128(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
    _ZdlPv(local_1b8);
  }
  if ((local_240[0] & 1) != 0) {
    _ZdlPv(local_230);
  }
  if ((local_210 & 1) != 0) {
                    /* try { // try from 00abb31c to 00bbb337 has its CatchHandler @ 00abd3f8 */
    _ZdlPv(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    _ZdlPv((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  if ((uVar3 & 1) != 0) {
    pbVar5 = (byte *)(
                     "%s/v1/notices?platform=%s&clientVersion=%d&clearedStageJapan=%d&clearedStageFuture=%d&clearedStageUniverse=%d&clearedStages=%d&clientTime=%d&timeDifference=%d&countryCode=%s"
                     + param_1 + 0x7b);
    lVar4 = 0x49;
    do {
      FUN_00465394(&local_1b0,0x2c);
      FUN_00464b8c(&local_1c8,&local_1b0,0);
      if ((*pbVar5 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar5 + 0x10));
      }
      lVar4 = lVar4 + -1;
      *(undefined8 *)(pbVar5 + 8) = uStack_1c0;
      *(ulong *)pbVar5 = CONCAT71(uStack_1c7,local_1c8);
                    /* try { // try from 00abb354 to 00bbb35b has its CatchHandler @ 00abd4cc */
      *(void **)(pbVar5 + 0x10) = local_1b8;
      pbVar5 = pbVar5 + 0x18;
    } while (lVar4 != 0);
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
  uVar3 = FUN_00ab1128(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
    _ZdlPv(local_1b8);
                    /* try { // try from 00abb430 to 00bbb47f has its CatchHandler @ 00abd4bc */
  }
  if ((local_258[0] & 1) != 0) {
    _ZdlPv(local_248);
  }
  if ((local_210 & 1) != 0) {
    _ZdlPv(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    _ZdlPv((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  if ((uVar3 & 1) != 0) {
    pbVar5 = (byte *)("(Ljava/lang/String;Ljava/lang/String;)Lcom/google/android/gms/tasks/Task;" +
                     param_1 + 0x10);
    lVar4 = 0x4d;
    do {
      FUN_00465394(&local_1b0,0x2c);
                    /* try { // try from 00abb4a4 to 00bbb4e7 has its CatchHandler @ 00abd46c */
      FUN_00464b8c(&local_1c8,&local_1b0,0);
      if ((*pbVar5 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar5 + 0x10));
      }
      lVar4 = lVar4 + -1;
      *(undefined8 *)(pbVar5 + 8) = uStack_1c0;
      *(ulong *)pbVar5 = CONCAT71(uStack_1c7,local_1c8);
      *(void **)(pbVar5 + 0x10) = local_1b8;
      pbVar5 = pbVar5 + 0x18;
    } while (lVar4 != 0);
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
  uVar3 = FUN_00ab1128(&local_1b0,&local_1c8,0,0);
  if ((local_1c8 & 1) != 0) {
    _ZdlPv(local_1b8);
  }
  if ((local_270[0] & 1) != 0) {
    _ZdlPv(local_260);
  }
  if ((local_210 & 1) != 0) {
    _ZdlPv(local_200);
  }
  if ((local_1e0 & 1) != 0) {
    _ZdlPv((void *)CONCAT53(uStack_1cd,CONCAT21(uStack_1cf,cStack_1d0)));
  }
  if ((uVar3 & 1) != 0) {
    lVar4 = 0x4d;
    pbVar5 = (byte *)("(Ljava/lang/String;Z)Landroid/content/SharedPreferences$Editor;" +
                     param_1 + 0x37);
    do {
      FUN_00465394(&local_1b0,0x2c);
      FUN_00464b8c(&local_1c8,&local_1b0,0);
      if ((*pbVar5 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar5 + 0x10));
      }
      lVar4 = lVar4 + -1;
      *(undefined8 *)(pbVar5 + 8) = uStack_1c0;
      *(ulong *)pbVar5 = CONCAT71(uStack_1c7,local_1c8);
                    /* try { // try from 00abb5b0 to 00bbb5cf has its CatchHandler @ 00abd4bc */
      *(void **)(pbVar5 + 0x10) = local_1b8;
      pbVar5 = pbVar5 + 0x18;
    } while (lVar4 != 0);
  }
  FUN_00465780(&local_1b0);
  puVar2 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1acc8
  ;
                    /* try { // try from 00abb604 to 00bbb64f has its CatchHandler @ 00abd518 */
  local_168 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1acc8
  ;
  local_1b0 = (undefined **)(PTR_DAT_00c1acc0 + 0x10);
  *(undefined8 *)((long)&local_168 + *(long *)(local_168 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1acc8 +
        0x18);
  local_160[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1acd0
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
                    /* try { // try from 00abb68c to 00bbb69f has its CatchHandler @ 00abd4bc */
  if (*(long *)(lVar1 + 0x28) != local_58) {
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
<a id="insn-00abae5c"></a> `00abae5c` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00abae60"></a> `00abae60` | `fc 67 01 a9` | stp x28,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abae64"></a> `00abae64` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abae68"></a> `00abae68` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abae6c"></a> `00abae6c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abae70"></a> `00abae70` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abae74"></a> `00abae74` | `ff 83 08 d1` | sub sp,sp,#0x220 | `FALL_THROUGH`
<a id="insn-00abae78"></a> `00abae78` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abae7c"></a> `00abae7c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abae80"></a> `00abae80` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abae84"></a> `00abae84` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00abae88"></a> `00abae88` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abae8c"></a> `00abae8c` | `2f a8 e6 97` | bl 0x00464f48 | `UNCONDITIONAL_CALL`
<a id="insn-00abae90"></a> `00abae90` | `68 09 00 b0` | adrp x8,0xbe7000 | `FALL_THROUGH`
<a id="insn-00abae94"></a> `00abae94` | `08 e1 31 91` | add x8,x8,#0xc78 | `FALL_THROUGH`
<a id="insn-00abae98"></a> `00abae98` | `e8 63 00 f9` | str x8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00abae9c"></a> `00abae9c` | `68 26 51 91` | add x8,x19,#0x449, LSL #12 | `FALL_THROUGH`
<a id="insn-00abaea0"></a> `00abaea0` | `00 e1 0c 91` | add x0,x8,#0x338 | `FALL_THROUGH`
<a id="insn-00abaea4"></a> `00abaea4` | `21 0c fe 97` | bl 0x00a3df28 | `UNCONDITIONAL_CALL`
<a id="insn-00abaea8"></a> `00abaea8` | `48 04 80 52` | mov w8,#0x22 | `FALL_THROUGH`
<a id="insn-00abaeac"></a> `00abaeac` | `a9 bf ff d0` | adrp x9,0x2b0000 | `FALL_THROUGH`
<a id="insn-00abaeb0"></a> `00abaeb0` | `29 59 0f 91` | add x9,x9,#0x3d6 | `FALL_THROUGH`
<a id="insn-00abaeb4"></a> `00abaeb4` | `f6 43 02 91` | add x22,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00abaeb8"></a> `00abaeb8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abaebc"></a> `00abaebc` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abaec0"></a> `00abaec0` | `c8 0e 80 52` | mov w8,#0x76 | `FALL_THROUGH`
<a id="insn-00abaec4"></a> `00abaec4` | `97 2d 8c 52` | mov w23,#0x616c | `FALL_THROUGH`
<a id="insn-00abaec8"></a> `00abaec8` | `ff 97 01 39` | strb wzr,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00abaecc"></a> `00abaecc` | `c8 12 01 78` | sturh w8,[x22, #0x11] | `FALL_THROUGH`
<a id="insn-00abaed0"></a> `00abaed0` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00abaed4"></a> `00abaed4` | `d7 ed ac 72` | movk w23,#0x676e, LSL #16 | `FALL_THROUGH`
<a id="insn-00abaed8"></a> `00abaed8` | `c0 12 80 3c` | stur q0,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00abaedc"></a> `00abaedc` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abaee0"></a> `00abaee0` | `f7 13 06 b8` | stur w23,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00abaee4"></a> `00abaee4` | `e8 e3 01 91` | add x8,sp,#0x78 | `FALL_THROUGH`
<a id="insn-00abaee8"></a> `00abaee8` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00abaeec"></a> `00abaeec` | `24 bc e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00abaef0"></a> `00abaef0` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abaef4"></a> `00abaef4` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00abaef8"></a> `00abaef8` | `e1 e3 01 91` | add x1,sp,#0x78 | `FALL_THROUGH`
<a id="insn-00abaefc"></a> `00abaefc` | `0d d4 e6 97` | bl 0x0046ff30 | `UNCONDITIONAL_CALL`
<a id="insn-00abaf00"></a> `00abaf00` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abaf04"></a> `00abaf04` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abaf08"></a> `00abaf08` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00abaf0c"></a> `00abaf0c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00abaf10"></a> `00abaf10` | `86 d8 ff 97` | bl 0x00ab1128 | `UNCONDITIONAL_CALL`
<a id="insn-00abaf14"></a> `00abaf14` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00abaf18"></a> `00abaf18` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abaf1c"></a> `00abaf1c` | `28 01 00 37` | tbnz w8,#0x0,0x00abaf40 | `CONDITIONAL_JUMP`
<a id="insn-00abaf20"></a> `00abaf20` | `e8 e3 41 39` | ldrb w8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00abaf24"></a> `00abaf24` | `68 01 00 37` | tbnz w8,#0x0,0x00abaf50 | `CONDITIONAL_JUMP`
<a id="insn-00abaf28"></a> `00abaf28` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abaf2c"></a> `00abaf2c` | `a8 01 00 37` | tbnz w8,#0x0,0x00abaf60 | `CONDITIONAL_JUMP`
<a id="insn-00abaf30"></a> `00abaf30` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abaf34"></a> `00abaf34` | `e8 01 00 37` | tbnz w8,#0x0,0x00abaf70 | `CONDITIONAL_JUMP`
<a id="insn-00abaf38"></a> `00abaf38` | `34 02 00 37` | tbnz w20,#0x0,0x00abaf7c | `CONDITIONAL_JUMP`
<a id="insn-00abaf3c"></a> `00abaf3c` | `7f 00 00 14` | b 0x00abb138 | `UNCONDITIONAL_JUMP`
<a id="insn-00abaf40"></a> `00abaf40` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abaf44"></a> `00abaf44` | `07 80 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abaf48"></a> `00abaf48` | `e8 e3 41 39` | ldrb w8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00abaf4c"></a> `00abaf4c` | `e8 fe 07 36` | tbz w8,#0x0,0x00abaf28 | `CONDITIONAL_JUMP`
<a id="insn-00abaf50"></a> `00abaf50` | `e0 47 40 f9` | ldr x0,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00abaf54"></a> `00abaf54` | `03 80 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abaf58"></a> `00abaf58` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abaf5c"></a> `00abaf5c` | `a8 fe 07 36` | tbz w8,#0x0,0x00abaf30 | `CONDITIONAL_JUMP`
<a id="insn-00abaf60"></a> `00abaf60` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abaf64"></a> `00abaf64` | `ff 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abaf68"></a> `00abaf68` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abaf6c"></a> `00abaf6c` | `68 fe 07 36` | tbz w8,#0x0,0x00abaf38 | `CONDITIONAL_JUMP`
<a id="insn-00abaf70"></a> `00abaf70` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abaf74"></a> `00abaf74` | `fb 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abaf78"></a> `00abaf78` | `14 0e 00 36` | tbz w20,#0x0,0x00abb138 | `CONDITIONAL_JUMP`
<a id="insn-00abaf7c"></a> `00abaf7c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abaf80"></a> `00abaf80` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00abaf84"></a> `00abaf84` | `04 a9 e6 97` | bl 0x00465394 | `UNCONDITIONAL_CALL`
<a id="insn-00abaf88"></a> `00abaf88` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abaf8c"></a> `00abaf8c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abaf90"></a> `00abaf90` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00abaf94"></a> `00abaf94` | `fe a6 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abaf98"></a> `00abaf98` | `68 ae 4c 91` | add x8,x19,#0x32b, LSL #12 | `FALL_THROUGH`
<a id="insn-00abaf9c"></a> `00abaf9c` | `14 c1 1a 91` | add x20,x8,#0x6b0 | `FALL_THROUGH`
<a id="insn-00abafa0"></a> `00abafa0` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00abafa4"></a> `00abafa4` | `68 00 00 36` | tbz w8,#0x0,0x00abafb0 | `CONDITIONAL_JUMP`
<a id="insn-00abafa8"></a> `00abafa8` | `80 0a 40 f9` | ldr x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00abafac"></a> `00abafac` | `ed 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abafb0"></a> `00abafb0` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abafb4"></a> `00abafb4` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abafb8"></a> `00abafb8` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00abafbc"></a> `00abafbc` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00abafc0"></a> `00abafc0` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abafc4"></a> `00abafc4` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abafc8"></a> `00abafc8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00abafcc"></a> `00abafcc` | `f0 a6 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abafd0"></a> `00abafd0` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abafd4"></a> `00abafd4` | `08 8f 41 38` | ldrb w8,[x24, #0x18]! | `FALL_THROUGH`
<a id="insn-00abafd8"></a> `00abafd8` | `68 00 00 36` | tbz w8,#0x0,0x00abafe4 | `CONDITIONAL_JUMP`
<a id="insn-00abafdc"></a> `00abafdc` | `80 16 40 f9` | ldr x0,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00abafe0"></a> `00abafe0` | `e0 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abafe4"></a> `00abafe4` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abafe8"></a> `00abafe8` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abafec"></a> `00abafec` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00abaff0"></a> `00abaff0` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00abaff4"></a> `00abaff4` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abaff8"></a> `00abaff8` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abaffc"></a> `00abaffc` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00abb000"></a> `00abb000` | `e3 a6 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abb004"></a> `00abb004` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abb008"></a> `00abb008` | `08 0f 43 38` | ldrb w8,[x24, #0x30]! | `FALL_THROUGH`
<a id="insn-00abb00c"></a> `00abb00c` | `68 00 00 36` | tbz w8,#0x0,0x00abb018 | `CONDITIONAL_JUMP`
<a id="insn-00abb010"></a> `00abb010` | `80 22 40 f9` | ldr x0,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00abb014"></a> `00abb014` | `d3 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb018"></a> `00abb018` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abb01c"></a> `00abb01c` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb020"></a> `00abb020` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00abb024"></a> `00abb024` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00abb028"></a> `00abb028` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb02c"></a> `00abb02c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb030"></a> `00abb030` | `61 00 80 52` | mov w1,#0x3 | `FALL_THROUGH`
<a id="insn-00abb034"></a> `00abb034` | `d6 a6 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abb038"></a> `00abb038` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abb03c"></a> `00abb03c` | `08 8f 44 38` | ldrb w8,[x24, #0x48]! | `FALL_THROUGH`
<a id="insn-00abb040"></a> `00abb040` | `68 00 00 36` | tbz w8,#0x0,0x00abb04c | `CONDITIONAL_JUMP`
<a id="insn-00abb044"></a> `00abb044` | `80 2e 40 f9` | ldr x0,[x20, #0x58] | `FALL_THROUGH`
<a id="insn-00abb048"></a> `00abb048` | `c6 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb04c"></a> `00abb04c` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abb050"></a> `00abb050` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb054"></a> `00abb054` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00abb058"></a> `00abb058` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00abb05c"></a> `00abb05c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb060"></a> `00abb060` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00abb064"></a> `00abb064` | `cc a8 e6 97` | bl 0x00465394 | `UNCONDITIONAL_CALL`
<a id="insn-00abb068"></a> `00abb068` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb06c"></a> `00abb06c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb070"></a> `00abb070` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00abb074"></a> `00abb074` | `c6 a6 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abb078"></a> `00abb078` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abb07c"></a> `00abb07c` | `08 0f 46 38` | ldrb w8,[x24, #0x60]! | `FALL_THROUGH`
<a id="insn-00abb080"></a> `00abb080` | `68 00 00 36` | tbz w8,#0x0,0x00abb08c | `CONDITIONAL_JUMP`
<a id="insn-00abb084"></a> `00abb084` | `80 3a 40 f9` | ldr x0,[x20, #0x70] | `FALL_THROUGH`
<a id="insn-00abb088"></a> `00abb088` | `b6 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb08c"></a> `00abb08c` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abb090"></a> `00abb090` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb094"></a> `00abb094` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00abb098"></a> `00abb098` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00abb09c"></a> `00abb09c` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb0a0"></a> `00abb0a0` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb0a4"></a> `00abb0a4` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00abb0a8"></a> `00abb0a8` | `b9 a6 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abb0ac"></a> `00abb0ac` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abb0b0"></a> `00abb0b0` | `08 8f 47 38` | ldrb w8,[x24, #0x78]! | `FALL_THROUGH`
<a id="insn-00abb0b4"></a> `00abb0b4` | `68 00 00 36` | tbz w8,#0x0,0x00abb0c0 | `CONDITIONAL_JUMP`
<a id="insn-00abb0b8"></a> `00abb0b8` | `80 46 40 f9` | ldr x0,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00abb0bc"></a> `00abb0bc` | `a9 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb0c0"></a> `00abb0c0` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abb0c4"></a> `00abb0c4` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb0c8"></a> `00abb0c8` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00abb0cc"></a> `00abb0cc` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00abb0d0"></a> `00abb0d0` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb0d4"></a> `00abb0d4` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb0d8"></a> `00abb0d8` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00abb0dc"></a> `00abb0dc` | `ac a6 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abb0e0"></a> `00abb0e0` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abb0e4"></a> `00abb0e4` | `08 0f 49 38` | ldrb w8,[x24, #0x90]! | `FALL_THROUGH`
<a id="insn-00abb0e8"></a> `00abb0e8` | `68 00 00 36` | tbz w8,#0x0,0x00abb0f4 | `CONDITIONAL_JUMP`
<a id="insn-00abb0ec"></a> `00abb0ec` | `80 52 40 f9` | ldr x0,[x20, #0xa0] | `FALL_THROUGH`
<a id="insn-00abb0f0"></a> `00abb0f0` | `9c 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb0f4"></a> `00abb0f4` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abb0f8"></a> `00abb0f8` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb0fc"></a> `00abb0fc` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00abb100"></a> `00abb100` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00abb104"></a> `00abb104` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb108"></a> `00abb108` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb10c"></a> `00abb10c` | `61 00 80 52` | mov w1,#0x3 | `FALL_THROUGH`
<a id="insn-00abb110"></a> `00abb110` | `9f a6 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abb114"></a> `00abb114` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00abb118"></a> `00abb118` | `08 8f 4a 38` | ldrb w8,[x24, #0xa8]! | `FALL_THROUGH`
<a id="insn-00abb11c"></a> `00abb11c` | `68 00 00 36` | tbz w8,#0x0,0x00abb128 | `CONDITIONAL_JUMP`
<a id="insn-00abb120"></a> `00abb120` | `80 5e 40 f9` | ldr x0,[x20, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb124"></a> `00abb124` | `8f 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb128"></a> `00abb128` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abb12c"></a> `00abb12c` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb130"></a> `00abb130` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00abb134"></a> `00abb134` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00abb138"></a> `00abb138` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb13c"></a> `00abb13c` | `91 a9 e6 97` | bl 0x00465780 | `UNCONDITIONAL_CALL`
<a id="insn-00abb140"></a> `00abb140` | `e9 be ff 90` | adrp x9,0x297000 | `FALL_THROUGH`
<a id="insn-00abb144"></a> `00abb144` | `29 51 0d 91` | add x9,x9,#0x354 | `FALL_THROUGH`
<a id="insn-00abb148"></a> `00abb148` | `48 02 80 52` | mov w8,#0x12 | `FALL_THROUGH`
<a id="insn-00abb14c"></a> `00abb14c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00abb150"></a> `00abb150` | `ca 0e 80 52` | mov w10,#0x76 | `FALL_THROUGH`
<a id="insn-00abb154"></a> `00abb154` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb158"></a> `00abb158` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00abb15c"></a> `00abb15c` | `ca 92 00 78` | sturh w10,[x22, #0x9] | `FALL_THROUGH`
<a id="insn-00abb160"></a> `00abb160` | `c9 12 00 f8` | stur x9,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00abb164"></a> `00abb164` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb168"></a> `00abb168` | `f7 13 06 b8` | stur w23,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00abb16c"></a> `00abb16c` | `ff 97 01 39` | strb wzr,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00abb170"></a> `00abb170` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00abb174"></a> `00abb174` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00abb178"></a> `00abb178` | `81 bb e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00abb17c"></a> `00abb17c` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb180"></a> `00abb180` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00abb184"></a> `00abb184` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00abb188"></a> `00abb188` | `6a d3 e6 97` | bl 0x0046ff30 | `UNCONDITIONAL_CALL`
<a id="insn-00abb18c"></a> `00abb18c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb190"></a> `00abb190` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb194"></a> `00abb194` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00abb198"></a> `00abb198` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00abb19c"></a> `00abb19c` | `e3 d7 ff 97` | bl 0x00ab1128 | `UNCONDITIONAL_CALL`
<a id="insn-00abb1a0"></a> `00abb1a0` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00abb1a4"></a> `00abb1a4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abb1a8"></a> `00abb1a8` | `08 09 00 37` | tbnz w8,#0x0,0x00abb2c8 | `CONDITIONAL_JUMP`
<a id="insn-00abb1ac"></a> `00abb1ac` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abb1b0"></a> `00abb1b0` | `48 09 00 37` | tbnz w8,#0x0,0x00abb2d8 | `CONDITIONAL_JUMP`
<a id="insn-00abb1b4"></a> `00abb1b4` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb1b8"></a> `00abb1b8` | `88 09 00 37` | tbnz w8,#0x0,0x00abb2e8 | `CONDITIONAL_JUMP`
<a id="insn-00abb1bc"></a> `00abb1bc` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb1c0"></a> `00abb1c0` | `68 00 00 36` | tbz w8,#0x0,0x00abb1cc | `CONDITIONAL_JUMP`
<a id="insn-00abb1c4"></a> `00abb1c4` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abb1c8"></a> `00abb1c8` | `66 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb1cc"></a> `00abb1cc` | `68 8e 4a 91` | add x8,x19,#0x2a3, LSL #12 | `FALL_THROUGH`
<a id="insn-00abb1d0"></a> `00abb1d0` | `18 01 06 91` | add x24,x8,#0x180 | `FALL_THROUGH`
<a id="insn-00abb1d4"></a> `00abb1d4` | `f4 02 00 36` | tbz w20,#0x0,0x00abb230 | `CONDITIONAL_JUMP`
<a id="insn-00abb1d8"></a> `00abb1d8` | `34 09 80 52` | mov w20,#0x49 | `FALL_THROUGH`
<a id="insn-00abb1dc"></a> `00abb1dc` | `f9 03 18 aa` | mov x25,x24 | `FALL_THROUGH`
<a id="insn-00abb1e0"></a> `00abb1e0` | `08 00 00 14` | b 0x00abb200 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb1e4"></a> `00abb1e4` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abb1e8"></a> `00abb1e8` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb1ec"></a> `00abb1ec` | `94 06 00 f1` | subs x20,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00abb1f0"></a> `00abb1f0` | `20 03 80 3d` | str q0,[x25] | `FALL_THROUGH`
<a id="insn-00abb1f4"></a> `00abb1f4` | `28 0b 00 f9` | str x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00abb1f8"></a> `00abb1f8` | `39 63 00 91` | add x25,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00abb1fc"></a> `00abb1fc` | `a0 01 00 54` | b.eq 0x00abb230 | `CONDITIONAL_JUMP`
<a id="insn-00abb200"></a> `00abb200` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb204"></a> `00abb204` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00abb208"></a> `00abb208` | `63 a8 e6 97` | bl 0x00465394 | `UNCONDITIONAL_CALL`
<a id="insn-00abb20c"></a> `00abb20c` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb210"></a> `00abb210` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb214"></a> `00abb214` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00abb218"></a> `00abb218` | `5d a6 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abb21c"></a> `00abb21c` | `28 03 40 39` | ldrb w8,[x25] | `FALL_THROUGH`
<a id="insn-00abb220"></a> `00abb220` | `28 fe 07 36` | tbz w8,#0x0,0x00abb1e4 | `CONDITIONAL_JUMP`
<a id="insn-00abb224"></a> `00abb224` | `20 0b 40 f9` | ldr x0,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00abb228"></a> `00abb228` | `4e 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb22c"></a> `00abb22c` | `ee ff ff 17` | b 0x00abb1e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb230"></a> `00abb230` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb234"></a> `00abb234` | `53 a9 e6 97` | bl 0x00465780 | `UNCONDITIONAL_CALL`
<a id="insn-00abb238"></a> `00abb238` | `89 bf ff d0` | adrp x9,0x2ad000 | `FALL_THROUGH`
<a id="insn-00abb23c"></a> `00abb23c` | `29 ad 06 91` | add x9,x9,#0x1ab | `FALL_THROUGH`
<a id="insn-00abb240"></a> `00abb240` | `c8 03 80 52` | mov w8,#0x1e | `FALL_THROUGH`
<a id="insn-00abb244"></a> `00abb244` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00abb248"></a> `00abb248` | `29 71 40 f8` | ldur x9,[x9, #0x7] | `FALL_THROUGH`
<a id="insn-00abb24c"></a> `00abb24c` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb250"></a> `00abb250` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00abb254"></a> `00abb254` | `ff 83 02 39` | strb wzr,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abb258"></a> `00abb258` | `ca 12 00 f8` | stur x10,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00abb25c"></a> `00abb25c` | `e9 4f 00 f9` | str x9,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00abb260"></a> `00abb260` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb264"></a> `00abb264` | `f7 13 06 b8` | stur w23,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00abb268"></a> `00abb268` | `ff 97 01 39` | strb wzr,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00abb26c"></a> `00abb26c` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abb270"></a> `00abb270` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00abb274"></a> `00abb274` | `42 bb e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00abb278"></a> `00abb278` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb27c"></a> `00abb27c` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00abb280"></a> `00abb280` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abb284"></a> `00abb284` | `2b d3 e6 97` | bl 0x0046ff30 | `UNCONDITIONAL_CALL`
<a id="insn-00abb288"></a> `00abb288` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb28c"></a> `00abb28c` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb290"></a> `00abb290` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00abb294"></a> `00abb294` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00abb298"></a> `00abb298` | `a4 d7 ff 97` | bl 0x00ab1128 | `UNCONDITIONAL_CALL`
<a id="insn-00abb29c"></a> `00abb29c` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00abb2a0"></a> `00abb2a0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abb2a4"></a> `00abb2a4` | `c8 02 00 37` | tbnz w8,#0x0,0x00abb2fc | `CONDITIONAL_JUMP`
<a id="insn-00abb2a8"></a> `00abb2a8` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abb2ac"></a> `00abb2ac` | `08 03 00 37` | tbnz w8,#0x0,0x00abb30c | `CONDITIONAL_JUMP`
<a id="insn-00abb2b0"></a> `00abb2b0` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb2b4"></a> `00abb2b4` | `48 03 00 37` | tbnz w8,#0x0,0x00abb31c | `CONDITIONAL_JUMP`
<a id="insn-00abb2b8"></a> `00abb2b8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb2bc"></a> `00abb2bc` | `88 03 00 37` | tbnz w8,#0x0,0x00abb32c | `CONDITIONAL_JUMP`
<a id="insn-00abb2c0"></a> `00abb2c0` | `d4 03 00 37` | tbnz w20,#0x0,0x00abb338 | `CONDITIONAL_JUMP`
<a id="insn-00abb2c4"></a> `00abb2c4` | `33 00 00 14` | b 0x00abb390 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb2c8"></a> `00abb2c8` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb2cc"></a> `00abb2cc` | `25 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb2d0"></a> `00abb2d0` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abb2d4"></a> `00abb2d4` | `08 f7 07 36` | tbz w8,#0x0,0x00abb1b4 | `CONDITIONAL_JUMP`
<a id="insn-00abb2d8"></a> `00abb2d8` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00abb2dc"></a> `00abb2dc` | `21 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb2e0"></a> `00abb2e0` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb2e4"></a> `00abb2e4` | `c8 f6 07 36` | tbz w8,#0x0,0x00abb1bc | `CONDITIONAL_JUMP`
<a id="insn-00abb2e8"></a> `00abb2e8` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abb2ec"></a> `00abb2ec` | `1d 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb2f0"></a> `00abb2f0` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb2f4"></a> `00abb2f4` | `88 f6 07 37` | tbnz w8,#0x0,0x00abb1c4 | `CONDITIONAL_JUMP`
<a id="insn-00abb2f8"></a> `00abb2f8` | `b5 ff ff 17` | b 0x00abb1cc | `UNCONDITIONAL_JUMP`
<a id="insn-00abb2fc"></a> `00abb2fc` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb300"></a> `00abb300` | `18 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb304"></a> `00abb304` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abb308"></a> `00abb308` | `48 fd 07 36` | tbz w8,#0x0,0x00abb2b0 | `CONDITIONAL_JUMP`
<a id="insn-00abb30c"></a> `00abb30c` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abb310"></a> `00abb310` | `14 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb314"></a> `00abb314` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb318"></a> `00abb318` | `08 fd 07 36` | tbz w8,#0x0,0x00abb2b8 | `CONDITIONAL_JUMP`
<a id="insn-00abb31c"></a> `00abb31c` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abb320"></a> `00abb320` | `10 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb324"></a> `00abb324` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb328"></a> `00abb328` | `c8 fc 07 36` | tbz w8,#0x0,0x00abb2c0 | `CONDITIONAL_JUMP`
<a id="insn-00abb32c"></a> `00abb32c` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abb330"></a> `00abb330` | `0c 7f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb334"></a> `00abb334` | `f4 02 00 36` | tbz w20,#0x0,0x00abb390 | `CONDITIONAL_JUMP`
<a id="insn-00abb338"></a> `00abb338` | `14 63 1b 91` | add x20,x24,#0x6d8 | `FALL_THROUGH`
<a id="insn-00abb33c"></a> `00abb33c` | `39 09 80 52` | mov w25,#0x49 | `FALL_THROUGH`
<a id="insn-00abb340"></a> `00abb340` | `08 00 00 14` | b 0x00abb360 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb344"></a> `00abb344` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abb348"></a> `00abb348` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb34c"></a> `00abb34c` | `39 07 00 f1` | subs x25,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00abb350"></a> `00abb350` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00abb354"></a> `00abb354` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00abb358"></a> `00abb358` | `94 62 00 91` | add x20,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00abb35c"></a> `00abb35c` | `a0 01 00 54` | b.eq 0x00abb390 | `CONDITIONAL_JUMP`
<a id="insn-00abb360"></a> `00abb360` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb364"></a> `00abb364` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00abb368"></a> `00abb368` | `0b a8 e6 97` | bl 0x00465394 | `UNCONDITIONAL_CALL`
<a id="insn-00abb36c"></a> `00abb36c` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb370"></a> `00abb370` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb374"></a> `00abb374` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00abb378"></a> `00abb378` | `05 a6 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abb37c"></a> `00abb37c` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00abb380"></a> `00abb380` | `28 fe 07 36` | tbz w8,#0x0,0x00abb344 | `CONDITIONAL_JUMP`
<a id="insn-00abb384"></a> `00abb384` | `80 0a 40 f9` | ldr x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00abb388"></a> `00abb388` | `f6 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb38c"></a> `00abb38c` | `ee ff ff 17` | b 0x00abb344 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb390"></a> `00abb390` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb394"></a> `00abb394` | `fb a8 e6 97` | bl 0x00465780 | `UNCONDITIONAL_CALL`
<a id="insn-00abb398"></a> `00abb398` | `09 bf ff f0` | adrp x9,0x29e000 | `FALL_THROUGH`
<a id="insn-00abb39c"></a> `00abb39c` | `29 0d 34 91` | add x9,x9,#0xd03 | `FALL_THROUGH`
<a id="insn-00abb3a0"></a> `00abb3a0` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00abb3a4"></a> `00abb3a4` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00abb3a8"></a> `00abb3a8` | `6a ce 8e 52` | mov w10,#0x7673 | `FALL_THROUGH`
<a id="insn-00abb3ac"></a> `00abb3ac` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb3b0"></a> `00abb3b0` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00abb3b4"></a> `00abb3b4` | `ca 92 00 78` | sturh w10,[x22, #0x9] | `FALL_THROUGH`
<a id="insn-00abb3b8"></a> `00abb3b8` | `c9 12 00 f8` | stur x9,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00abb3bc"></a> `00abb3bc` | `ff 6f 02 39` | strb wzr,[sp, #0x9b] | `FALL_THROUGH`
<a id="insn-00abb3c0"></a> `00abb3c0` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb3c4"></a> `00abb3c4` | `f7 13 06 b8` | stur w23,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00abb3c8"></a> `00abb3c8` | `ff 97 01 39` | strb wzr,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00abb3cc"></a> `00abb3cc` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00abb3d0"></a> `00abb3d0` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00abb3d4"></a> `00abb3d4` | `ea ba e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00abb3d8"></a> `00abb3d8` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb3dc"></a> `00abb3dc` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00abb3e0"></a> `00abb3e0` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00abb3e4"></a> `00abb3e4` | `d3 d2 e6 97` | bl 0x0046ff30 | `UNCONDITIONAL_CALL`
<a id="insn-00abb3e8"></a> `00abb3e8` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb3ec"></a> `00abb3ec` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb3f0"></a> `00abb3f0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00abb3f4"></a> `00abb3f4` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00abb3f8"></a> `00abb3f8` | `4c d7 ff 97` | bl 0x00ab1128 | `UNCONDITIONAL_CALL`
<a id="insn-00abb3fc"></a> `00abb3fc` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00abb400"></a> `00abb400` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abb404"></a> `00abb404` | `28 01 00 37` | tbnz w8,#0x0,0x00abb428 | `CONDITIONAL_JUMP`
<a id="insn-00abb408"></a> `00abb408` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abb40c"></a> `00abb40c` | `68 01 00 37` | tbnz w8,#0x0,0x00abb438 | `CONDITIONAL_JUMP`
<a id="insn-00abb410"></a> `00abb410` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb414"></a> `00abb414` | `a8 01 00 37` | tbnz w8,#0x0,0x00abb448 | `CONDITIONAL_JUMP`
<a id="insn-00abb418"></a> `00abb418` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb41c"></a> `00abb41c` | `e8 01 00 37` | tbnz w8,#0x0,0x00abb458 | `CONDITIONAL_JUMP`
<a id="insn-00abb420"></a> `00abb420` | `34 02 00 37` | tbnz w20,#0x0,0x00abb464 | `CONDITIONAL_JUMP`
<a id="insn-00abb424"></a> `00abb424` | `26 00 00 14` | b 0x00abb4bc | `UNCONDITIONAL_JUMP`
<a id="insn-00abb428"></a> `00abb428` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb42c"></a> `00abb42c` | `cd 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb430"></a> `00abb430` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abb434"></a> `00abb434` | `e8 fe 07 36` | tbz w8,#0x0,0x00abb410 | `CONDITIONAL_JUMP`
<a id="insn-00abb438"></a> `00abb438` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00abb43c"></a> `00abb43c` | `c9 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb440"></a> `00abb440` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb444"></a> `00abb444` | `a8 fe 07 36` | tbz w8,#0x0,0x00abb418 | `CONDITIONAL_JUMP`
<a id="insn-00abb448"></a> `00abb448` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abb44c"></a> `00abb44c` | `c5 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb450"></a> `00abb450` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb454"></a> `00abb454` | `68 fe 07 36` | tbz w8,#0x0,0x00abb420 | `CONDITIONAL_JUMP`
<a id="insn-00abb458"></a> `00abb458` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abb45c"></a> `00abb45c` | `c1 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb460"></a> `00abb460` | `f4 02 00 36` | tbz w20,#0x0,0x00abb4bc | `CONDITIONAL_JUMP`
<a id="insn-00abb464"></a> `00abb464` | `14 c3 36 91` | add x20,x24,#0xdb0 | `FALL_THROUGH`
<a id="insn-00abb468"></a> `00abb468` | `b8 09 80 52` | mov w24,#0x4d | `FALL_THROUGH`
<a id="insn-00abb46c"></a> `00abb46c` | `08 00 00 14` | b 0x00abb48c | `UNCONDITIONAL_JUMP`
<a id="insn-00abb470"></a> `00abb470` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abb474"></a> `00abb474` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb478"></a> `00abb478` | `18 07 00 f1` | subs x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00abb47c"></a> `00abb47c` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00abb480"></a> `00abb480` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00abb484"></a> `00abb484` | `94 62 00 91` | add x20,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00abb488"></a> `00abb488` | `a0 01 00 54` | b.eq 0x00abb4bc | `CONDITIONAL_JUMP`
<a id="insn-00abb48c"></a> `00abb48c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb490"></a> `00abb490` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00abb494"></a> `00abb494` | `c0 a7 e6 97` | bl 0x00465394 | `UNCONDITIONAL_CALL`
<a id="insn-00abb498"></a> `00abb498` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb49c"></a> `00abb49c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb4a0"></a> `00abb4a0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00abb4a4"></a> `00abb4a4` | `ba a5 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abb4a8"></a> `00abb4a8` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00abb4ac"></a> `00abb4ac` | `28 fe 07 36` | tbz w8,#0x0,0x00abb470 | `CONDITIONAL_JUMP`
<a id="insn-00abb4b0"></a> `00abb4b0` | `80 0a 40 f9` | ldr x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00abb4b4"></a> `00abb4b4` | `ab 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb4b8"></a> `00abb4b8` | `ee ff ff 17` | b 0x00abb470 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb4bc"></a> `00abb4bc` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb4c0"></a> `00abb4c0` | `b0 a8 e6 97` | bl 0x00465780 | `UNCONDITIONAL_CALL`
<a id="insn-00abb4c4"></a> `00abb4c4` | `a9 be ff f0` | adrp x9,0x292000 | `FALL_THROUGH`
<a id="insn-00abb4c8"></a> `00abb4c8` | `29 99 08 91` | add x9,x9,#0x226 | `FALL_THROUGH`
<a id="insn-00abb4cc"></a> `00abb4cc` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00abb4d0"></a> `00abb4d0` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00abb4d4"></a> `00abb4d4` | `6a ce 8e 52` | mov w10,#0x7673 | `FALL_THROUGH`
<a id="insn-00abb4d8"></a> `00abb4d8` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb4dc"></a> `00abb4dc` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00abb4e0"></a> `00abb4e0` | `ca 92 00 78` | sturh w10,[x22, #0x9] | `FALL_THROUGH`
<a id="insn-00abb4e4"></a> `00abb4e4` | `c9 12 00 f8` | stur x9,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00abb4e8"></a> `00abb4e8` | `ff 6f 02 39` | strb wzr,[sp, #0x9b] | `FALL_THROUGH`
<a id="insn-00abb4ec"></a> `00abb4ec` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb4f0"></a> `00abb4f0` | `f7 13 06 b8` | stur w23,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00abb4f4"></a> `00abb4f4` | `ff 97 01 39` | strb wzr,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00abb4f8"></a> `00abb4f8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00abb4fc"></a> `00abb4fc` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00abb500"></a> `00abb500` | `9f ba e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00abb504"></a> `00abb504` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb508"></a> `00abb508` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00abb50c"></a> `00abb50c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00abb510"></a> `00abb510` | `88 d2 e6 97` | bl 0x0046ff30 | `UNCONDITIONAL_CALL`
<a id="insn-00abb514"></a> `00abb514` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb518"></a> `00abb518` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb51c"></a> `00abb51c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00abb520"></a> `00abb520` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00abb524"></a> `00abb524` | `01 d7 ff 97` | bl 0x00ab1128 | `UNCONDITIONAL_CALL`
<a id="insn-00abb528"></a> `00abb528` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00abb52c"></a> `00abb52c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abb530"></a> `00abb530` | `28 01 00 37` | tbnz w8,#0x0,0x00abb554 | `CONDITIONAL_JUMP`
<a id="insn-00abb534"></a> `00abb534` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00abb538"></a> `00abb538` | `68 01 00 37` | tbnz w8,#0x0,0x00abb564 | `CONDITIONAL_JUMP`
<a id="insn-00abb53c"></a> `00abb53c` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb540"></a> `00abb540` | `a8 01 00 37` | tbnz w8,#0x0,0x00abb574 | `CONDITIONAL_JUMP`
<a id="insn-00abb544"></a> `00abb544` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb548"></a> `00abb548` | `e8 01 00 37` | tbnz w8,#0x0,0x00abb584 | `CONDITIONAL_JUMP`
<a id="insn-00abb54c"></a> `00abb54c` | `34 02 00 37` | tbnz w20,#0x0,0x00abb590 | `CONDITIONAL_JUMP`
<a id="insn-00abb550"></a> `00abb550` | `27 00 00 14` | b 0x00abb5ec | `UNCONDITIONAL_JUMP`
<a id="insn-00abb554"></a> `00abb554` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb558"></a> `00abb558` | `82 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb55c"></a> `00abb55c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00abb560"></a> `00abb560` | `e8 fe 07 36` | tbz w8,#0x0,0x00abb53c | `CONDITIONAL_JUMP`
<a id="insn-00abb564"></a> `00abb564` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abb568"></a> `00abb568` | `7e 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb56c"></a> `00abb56c` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abb570"></a> `00abb570` | `a8 fe 07 36` | tbz w8,#0x0,0x00abb544 | `CONDITIONAL_JUMP`
<a id="insn-00abb574"></a> `00abb574` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abb578"></a> `00abb578` | `7a 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb57c"></a> `00abb57c` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abb580"></a> `00abb580` | `68 fe 07 36` | tbz w8,#0x0,0x00abb54c | `CONDITIONAL_JUMP`
<a id="insn-00abb584"></a> `00abb584` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abb588"></a> `00abb588` | `76 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb58c"></a> `00abb58c` | `14 03 00 36` | tbz w20,#0x0,0x00abb5ec | `CONDITIONAL_JUMP`
<a id="insn-00abb590"></a> `00abb590` | `68 92 4a 91` | add x8,x19,#0x2a4, LSL #12 | `FALL_THROUGH`
<a id="insn-00abb594"></a> `00abb594` | `b4 09 80 52` | mov w20,#0x4d | `FALL_THROUGH`
<a id="insn-00abb598"></a> `00abb598` | `13 a1 19 91` | add x19,x8,#0x668 | `FALL_THROUGH`
<a id="insn-00abb59c"></a> `00abb59c` | `08 00 00 14` | b 0x00abb5bc | `UNCONDITIONAL_JUMP`
<a id="insn-00abb5a0"></a> `00abb5a0` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abb5a4"></a> `00abb5a4` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00abb5a8"></a> `00abb5a8` | `94 06 00 f1` | subs x20,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00abb5ac"></a> `00abb5ac` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00abb5b0"></a> `00abb5b0` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00abb5b4"></a> `00abb5b4` | `73 62 00 91` | add x19,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00abb5b8"></a> `00abb5b8` | `a0 01 00 54` | b.eq 0x00abb5ec | `CONDITIONAL_JUMP`
<a id="insn-00abb5bc"></a> `00abb5bc` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb5c0"></a> `00abb5c0` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00abb5c4"></a> `00abb5c4` | `74 a7 e6 97` | bl 0x00465394 | `UNCONDITIONAL_CALL`
<a id="insn-00abb5c8"></a> `00abb5c8` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00abb5cc"></a> `00abb5cc` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb5d0"></a> `00abb5d0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00abb5d4"></a> `00abb5d4` | `6e a5 e6 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abb5d8"></a> `00abb5d8` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00abb5dc"></a> `00abb5dc` | `28 fe 07 36` | tbz w8,#0x0,0x00abb5a0 | `CONDITIONAL_JUMP`
<a id="insn-00abb5e0"></a> `00abb5e0` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00abb5e4"></a> `00abb5e4` | `5f 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb5e8"></a> `00abb5e8` | `ee ff ff 17` | b 0x00abb5a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00abb5ec"></a> `00abb5ec` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb5f0"></a> `00abb5f0` | `f4 03 03 91` | add x20,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb5f4"></a> `00abb5f4` | `63 a8 e6 97` | bl 0x00465780 | `UNCONDITIONAL_CALL`
<a id="insn-00abb5f8"></a> `00abb5f8` | `e8 0a 00 f0` | adrp x8,0xc1a000 | `FALL_THROUGH`
<a id="insn-00abb5fc"></a> `00abb5fc` | `f6 0a 00 f0` | adrp x22,0xc1a000 | `FALL_THROUGH`
<a id="insn-00abb600"></a> `00abb600` | `93 22 01 91` | add x19,x20,#0x48 | `FALL_THROUGH`
<a id="insn-00abb604"></a> `00abb604` | `08 61 46 f9` | ldr x8,[x8, #0xcc0] | `FALL_THROUGH`
<a id="insn-00abb608"></a> `00abb608` | `d6 66 46 f9` | ldr x22,[x22, #0xcc8] | `FALL_THROUGH`
<a id="insn-00abb60c"></a> `00abb60c` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-00abb610"></a> `00abb610` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00abb614"></a> `00abb614` | `e8 63 00 f9` | str x8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00abb618"></a> `00abb618` | `e9 87 00 f9` | str x9,[sp, #0x108] | `FALL_THROUGH`
<a id="insn-00abb61c"></a> `00abb61c` | `28 81 5e f8` | ldur x8,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00abb620"></a> `00abb620` | `c9 0e 40 f9` | ldr x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00abb624"></a> `00abb624` | `69 6a 28 f8` | str x9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00abb628"></a> `00abb628` | `e8 0a 00 f0` | adrp x8,0xc1a000 | `FALL_THROUGH`
<a id="insn-00abb62c"></a> `00abb62c` | `08 69 46 f9` | ldr x8,[x8, #0xcd0] | `FALL_THROUGH`
<a id="insn-00abb630"></a> `00abb630` | `e9 43 45 39` | ldrb w9,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00abb634"></a> `00abb634` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00abb638"></a> `00abb638` | `e8 8b 00 f9` | str x8,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00abb63c"></a> `00abb63c` | `69 00 00 36` | tbz w9,#0x0,0x00abb648 | `CONDITIONAL_JUMP`
<a id="insn-00abb640"></a> `00abb640` | `e0 b3 40 f9` | ldr x0,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00abb644"></a> `00abb644` | `47 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb648"></a> `00abb648` | `80 42 01 91` | add x0,x20,#0x50 | `FALL_THROUGH`
<a id="insn-00abb64c"></a> `00abb64c` | `81 7e 04 94` | bl 0x00bdb050 | `UNCONDITIONAL_CALL`
<a id="insn-00abb650"></a> `00abb650` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00abb654"></a> `00abb654` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abb658"></a> `00abb658` | `82 7e 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00abb65c"></a> `00abb65c` | `e8 03 03 91` | add x8,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00abb660"></a> `00abb660` | `00 e1 02 91` | add x0,x8,#0xb8 | `FALL_THROUGH`
<a id="insn-00abb664"></a> `00abb664` | `83 7e 04 94` | bl 0x00bdb070 | `UNCONDITIONAL_CALL`
<a id="insn-00abb668"></a> `00abb668` | `e8 83 43 39` | ldrb w8,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00abb66c"></a> `00abb66c` | `68 00 00 36` | tbz w8,#0x0,0x00abb678 | `CONDITIONAL_JUMP`
<a id="insn-00abb670"></a> `00abb670` | `e0 7b 40 f9` | ldr x0,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00abb674"></a> `00abb674` | `3b 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb678"></a> `00abb678` | `e0 67 40 f9` | ldr x0,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00abb67c"></a> `00abb67c` | `60 00 00 b4` | cbz x0,0x00abb688 | `CONDITIONAL_JUMP`
<a id="insn-00abb680"></a> `00abb680` | `e0 6b 00 f9` | str x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00abb684"></a> `00abb684` | `37 7e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abb688"></a> `00abb688` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00abb68c"></a> `00abb68c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abb690"></a> `00abb690` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abb694"></a> `00abb694` | `61 0c 00 54` | b.ne 0x00abb820 | `CONDITIONAL_JUMP`
<a id="insn-00abb698"></a> `00abb698` | `ff 83 08 91` | add sp,sp,#0x220 | `FALL_THROUGH`
<a id="insn-00abb69c"></a> `00abb69c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abb6a0"></a> `00abb6a0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abb6a4"></a> `00abb6a4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abb6a8"></a> `00abb6a8` | `fc 67 41 a9` | ldp x28,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abb6ac"></a> `00abb6ac` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00abb6b0"></a> `00abb6b0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abb820"></a> `00abb820` | `dc 7d 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abae5c`](#insn-00abae5c) 範囲 `[['00abae5c', '00abaf03']]`
  - `FALL_THROUGH` [`00abaf00`](#insn-00abaf00) → [`00abaf04`](#insn-00abaf04)
- ブロック [`00abaf04`](#insn-00abaf04) 範囲 `[['00abaf04', '00abaf1f']]`
  - `CONDITIONAL_JUMP` [`00abaf1c`](#insn-00abaf1c) → [`00abaf40`](#insn-00abaf40)
  - `FALL_THROUGH` [`00abaf1c`](#insn-00abaf1c) → [`00abaf20`](#insn-00abaf20)
- ブロック [`00abaf20`](#insn-00abaf20) 範囲 `[['00abaf20', '00abaf23']]`
  - `FALL_THROUGH` [`00abaf20`](#insn-00abaf20) → [`00abaf24`](#insn-00abaf24)
- ブロック [`00abaf24`](#insn-00abaf24) 範囲 `[['00abaf24', '00abaf27']]`
  - `CONDITIONAL_JUMP` [`00abaf24`](#insn-00abaf24) → [`00abaf50`](#insn-00abaf50)
  - `FALL_THROUGH` [`00abaf24`](#insn-00abaf24) → [`00abaf28`](#insn-00abaf28)
- ブロック [`00abaf28`](#insn-00abaf28) 範囲 `[['00abaf28', '00abaf2f']]`
  - `CONDITIONAL_JUMP` [`00abaf2c`](#insn-00abaf2c) → [`00abaf60`](#insn-00abaf60)
  - `FALL_THROUGH` [`00abaf2c`](#insn-00abaf2c) → [`00abaf30`](#insn-00abaf30)
- ブロック [`00abaf30`](#insn-00abaf30) 範囲 `[['00abaf30', '00abaf37']]`
  - `CONDITIONAL_JUMP` [`00abaf34`](#insn-00abaf34) → [`00abaf70`](#insn-00abaf70)
  - `FALL_THROUGH` [`00abaf34`](#insn-00abaf34) → [`00abaf38`](#insn-00abaf38)
- ブロック [`00abaf38`](#insn-00abaf38) 範囲 `[['00abaf38', '00abaf3b']]`
  - `CONDITIONAL_JUMP` [`00abaf38`](#insn-00abaf38) → [`00abaf7c`](#insn-00abaf7c)
  - `FALL_THROUGH` [`00abaf38`](#insn-00abaf38) → [`00abaf3c`](#insn-00abaf3c)
- ブロック [`00abaf3c`](#insn-00abaf3c) 範囲 `[['00abaf3c', '00abaf3f']]`
  - `UNCONDITIONAL_JUMP` [`00abaf3c`](#insn-00abaf3c) → [`00abb138`](#insn-00abb138)
- ブロック [`00abaf40`](#insn-00abaf40) 範囲 `[['00abaf40', '00abaf4f']]`
  - `CONDITIONAL_JUMP` [`00abaf4c`](#insn-00abaf4c) → [`00abaf28`](#insn-00abaf28)
  - `FALL_THROUGH` [`00abaf4c`](#insn-00abaf4c) → [`00abaf50`](#insn-00abaf50)
- ブロック [`00abaf50`](#insn-00abaf50) 範囲 `[['00abaf50', '00abaf5f']]`
  - `CONDITIONAL_JUMP` [`00abaf5c`](#insn-00abaf5c) → [`00abaf30`](#insn-00abaf30)
  - `FALL_THROUGH` [`00abaf5c`](#insn-00abaf5c) → [`00abaf60`](#insn-00abaf60)
- ブロック [`00abaf60`](#insn-00abaf60) 範囲 `[['00abaf60', '00abaf6f']]`
  - `CONDITIONAL_JUMP` [`00abaf6c`](#insn-00abaf6c) → [`00abaf38`](#insn-00abaf38)
  - `FALL_THROUGH` [`00abaf6c`](#insn-00abaf6c) → [`00abaf70`](#insn-00abaf70)
- ブロック [`00abaf70`](#insn-00abaf70) 範囲 `[['00abaf70', '00abaf7b']]`
  - `CONDITIONAL_JUMP` [`00abaf78`](#insn-00abaf78) → [`00abb138`](#insn-00abb138)
  - `FALL_THROUGH` [`00abaf78`](#insn-00abaf78) → [`00abaf7c`](#insn-00abaf7c)
- ブロック [`00abaf7c`](#insn-00abaf7c) 範囲 `[['00abaf7c', '00abafa7']]`
  - `CONDITIONAL_JUMP` [`00abafa4`](#insn-00abafa4) → [`00abafb0`](#insn-00abafb0)
  - `FALL_THROUGH` [`00abafa4`](#insn-00abafa4) → [`00abafa8`](#insn-00abafa8)
- ブロック [`00abafa8`](#insn-00abafa8) 範囲 `[['00abafa8', '00abafab']]`
  - `FALL_THROUGH` [`00abafa8`](#insn-00abafa8) → [`00abafac`](#insn-00abafac)
- ブロック [`00abafac`](#insn-00abafac) 範囲 `[['00abafac', '00abafaf']]`
  - `FALL_THROUGH` [`00abafac`](#insn-00abafac) → [`00abafb0`](#insn-00abafb0)
- ブロック [`00abafb0`](#insn-00abafb0) 範囲 `[['00abafb0', '00abafdb']]`
  - `CONDITIONAL_JUMP` [`00abafd8`](#insn-00abafd8) → [`00abafe4`](#insn-00abafe4)
  - `FALL_THROUGH` [`00abafd8`](#insn-00abafd8) → [`00abafdc`](#insn-00abafdc)
- ブロック [`00abafdc`](#insn-00abafdc) 範囲 `[['00abafdc', '00abafe3']]`
  - `FALL_THROUGH` [`00abafe0`](#insn-00abafe0) → [`00abafe4`](#insn-00abafe4)
- ブロック [`00abafe4`](#insn-00abafe4) 範囲 `[['00abafe4', '00abb00f']]`
  - `CONDITIONAL_JUMP` [`00abb00c`](#insn-00abb00c) → [`00abb018`](#insn-00abb018)
  - `FALL_THROUGH` [`00abb00c`](#insn-00abb00c) → [`00abb010`](#insn-00abb010)
- ブロック [`00abb010`](#insn-00abb010) 範囲 `[['00abb010', '00abb017']]`
  - `FALL_THROUGH` [`00abb014`](#insn-00abb014) → [`00abb018`](#insn-00abb018)
- ブロック [`00abb018`](#insn-00abb018) 範囲 `[['00abb018', '00abb043']]`
  - `CONDITIONAL_JUMP` [`00abb040`](#insn-00abb040) → [`00abb04c`](#insn-00abb04c)
  - `FALL_THROUGH` [`00abb040`](#insn-00abb040) → [`00abb044`](#insn-00abb044)
- ブロック [`00abb044`](#insn-00abb044) 範囲 `[['00abb044', '00abb04b']]`
  - `FALL_THROUGH` [`00abb048`](#insn-00abb048) → [`00abb04c`](#insn-00abb04c)
- ブロック [`00abb04c`](#insn-00abb04c) 範囲 `[['00abb04c', '00abb05b']]`
  - `FALL_THROUGH` [`00abb058`](#insn-00abb058) → [`00abb05c`](#insn-00abb05c)
- ブロック [`00abb05c`](#insn-00abb05c) 範囲 `[['00abb05c', '00abb083']]`
  - `CONDITIONAL_JUMP` [`00abb080`](#insn-00abb080) → [`00abb08c`](#insn-00abb08c)
  - `FALL_THROUGH` [`00abb080`](#insn-00abb080) → [`00abb084`](#insn-00abb084)
- ブロック [`00abb084`](#insn-00abb084) 範囲 `[['00abb084', '00abb08b']]`
  - `FALL_THROUGH` [`00abb088`](#insn-00abb088) → [`00abb08c`](#insn-00abb08c)
- ブロック [`00abb08c`](#insn-00abb08c) 範囲 `[['00abb08c', '00abb0a7']]`
  - `FALL_THROUGH` [`00abb0a4`](#insn-00abb0a4) → [`00abb0a8`](#insn-00abb0a8)
- ブロック [`00abb0a8`](#insn-00abb0a8) 範囲 `[['00abb0a8', '00abb0b7']]`
  - `CONDITIONAL_JUMP` [`00abb0b4`](#insn-00abb0b4) → [`00abb0c0`](#insn-00abb0c0)
  - `FALL_THROUGH` [`00abb0b4`](#insn-00abb0b4) → [`00abb0b8`](#insn-00abb0b8)
- ブロック [`00abb0b8`](#insn-00abb0b8) 範囲 `[['00abb0b8', '00abb0bf']]`
  - `FALL_THROUGH` [`00abb0bc`](#insn-00abb0bc) → [`00abb0c0`](#insn-00abb0c0)
- ブロック [`00abb0c0`](#insn-00abb0c0) 範囲 `[['00abb0c0', '00abb0eb']]`
  - `CONDITIONAL_JUMP` [`00abb0e8`](#insn-00abb0e8) → [`00abb0f4`](#insn-00abb0f4)
  - `FALL_THROUGH` [`00abb0e8`](#insn-00abb0e8) → [`00abb0ec`](#insn-00abb0ec)
- ブロック [`00abb0ec`](#insn-00abb0ec) 範囲 `[['00abb0ec', '00abb0f3']]`
  - `FALL_THROUGH` [`00abb0f0`](#insn-00abb0f0) → [`00abb0f4`](#insn-00abb0f4)
- ブロック [`00abb0f4`](#insn-00abb0f4) 範囲 `[['00abb0f4', '00abb113']]`
  - `FALL_THROUGH` [`00abb110`](#insn-00abb110) → [`00abb114`](#insn-00abb114)
- ブロック [`00abb114`](#insn-00abb114) 範囲 `[['00abb114', '00abb11f']]`
  - `CONDITIONAL_JUMP` [`00abb11c`](#insn-00abb11c) → [`00abb128`](#insn-00abb128)
  - `FALL_THROUGH` [`00abb11c`](#insn-00abb11c) → [`00abb120`](#insn-00abb120)
- ブロック [`00abb120`](#insn-00abb120) 範囲 `[['00abb120', '00abb127']]`
  - `FALL_THROUGH` [`00abb124`](#insn-00abb124) → [`00abb128`](#insn-00abb128)
- ブロック [`00abb128`](#insn-00abb128) 範囲 `[['00abb128', '00abb137']]`
  - `FALL_THROUGH` [`00abb134`](#insn-00abb134) → [`00abb138`](#insn-00abb138)
- ブロック [`00abb138`](#insn-00abb138) 範囲 `[['00abb138', '00abb167']]`
  - `FALL_THROUGH` [`00abb164`](#insn-00abb164) → [`00abb168`](#insn-00abb168)
- ブロック [`00abb168`](#insn-00abb168) 範囲 `[['00abb168', '00abb1ab']]`
  - `CONDITIONAL_JUMP` [`00abb1a8`](#insn-00abb1a8) → [`00abb2c8`](#insn-00abb2c8)
  - `FALL_THROUGH` [`00abb1a8`](#insn-00abb1a8) → [`00abb1ac`](#insn-00abb1ac)
- ブロック [`00abb1ac`](#insn-00abb1ac) 範囲 `[['00abb1ac', '00abb1b3']]`
  - `CONDITIONAL_JUMP` [`00abb1b0`](#insn-00abb1b0) → [`00abb2d8`](#insn-00abb2d8)
  - `FALL_THROUGH` [`00abb1b0`](#insn-00abb1b0) → [`00abb1b4`](#insn-00abb1b4)
- ブロック [`00abb1b4`](#insn-00abb1b4) 範囲 `[['00abb1b4', '00abb1bb']]`
  - `CONDITIONAL_JUMP` [`00abb1b8`](#insn-00abb1b8) → [`00abb2e8`](#insn-00abb2e8)
  - `FALL_THROUGH` [`00abb1b8`](#insn-00abb1b8) → [`00abb1bc`](#insn-00abb1bc)
- ブロック [`00abb1bc`](#insn-00abb1bc) 範囲 `[['00abb1bc', '00abb1c3']]`
  - `CONDITIONAL_JUMP` [`00abb1c0`](#insn-00abb1c0) → [`00abb1cc`](#insn-00abb1cc)
  - `FALL_THROUGH` [`00abb1c0`](#insn-00abb1c0) → [`00abb1c4`](#insn-00abb1c4)
- ブロック [`00abb1c4`](#insn-00abb1c4) 範囲 `[['00abb1c4', '00abb1cb']]`
  - `FALL_THROUGH` [`00abb1c8`](#insn-00abb1c8) → [`00abb1cc`](#insn-00abb1cc)
- ブロック [`00abb1cc`](#insn-00abb1cc) 範囲 `[['00abb1cc', '00abb1d7']]`
  - `CONDITIONAL_JUMP` [`00abb1d4`](#insn-00abb1d4) → [`00abb230`](#insn-00abb230)
  - `FALL_THROUGH` [`00abb1d4`](#insn-00abb1d4) → [`00abb1d8`](#insn-00abb1d8)
- ブロック [`00abb1d8`](#insn-00abb1d8) 範囲 `[['00abb1d8', '00abb1e3']]`
  - `UNCONDITIONAL_JUMP` [`00abb1e0`](#insn-00abb1e0) → [`00abb200`](#insn-00abb200)
- ブロック [`00abb1e4`](#insn-00abb1e4) 範囲 `[['00abb1e4', '00abb1ff']]`
  - `CONDITIONAL_JUMP` [`00abb1fc`](#insn-00abb1fc) → [`00abb230`](#insn-00abb230)
  - `FALL_THROUGH` [`00abb1fc`](#insn-00abb1fc) → [`00abb200`](#insn-00abb200)
- ブロック [`00abb200`](#insn-00abb200) 範囲 `[['00abb200', '00abb20f']]`
  - `FALL_THROUGH` [`00abb20c`](#insn-00abb20c) → [`00abb210`](#insn-00abb210)
- ブロック [`00abb210`](#insn-00abb210) 範囲 `[['00abb210', '00abb223']]`
  - `CONDITIONAL_JUMP` [`00abb220`](#insn-00abb220) → [`00abb1e4`](#insn-00abb1e4)
  - `FALL_THROUGH` [`00abb220`](#insn-00abb220) → [`00abb224`](#insn-00abb224)
- ブロック [`00abb224`](#insn-00abb224) 範囲 `[['00abb224', '00abb22f']]`
  - `UNCONDITIONAL_JUMP` [`00abb22c`](#insn-00abb22c) → [`00abb1e4`](#insn-00abb1e4)
- ブロック [`00abb230`](#insn-00abb230) 範囲 `[['00abb230', '00abb25b']]`
  - `FALL_THROUGH` [`00abb258`](#insn-00abb258) → [`00abb25c`](#insn-00abb25c)
- ブロック [`00abb25c`](#insn-00abb25c) 範囲 `[['00abb25c', '00abb2a7']]`
  - `CONDITIONAL_JUMP` [`00abb2a4`](#insn-00abb2a4) → [`00abb2fc`](#insn-00abb2fc)
  - `FALL_THROUGH` [`00abb2a4`](#insn-00abb2a4) → [`00abb2a8`](#insn-00abb2a8)
- ブロック [`00abb2a8`](#insn-00abb2a8) 範囲 `[['00abb2a8', '00abb2af']]`
  - `CONDITIONAL_JUMP` [`00abb2ac`](#insn-00abb2ac) → [`00abb30c`](#insn-00abb30c)
  - `FALL_THROUGH` [`00abb2ac`](#insn-00abb2ac) → [`00abb2b0`](#insn-00abb2b0)
- ブロック [`00abb2b0`](#insn-00abb2b0) 範囲 `[['00abb2b0', '00abb2b7']]`
  - `CONDITIONAL_JUMP` [`00abb2b4`](#insn-00abb2b4) → [`00abb31c`](#insn-00abb31c)
  - `FALL_THROUGH` [`00abb2b4`](#insn-00abb2b4) → [`00abb2b8`](#insn-00abb2b8)
- ブロック [`00abb2b8`](#insn-00abb2b8) 範囲 `[['00abb2b8', '00abb2bf']]`
  - `CONDITIONAL_JUMP` [`00abb2bc`](#insn-00abb2bc) → [`00abb32c`](#insn-00abb32c)
  - `FALL_THROUGH` [`00abb2bc`](#insn-00abb2bc) → [`00abb2c0`](#insn-00abb2c0)
- ブロック [`00abb2c0`](#insn-00abb2c0) 範囲 `[['00abb2c0', '00abb2c3']]`
  - `CONDITIONAL_JUMP` [`00abb2c0`](#insn-00abb2c0) → [`00abb338`](#insn-00abb338)
  - `FALL_THROUGH` [`00abb2c0`](#insn-00abb2c0) → [`00abb2c4`](#insn-00abb2c4)
- ブロック [`00abb2c4`](#insn-00abb2c4) 範囲 `[['00abb2c4', '00abb2c7']]`
  - `UNCONDITIONAL_JUMP` [`00abb2c4`](#insn-00abb2c4) → [`00abb390`](#insn-00abb390)
- ブロック [`00abb2c8`](#insn-00abb2c8) 範囲 `[['00abb2c8', '00abb2d7']]`
  - `CONDITIONAL_JUMP` [`00abb2d4`](#insn-00abb2d4) → [`00abb1b4`](#insn-00abb1b4)
  - `FALL_THROUGH` [`00abb2d4`](#insn-00abb2d4) → [`00abb2d8`](#insn-00abb2d8)
- ブロック [`00abb2d8`](#insn-00abb2d8) 範囲 `[['00abb2d8', '00abb2e7']]`
  - `CONDITIONAL_JUMP` [`00abb2e4`](#insn-00abb2e4) → [`00abb1bc`](#insn-00abb1bc)
  - `FALL_THROUGH` [`00abb2e4`](#insn-00abb2e4) → [`00abb2e8`](#insn-00abb2e8)
- ブロック [`00abb2e8`](#insn-00abb2e8) 範囲 `[['00abb2e8', '00abb2f7']]`
  - `CONDITIONAL_JUMP` [`00abb2f4`](#insn-00abb2f4) → [`00abb1c4`](#insn-00abb1c4)
  - `FALL_THROUGH` [`00abb2f4`](#insn-00abb2f4) → [`00abb2f8`](#insn-00abb2f8)
- ブロック [`00abb2f8`](#insn-00abb2f8) 範囲 `[['00abb2f8', '00abb2fb']]`
  - `UNCONDITIONAL_JUMP` [`00abb2f8`](#insn-00abb2f8) → [`00abb1cc`](#insn-00abb1cc)
- ブロック [`00abb2fc`](#insn-00abb2fc) 範囲 `[['00abb2fc', '00abb30b']]`
  - `CONDITIONAL_JUMP` [`00abb308`](#insn-00abb308) → [`00abb2b0`](#insn-00abb2b0)
  - `FALL_THROUGH` [`00abb308`](#insn-00abb308) → [`00abb30c`](#insn-00abb30c)
- ブロック [`00abb30c`](#insn-00abb30c) 範囲 `[['00abb30c', '00abb31b']]`
  - `CONDITIONAL_JUMP` [`00abb318`](#insn-00abb318) → [`00abb2b8`](#insn-00abb2b8)
  - `FALL_THROUGH` [`00abb318`](#insn-00abb318) → [`00abb31c`](#insn-00abb31c)
- ブロック [`00abb31c`](#insn-00abb31c) 範囲 `[['00abb31c', '00abb32b']]`
  - `CONDITIONAL_JUMP` [`00abb328`](#insn-00abb328) → [`00abb2c0`](#insn-00abb2c0)
  - `FALL_THROUGH` [`00abb328`](#insn-00abb328) → [`00abb32c`](#insn-00abb32c)
- ブロック [`00abb32c`](#insn-00abb32c) 範囲 `[['00abb32c', '00abb337']]`
  - `CONDITIONAL_JUMP` [`00abb334`](#insn-00abb334) → [`00abb390`](#insn-00abb390)
  - `FALL_THROUGH` [`00abb334`](#insn-00abb334) → [`00abb338`](#insn-00abb338)
- ブロック [`00abb338`](#insn-00abb338) 範囲 `[['00abb338', '00abb343']]`
  - `UNCONDITIONAL_JUMP` [`00abb340`](#insn-00abb340) → [`00abb360`](#insn-00abb360)
- ブロック [`00abb344`](#insn-00abb344) 範囲 `[['00abb344', '00abb353']]`
  - `FALL_THROUGH` [`00abb350`](#insn-00abb350) → [`00abb354`](#insn-00abb354)
- ブロック [`00abb354`](#insn-00abb354) 範囲 `[['00abb354', '00abb35f']]`
  - `CONDITIONAL_JUMP` [`00abb35c`](#insn-00abb35c) → [`00abb390`](#insn-00abb390)
  - `FALL_THROUGH` [`00abb35c`](#insn-00abb35c) → [`00abb360`](#insn-00abb360)
- ブロック [`00abb360`](#insn-00abb360) 範囲 `[['00abb360', '00abb383']]`
  - `CONDITIONAL_JUMP` [`00abb380`](#insn-00abb380) → [`00abb344`](#insn-00abb344)
  - `FALL_THROUGH` [`00abb380`](#insn-00abb380) → [`00abb384`](#insn-00abb384)
- ブロック [`00abb384`](#insn-00abb384) 範囲 `[['00abb384', '00abb38f']]`
  - `UNCONDITIONAL_JUMP` [`00abb38c`](#insn-00abb38c) → [`00abb344`](#insn-00abb344)
- ブロック [`00abb390`](#insn-00abb390) 範囲 `[['00abb390', '00abb3b3']]`
  - `FALL_THROUGH` [`00abb3b0`](#insn-00abb3b0) → [`00abb3b4`](#insn-00abb3b4)
- ブロック [`00abb3b4`](#insn-00abb3b4) 範囲 `[['00abb3b4', '00abb3df']]`
  - `FALL_THROUGH` [`00abb3dc`](#insn-00abb3dc) → [`00abb3e0`](#insn-00abb3e0)
- ブロック [`00abb3e0`](#insn-00abb3e0) 範囲 `[['00abb3e0', '00abb407']]`
  - `CONDITIONAL_JUMP` [`00abb404`](#insn-00abb404) → [`00abb428`](#insn-00abb428)
  - `FALL_THROUGH` [`00abb404`](#insn-00abb404) → [`00abb408`](#insn-00abb408)
- ブロック [`00abb408`](#insn-00abb408) 範囲 `[['00abb408', '00abb40f']]`
  - `CONDITIONAL_JUMP` [`00abb40c`](#insn-00abb40c) → [`00abb438`](#insn-00abb438)
  - `FALL_THROUGH` [`00abb40c`](#insn-00abb40c) → [`00abb410`](#insn-00abb410)
- ブロック [`00abb410`](#insn-00abb410) 範囲 `[['00abb410', '00abb417']]`
  - `CONDITIONAL_JUMP` [`00abb414`](#insn-00abb414) → [`00abb448`](#insn-00abb448)
  - `FALL_THROUGH` [`00abb414`](#insn-00abb414) → [`00abb418`](#insn-00abb418)
- ブロック [`00abb418`](#insn-00abb418) 範囲 `[['00abb418', '00abb41f']]`
  - `CONDITIONAL_JUMP` [`00abb41c`](#insn-00abb41c) → [`00abb458`](#insn-00abb458)
  - `FALL_THROUGH` [`00abb41c`](#insn-00abb41c) → [`00abb420`](#insn-00abb420)
- ブロック [`00abb420`](#insn-00abb420) 範囲 `[['00abb420', '00abb423']]`
  - `CONDITIONAL_JUMP` [`00abb420`](#insn-00abb420) → [`00abb464`](#insn-00abb464)
  - `FALL_THROUGH` [`00abb420`](#insn-00abb420) → [`00abb424`](#insn-00abb424)
- ブロック [`00abb424`](#insn-00abb424) 範囲 `[['00abb424', '00abb427']]`
  - `UNCONDITIONAL_JUMP` [`00abb424`](#insn-00abb424) → [`00abb4bc`](#insn-00abb4bc)
- ブロック [`00abb428`](#insn-00abb428) 範囲 `[['00abb428', '00abb42f']]`
  - `FALL_THROUGH` [`00abb42c`](#insn-00abb42c) → [`00abb430`](#insn-00abb430)
- ブロック [`00abb430`](#insn-00abb430) 範囲 `[['00abb430', '00abb437']]`
  - `CONDITIONAL_JUMP` [`00abb434`](#insn-00abb434) → [`00abb410`](#insn-00abb410)
  - `FALL_THROUGH` [`00abb434`](#insn-00abb434) → [`00abb438`](#insn-00abb438)
- ブロック [`00abb438`](#insn-00abb438) 範囲 `[['00abb438', '00abb447']]`
  - `CONDITIONAL_JUMP` [`00abb444`](#insn-00abb444) → [`00abb418`](#insn-00abb418)
  - `FALL_THROUGH` [`00abb444`](#insn-00abb444) → [`00abb448`](#insn-00abb448)
- ブロック [`00abb448`](#insn-00abb448) 範囲 `[['00abb448', '00abb457']]`
  - `CONDITIONAL_JUMP` [`00abb454`](#insn-00abb454) → [`00abb420`](#insn-00abb420)
  - `FALL_THROUGH` [`00abb454`](#insn-00abb454) → [`00abb458`](#insn-00abb458)
- ブロック [`00abb458`](#insn-00abb458) 範囲 `[['00abb458', '00abb463']]`
  - `CONDITIONAL_JUMP` [`00abb460`](#insn-00abb460) → [`00abb4bc`](#insn-00abb4bc)
  - `FALL_THROUGH` [`00abb460`](#insn-00abb460) → [`00abb464`](#insn-00abb464)
- ブロック [`00abb464`](#insn-00abb464) 範囲 `[['00abb464', '00abb46f']]`
  - `UNCONDITIONAL_JUMP` [`00abb46c`](#insn-00abb46c) → [`00abb48c`](#insn-00abb48c)
- ブロック [`00abb470`](#insn-00abb470) 範囲 `[['00abb470', '00abb48b']]`
  - `CONDITIONAL_JUMP` [`00abb488`](#insn-00abb488) → [`00abb4bc`](#insn-00abb4bc)
  - `FALL_THROUGH` [`00abb488`](#insn-00abb488) → [`00abb48c`](#insn-00abb48c)
- ブロック [`00abb48c`](#insn-00abb48c) 範囲 `[['00abb48c', '00abb4a3']]`
  - `FALL_THROUGH` [`00abb4a0`](#insn-00abb4a0) → [`00abb4a4`](#insn-00abb4a4)
- ブロック [`00abb4a4`](#insn-00abb4a4) 範囲 `[['00abb4a4', '00abb4af']]`
  - `CONDITIONAL_JUMP` [`00abb4ac`](#insn-00abb4ac) → [`00abb470`](#insn-00abb470)
  - `FALL_THROUGH` [`00abb4ac`](#insn-00abb4ac) → [`00abb4b0`](#insn-00abb4b0)
- ブロック [`00abb4b0`](#insn-00abb4b0) 範囲 `[['00abb4b0', '00abb4bb']]`
  - `UNCONDITIONAL_JUMP` [`00abb4b8`](#insn-00abb4b8) → [`00abb470`](#insn-00abb470)
- ブロック [`00abb4bc`](#insn-00abb4bc) 範囲 `[['00abb4bc', '00abb50b']]`
  - `FALL_THROUGH` [`00abb508`](#insn-00abb508) → [`00abb50c`](#insn-00abb50c)
- ブロック [`00abb50c`](#insn-00abb50c) 範囲 `[['00abb50c', '00abb533']]`
  - `CONDITIONAL_JUMP` [`00abb530`](#insn-00abb530) → [`00abb554`](#insn-00abb554)
  - `FALL_THROUGH` [`00abb530`](#insn-00abb530) → [`00abb534`](#insn-00abb534)
- ブロック [`00abb534`](#insn-00abb534) 範囲 `[['00abb534', '00abb53b']]`
  - `CONDITIONAL_JUMP` [`00abb538`](#insn-00abb538) → [`00abb564`](#insn-00abb564)
  - `FALL_THROUGH` [`00abb538`](#insn-00abb538) → [`00abb53c`](#insn-00abb53c)
- ブロック [`00abb53c`](#insn-00abb53c) 範囲 `[['00abb53c', '00abb543']]`
  - `CONDITIONAL_JUMP` [`00abb540`](#insn-00abb540) → [`00abb574`](#insn-00abb574)
  - `FALL_THROUGH` [`00abb540`](#insn-00abb540) → [`00abb544`](#insn-00abb544)
- ブロック [`00abb544`](#insn-00abb544) 範囲 `[['00abb544', '00abb54b']]`
  - `CONDITIONAL_JUMP` [`00abb548`](#insn-00abb548) → [`00abb584`](#insn-00abb584)
  - `FALL_THROUGH` [`00abb548`](#insn-00abb548) → [`00abb54c`](#insn-00abb54c)
- ブロック [`00abb54c`](#insn-00abb54c) 範囲 `[['00abb54c', '00abb54f']]`
  - `CONDITIONAL_JUMP` [`00abb54c`](#insn-00abb54c) → [`00abb590`](#insn-00abb590)
  - `FALL_THROUGH` [`00abb54c`](#insn-00abb54c) → [`00abb550`](#insn-00abb550)
- ブロック [`00abb550`](#insn-00abb550) 範囲 `[['00abb550', '00abb553']]`
  - `UNCONDITIONAL_JUMP` [`00abb550`](#insn-00abb550) → [`00abb5ec`](#insn-00abb5ec)
- ブロック [`00abb554`](#insn-00abb554) 範囲 `[['00abb554', '00abb563']]`
  - `CONDITIONAL_JUMP` [`00abb560`](#insn-00abb560) → [`00abb53c`](#insn-00abb53c)
  - `FALL_THROUGH` [`00abb560`](#insn-00abb560) → [`00abb564`](#insn-00abb564)
- ブロック [`00abb564`](#insn-00abb564) 範囲 `[['00abb564', '00abb573']]`
  - `CONDITIONAL_JUMP` [`00abb570`](#insn-00abb570) → [`00abb544`](#insn-00abb544)
  - `FALL_THROUGH` [`00abb570`](#insn-00abb570) → [`00abb574`](#insn-00abb574)
- ブロック [`00abb574`](#insn-00abb574) 範囲 `[['00abb574', '00abb583']]`
  - `CONDITIONAL_JUMP` [`00abb580`](#insn-00abb580) → [`00abb54c`](#insn-00abb54c)
  - `FALL_THROUGH` [`00abb580`](#insn-00abb580) → [`00abb584`](#insn-00abb584)
- ブロック [`00abb584`](#insn-00abb584) 範囲 `[['00abb584', '00abb58f']]`
  - `CONDITIONAL_JUMP` [`00abb58c`](#insn-00abb58c) → [`00abb5ec`](#insn-00abb5ec)
  - `FALL_THROUGH` [`00abb58c`](#insn-00abb58c) → [`00abb590`](#insn-00abb590)
- ブロック [`00abb590`](#insn-00abb590) 範囲 `[['00abb590', '00abb59f']]`
  - `UNCONDITIONAL_JUMP` [`00abb59c`](#insn-00abb59c) → [`00abb5bc`](#insn-00abb5bc)
- ブロック [`00abb5a0`](#insn-00abb5a0) 範囲 `[['00abb5a0', '00abb5af']]`
  - `FALL_THROUGH` [`00abb5ac`](#insn-00abb5ac) → [`00abb5b0`](#insn-00abb5b0)
- ブロック [`00abb5b0`](#insn-00abb5b0) 範囲 `[['00abb5b0', '00abb5bb']]`
  - `CONDITIONAL_JUMP` [`00abb5b8`](#insn-00abb5b8) → [`00abb5ec`](#insn-00abb5ec)
  - `FALL_THROUGH` [`00abb5b8`](#insn-00abb5b8) → [`00abb5bc`](#insn-00abb5bc)
- ブロック [`00abb5bc`](#insn-00abb5bc) 範囲 `[['00abb5bc', '00abb5df']]`
  - `CONDITIONAL_JUMP` [`00abb5dc`](#insn-00abb5dc) → [`00abb5a0`](#insn-00abb5a0)
  - `FALL_THROUGH` [`00abb5dc`](#insn-00abb5dc) → [`00abb5e0`](#insn-00abb5e0)
- ブロック [`00abb5e0`](#insn-00abb5e0) 範囲 `[['00abb5e0', '00abb5eb']]`
  - `UNCONDITIONAL_JUMP` [`00abb5e8`](#insn-00abb5e8) → [`00abb5a0`](#insn-00abb5a0)
- ブロック [`00abb5ec`](#insn-00abb5ec) 範囲 `[['00abb5ec', '00abb603']]`
  - `FALL_THROUGH` [`00abb600`](#insn-00abb600) → [`00abb604`](#insn-00abb604)
- ブロック [`00abb604`](#insn-00abb604) 範囲 `[['00abb604', '00abb63f']]`
  - `CONDITIONAL_JUMP` [`00abb63c`](#insn-00abb63c) → [`00abb648`](#insn-00abb648)
  - `FALL_THROUGH` [`00abb63c`](#insn-00abb63c) → [`00abb640`](#insn-00abb640)
- ブロック [`00abb640`](#insn-00abb640) 範囲 `[['00abb640', '00abb647']]`
  - `FALL_THROUGH` [`00abb644`](#insn-00abb644) → [`00abb648`](#insn-00abb648)
- ブロック [`00abb648`](#insn-00abb648) 範囲 `[['00abb648', '00abb66f']]`
  - `CONDITIONAL_JUMP` [`00abb66c`](#insn-00abb66c) → [`00abb678`](#insn-00abb678)
  - `FALL_THROUGH` [`00abb66c`](#insn-00abb66c) → [`00abb670`](#insn-00abb670)
- ブロック [`00abb670`](#insn-00abb670) 範囲 `[['00abb670', '00abb677']]`
  - `FALL_THROUGH` [`00abb674`](#insn-00abb674) → [`00abb678`](#insn-00abb678)
- ブロック [`00abb678`](#insn-00abb678) 範囲 `[['00abb678', '00abb67f']]`
  - `CONDITIONAL_JUMP` [`00abb67c`](#insn-00abb67c) → [`00abb688`](#insn-00abb688)
  - `FALL_THROUGH` [`00abb67c`](#insn-00abb67c) → [`00abb680`](#insn-00abb680)
- ブロック [`00abb680`](#insn-00abb680) 範囲 `[['00abb680', '00abb687']]`
  - `FALL_THROUGH` [`00abb684`](#insn-00abb684) → [`00abb688`](#insn-00abb688)
- ブロック [`00abb688`](#insn-00abb688) 範囲 `[['00abb688', '00abb68b']]`
  - `FALL_THROUGH` [`00abb688`](#insn-00abb688) → [`00abb68c`](#insn-00abb68c)
- ブロック [`00abb68c`](#insn-00abb68c) 範囲 `[['00abb68c', '00abb697']]`
  - `CONDITIONAL_JUMP` [`00abb694`](#insn-00abb694) → [`00abb820`](#insn-00abb820)
  - `FALL_THROUGH` [`00abb694`](#insn-00abb694) → [`00abb698`](#insn-00abb698)
- ブロック [`00abb698`](#insn-00abb698) 範囲 `[['00abb698', '00abb6b3']]`
- ブロック [`00abb820`](#insn-00abb820) 範囲 `[['00abb820', '00abb823']]`

## 命令位置別の参照

- [`00abae5c`](#insn-00abae5c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae60`](#insn-00abae60) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae64`](#insn-00abae64) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae68`](#insn-00abae68) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae6c`](#insn-00abae6c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae88`](#insn-00abae88) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae8c`](#insn-00abae8c) → [`00464f48`](../00464/00464f48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464f48` · 推定シンボル `None` · 推定型 `None`
- [`00abae98`](#insn-00abae98) → `00be7c78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abae98`](#insn-00abae98) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaea4`](#insn-00abaea4) → [`00a3df28`](../00a3d/00a3df28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a3df28` · 推定シンボル `None` · 推定型 `None`
- [`00abaeb8`](#insn-00abaeb8) → `002b03d6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abaebc`](#insn-00abaebc) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaec8`](#insn-00abaec8) → `Stack[-0x20b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaecc`](#insn-00abaecc) → `Stack[-0x1cf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaed8`](#insn-00abaed8) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaedc`](#insn-00abaedc) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaee0`](#insn-00abaee0) → `Stack[-0x20f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaeec`](#insn-00abaeec) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00abaefc`](#insn-00abaefc) → [`0046ff30`](../0046f/0046ff30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ff30` · 推定シンボル `None` · 推定型 `None`
- [`00abaf10`](#insn-00abaf10) → [`00ab1128`](../00ab1/00ab1128.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab1128` · 推定シンボル `None` · 推定型 `None`
- [`00abaf14`](#insn-00abaf14) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf1c`](#insn-00abaf1c) → [`00abaf40`](#insn-00abaf40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf20`](#insn-00abaf20) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf24`](#insn-00abaf24) → [`00abaf50`](#insn-00abaf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf28`](#insn-00abaf28) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf2c`](#insn-00abaf2c) → [`00abaf60`](#insn-00abaf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf30`](#insn-00abaf30) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf34`](#insn-00abaf34) → [`00abaf70`](#insn-00abaf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf38`](#insn-00abaf38) → [`00abaf7c`](#insn-00abaf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf3c`](#insn-00abaf3c) → [`00abb138`](#insn-00abb138) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf40`](#insn-00abaf40) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf44`](#insn-00abaf44) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abaf48`](#insn-00abaf48) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf4c`](#insn-00abaf4c) → [`00abaf28`](#insn-00abaf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf50`](#insn-00abaf50) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf54`](#insn-00abaf54) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abaf58`](#insn-00abaf58) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf5c`](#insn-00abaf5c) → [`00abaf30`](#insn-00abaf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf60`](#insn-00abaf60) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf64`](#insn-00abaf64) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abaf68`](#insn-00abaf68) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf6c`](#insn-00abaf6c) → [`00abaf38`](#insn-00abaf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf70`](#insn-00abaf70) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf74`](#insn-00abaf74) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abaf78`](#insn-00abaf78) → [`00abb138`](#insn-00abb138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf84`](#insn-00abaf84) → [`00465394`](../00465/00465394.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465394` · 推定シンボル `None` · 推定型 `None`
- [`00abaf94`](#insn-00abaf94) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abafa0`](#insn-00abafa0) → `0032b6b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00abafa4`](#insn-00abafa4) → [`00abafb0`](#insn-00abafb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abafa8`](#insn-00abafa8) → `0032b6c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00abafac`](#insn-00abafac) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abafb0`](#insn-00abafb0) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abafb4`](#insn-00abafb4) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abafb8`](#insn-00abafb8) → `0032b6b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00abafbc`](#insn-00abafbc) → `0032b6c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00abafcc`](#insn-00abafcc) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abafd4`](#insn-00abafd4) → `0032b6c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00abafd8`](#insn-00abafd8) → [`00abafe4`](#insn-00abafe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abafdc`](#insn-00abafdc) → `0032b6d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00abafe0`](#insn-00abafe0) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abafe4`](#insn-00abafe4) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abafe8`](#insn-00abafe8) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abafec`](#insn-00abafec) → `0032b6c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00abaff0`](#insn-00abaff0) → `0032b6d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00abb000`](#insn-00abb000) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abb008`](#insn-00abb008) → `0032b6e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00abb00c`](#insn-00abb00c) → [`00abb018`](#insn-00abb018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb010`](#insn-00abb010) → `0032b6f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00abb014`](#insn-00abb014) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb018`](#insn-00abb018) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb01c`](#insn-00abb01c) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb020`](#insn-00abb020) → `0032b6e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00abb024`](#insn-00abb024) → `0032b6f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00abb034`](#insn-00abb034) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abb03c`](#insn-00abb03c) → `0032b6f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0032b6f8` · 推定型 `dword`
- [`00abb040`](#insn-00abb040) → [`00abb04c`](#insn-00abb04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb044`](#insn-00abb044) → `0032b708`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00abb048`](#insn-00abb048) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb04c`](#insn-00abb04c) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb050`](#insn-00abb050) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb054`](#insn-00abb054) → `0032b6f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0032b6f8` · 推定型 `dword`
- [`00abb058`](#insn-00abb058) → `0032b708`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00abb064`](#insn-00abb064) → [`00465394`](../00465/00465394.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465394` · 推定シンボル `None` · 推定型 `None`
- [`00abb074`](#insn-00abb074) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abb07c`](#insn-00abb07c) → `0032b710`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00abb080`](#insn-00abb080) → [`00abb08c`](#insn-00abb08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb084`](#insn-00abb084) → `0032b720`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0032b720` · 推定型 `dword`
- [`00abb088`](#insn-00abb088) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb08c`](#insn-00abb08c) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb090`](#insn-00abb090) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb094`](#insn-00abb094) → `0032b710`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00abb098`](#insn-00abb098) → `0032b720`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0032b720` · 推定型 `dword`
- [`00abb0a8`](#insn-00abb0a8) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abb0b0`](#insn-00abb0b0) → `0032b728`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00abb0b4`](#insn-00abb0b4) → [`00abb0c0`](#insn-00abb0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0b8`](#insn-00abb0b8) → `0032b738`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00abb0bc`](#insn-00abb0bc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb0c0`](#insn-00abb0c0) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0c4`](#insn-00abb0c4) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0c8`](#insn-00abb0c8) → `0032b728`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00abb0cc`](#insn-00abb0cc) → `0032b738`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00abb0dc`](#insn-00abb0dc) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abb0e4`](#insn-00abb0e4) → `0032b740`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00abb0e8`](#insn-00abb0e8) → [`00abb0f4`](#insn-00abb0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0ec`](#insn-00abb0ec) → `0032b750`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00abb0f0`](#insn-00abb0f0) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb0f4`](#insn-00abb0f4) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0f8`](#insn-00abb0f8) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb0fc`](#insn-00abb0fc) → `0032b740`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00abb100`](#insn-00abb100) → `0032b750`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00abb110`](#insn-00abb110) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abb118`](#insn-00abb118) → `0032b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00abb11c`](#insn-00abb11c) → [`00abb128`](#insn-00abb128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb120`](#insn-00abb120) → `0032b768`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[43]`
- [`00abb124`](#insn-00abb124) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb128`](#insn-00abb128) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb12c`](#insn-00abb12c) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb130`](#insn-00abb130) → `0032b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00abb134`](#insn-00abb134) → `0032b768`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[43]`
- [`00abb13c`](#insn-00abb13c) → [`00465780`](../00465/00465780.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465780` · 推定シンボル `None` · 推定型 `None`
- [`00abb14c`](#insn-00abb14c) → `00297354`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb154`](#insn-00abb154) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb15c`](#insn-00abb15c) → `Stack[-0x1d7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb160`](#insn-00abb160) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb164`](#insn-00abb164) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb168`](#insn-00abb168) → `Stack[-0x20f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb16c`](#insn-00abb16c) → `Stack[-0x20b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb178`](#insn-00abb178) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00abb188`](#insn-00abb188) → [`0046ff30`](../0046f/0046ff30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ff30` · 推定シンボル `None` · 推定型 `None`
- [`00abb19c`](#insn-00abb19c) → [`00ab1128`](../00ab1/00ab1128.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab1128` · 推定シンボル `None` · 推定型 `None`
- [`00abb1a0`](#insn-00abb1a0) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1a8`](#insn-00abb1a8) → [`00abb2c8`](#insn-00abb2c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1ac`](#insn-00abb1ac) → `Stack[-0x228]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1b0`](#insn-00abb1b0) → [`00abb2d8`](#insn-00abb2d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1b4`](#insn-00abb1b4) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1b8`](#insn-00abb1b8) → [`00abb2e8`](#insn-00abb2e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1bc`](#insn-00abb1bc) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1c0`](#insn-00abb1c0) → [`00abb1cc`](#insn-00abb1cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1c4`](#insn-00abb1c4) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1c8`](#insn-00abb1c8) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb1d4`](#insn-00abb1d4) → [`00abb230`](#insn-00abb230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1e0`](#insn-00abb1e0) → [`00abb200`](#insn-00abb200) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1e4`](#insn-00abb1e4) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1e8`](#insn-00abb1e8) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb1f0`](#insn-00abb1f0) → `002a3180`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb1f4`](#insn-00abb1f4) → `002a3190`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb1fc`](#insn-00abb1fc) → [`00abb230`](#insn-00abb230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb208`](#insn-00abb208) → [`00465394`](../00465/00465394.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465394` · 推定シンボル `None` · 推定型 `None`
- [`00abb218`](#insn-00abb218) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abb21c`](#insn-00abb21c) → `002a3180`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb220`](#insn-00abb220) → [`00abb1e4`](#insn-00abb1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb224`](#insn-00abb224) → `002a3190`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb228`](#insn-00abb228) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb22c`](#insn-00abb22c) → [`00abb1e4`](#insn-00abb1e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb234`](#insn-00abb234) → [`00465780`](../00465/00465780.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465780` · 推定シンボル `None` · 推定型 `None`
- [`00abb244`](#insn-00abb244) → `002ad1ab`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb248`](#insn-00abb248) → `002ad1b2`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb24c`](#insn-00abb24c) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb254`](#insn-00abb254) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb258`](#insn-00abb258) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb25c`](#insn-00abb25c) → `Stack[-0x1d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb260`](#insn-00abb260) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb264`](#insn-00abb264) → `Stack[-0x20f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb268`](#insn-00abb268) → `Stack[-0x20b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb274`](#insn-00abb274) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00abb284`](#insn-00abb284) → [`0046ff30`](../0046f/0046ff30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ff30` · 推定シンボル `None` · 推定型 `None`
- [`00abb298`](#insn-00abb298) → [`00ab1128`](../00ab1/00ab1128.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab1128` · 推定シンボル `None` · 推定型 `None`
- [`00abb29c`](#insn-00abb29c) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2a4`](#insn-00abb2a4) → [`00abb2fc`](#insn-00abb2fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2a8`](#insn-00abb2a8) → `Stack[-0x240]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2ac`](#insn-00abb2ac) → [`00abb30c`](#insn-00abb30c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2b0`](#insn-00abb2b0) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2b4`](#insn-00abb2b4) → [`00abb31c`](#insn-00abb31c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2b8`](#insn-00abb2b8) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2bc`](#insn-00abb2bc) → [`00abb32c`](#insn-00abb32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2c0`](#insn-00abb2c0) → [`00abb338`](#insn-00abb338) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2c4`](#insn-00abb2c4) → [`00abb390`](#insn-00abb390) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2c8`](#insn-00abb2c8) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2cc`](#insn-00abb2cc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb2d0`](#insn-00abb2d0) → `Stack[-0x228]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2d4`](#insn-00abb2d4) → [`00abb1b4`](#insn-00abb1b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2d8`](#insn-00abb2d8) → `Stack[-0x218]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2dc`](#insn-00abb2dc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb2e0`](#insn-00abb2e0) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2e4`](#insn-00abb2e4) → [`00abb1bc`](#insn-00abb1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2e8`](#insn-00abb2e8) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2ec`](#insn-00abb2ec) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb2f0`](#insn-00abb2f0) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2f4`](#insn-00abb2f4) → [`00abb1c4`](#insn-00abb1c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2f8`](#insn-00abb2f8) → [`00abb1cc`](#insn-00abb1cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb2fc`](#insn-00abb2fc) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb300`](#insn-00abb300) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb304`](#insn-00abb304) → `Stack[-0x240]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb308`](#insn-00abb308) → [`00abb2b0`](#insn-00abb2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb30c`](#insn-00abb30c) → `Stack[-0x230]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb310`](#insn-00abb310) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb314`](#insn-00abb314) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb318`](#insn-00abb318) → [`00abb2b8`](#insn-00abb2b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb31c`](#insn-00abb31c) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb320`](#insn-00abb320) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb324`](#insn-00abb324) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb328`](#insn-00abb328) → [`00abb2c0`](#insn-00abb2c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb32c`](#insn-00abb32c) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb330`](#insn-00abb330) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb334`](#insn-00abb334) → [`00abb390`](#insn-00abb390) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb340`](#insn-00abb340) → [`00abb360`](#insn-00abb360) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb344`](#insn-00abb344) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb348`](#insn-00abb348) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb350`](#insn-00abb350) → `002a3858`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb354`](#insn-00abb354) → `002a3868`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb35c`](#insn-00abb35c) → [`00abb390`](#insn-00abb390) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb368`](#insn-00abb368) → [`00465394`](../00465/00465394.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465394` · 推定シンボル `None` · 推定型 `None`
- [`00abb378`](#insn-00abb378) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abb37c`](#insn-00abb37c) → `002a3858`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb380`](#insn-00abb380) → [`00abb344`](#insn-00abb344) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb384`](#insn-00abb384) → `002a3868`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb388`](#insn-00abb388) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb38c`](#insn-00abb38c) → [`00abb344`](#insn-00abb344) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb394`](#insn-00abb394) → [`00465780`](../00465/00465780.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465780` · 推定シンボル `None` · 推定型 `None`
- [`00abb3a4`](#insn-00abb3a4) → `0029ed03`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb3ac`](#insn-00abb3ac) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb3b4`](#insn-00abb3b4) → `Stack[-0x1d7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb3b8`](#insn-00abb3b8) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb3bc`](#insn-00abb3bc) → `Stack[-0x1d5]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb3c0`](#insn-00abb3c0) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb3c4`](#insn-00abb3c4) → `Stack[-0x20f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb3c8`](#insn-00abb3c8) → `Stack[-0x20b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb3d4`](#insn-00abb3d4) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00abb3e4`](#insn-00abb3e4) → [`0046ff30`](../0046f/0046ff30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ff30` · 推定シンボル `None` · 推定型 `None`
- [`00abb3f8`](#insn-00abb3f8) → [`00ab1128`](../00ab1/00ab1128.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab1128` · 推定シンボル `None` · 推定型 `None`
- [`00abb3fc`](#insn-00abb3fc) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb404`](#insn-00abb404) → [`00abb428`](#insn-00abb428) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb408`](#insn-00abb408) → `Stack[-0x258]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb40c`](#insn-00abb40c) → [`00abb438`](#insn-00abb438) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb410`](#insn-00abb410) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb414`](#insn-00abb414) → [`00abb448`](#insn-00abb448) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb418`](#insn-00abb418) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb41c`](#insn-00abb41c) → [`00abb458`](#insn-00abb458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb420`](#insn-00abb420) → [`00abb464`](#insn-00abb464) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb424`](#insn-00abb424) → [`00abb4bc`](#insn-00abb4bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb428`](#insn-00abb428) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb42c`](#insn-00abb42c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb430`](#insn-00abb430) → `Stack[-0x258]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb434`](#insn-00abb434) → [`00abb410`](#insn-00abb410) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb438`](#insn-00abb438) → `Stack[-0x248]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb43c`](#insn-00abb43c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb440`](#insn-00abb440) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb444`](#insn-00abb444) → [`00abb418`](#insn-00abb418) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb448`](#insn-00abb448) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb44c`](#insn-00abb44c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb450`](#insn-00abb450) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb454`](#insn-00abb454) → [`00abb420`](#insn-00abb420) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb458`](#insn-00abb458) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb45c`](#insn-00abb45c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb460`](#insn-00abb460) → [`00abb4bc`](#insn-00abb4bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb46c`](#insn-00abb46c) → [`00abb48c`](#insn-00abb48c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb470`](#insn-00abb470) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb474`](#insn-00abb474) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb47c`](#insn-00abb47c) → `002a3f30`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb480`](#insn-00abb480) → `002a3f40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb488`](#insn-00abb488) → [`00abb4bc`](#insn-00abb4bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb494`](#insn-00abb494) → [`00465394`](../00465/00465394.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465394` · 推定シンボル `None` · 推定型 `None`
- [`00abb4a4`](#insn-00abb4a4) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abb4a8`](#insn-00abb4a8) → `002a3f30`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb4ac`](#insn-00abb4ac) → [`00abb470`](#insn-00abb470) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb4b0`](#insn-00abb4b0) → `002a3f40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb4b4`](#insn-00abb4b4) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb4b8`](#insn-00abb4b8) → [`00abb470`](#insn-00abb470) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb4c0`](#insn-00abb4c0) → [`00465780`](../00465/00465780.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465780` · 推定シンボル `None` · 推定型 `None`
- [`00abb4d0`](#insn-00abb4d0) → `00292226`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb4d8`](#insn-00abb4d8) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb4e0`](#insn-00abb4e0) → `Stack[-0x1d7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb4e4`](#insn-00abb4e4) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb4e8`](#insn-00abb4e8) → `Stack[-0x1d5]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb4ec`](#insn-00abb4ec) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb4f0`](#insn-00abb4f0) → `Stack[-0x20f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb4f4`](#insn-00abb4f4) → `Stack[-0x20b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb500`](#insn-00abb500) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00abb510`](#insn-00abb510) → [`0046ff30`](../0046f/0046ff30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ff30` · 推定シンボル `None` · 推定型 `None`
- [`00abb524`](#insn-00abb524) → [`00ab1128`](../00ab1/00ab1128.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab1128` · 推定シンボル `None` · 推定型 `None`
- [`00abb528`](#insn-00abb528) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb530`](#insn-00abb530) → [`00abb554`](#insn-00abb554) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb534`](#insn-00abb534) → `Stack[-0x270]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb538`](#insn-00abb538) → [`00abb564`](#insn-00abb564) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb53c`](#insn-00abb53c) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb540`](#insn-00abb540) → [`00abb574`](#insn-00abb574) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb544`](#insn-00abb544) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb548`](#insn-00abb548) → [`00abb584`](#insn-00abb584) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb54c`](#insn-00abb54c) → [`00abb590`](#insn-00abb590) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb550`](#insn-00abb550) → [`00abb5ec`](#insn-00abb5ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb554`](#insn-00abb554) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb558`](#insn-00abb558) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb55c`](#insn-00abb55c) → `Stack[-0x270]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb560`](#insn-00abb560) → [`00abb53c`](#insn-00abb53c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb564`](#insn-00abb564) → `Stack[-0x260]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb568`](#insn-00abb568) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb56c`](#insn-00abb56c) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb570`](#insn-00abb570) → [`00abb544`](#insn-00abb544) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb574`](#insn-00abb574) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb578`](#insn-00abb578) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb57c`](#insn-00abb57c) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb580`](#insn-00abb580) → [`00abb54c`](#insn-00abb54c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb584`](#insn-00abb584) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb588`](#insn-00abb588) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb58c`](#insn-00abb58c) → [`00abb5ec`](#insn-00abb5ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb59c`](#insn-00abb59c) → [`00abb5bc`](#insn-00abb5bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb5a0`](#insn-00abb5a0) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb5a4`](#insn-00abb5a4) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb5ac`](#insn-00abb5ac) → `002a4668`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb5b0`](#insn-00abb5b0) → `002a4678`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb5b8`](#insn-00abb5b8) → [`00abb5ec`](#insn-00abb5ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb5c4`](#insn-00abb5c4) → [`00465394`](../00465/00465394.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465394` · 推定シンボル `None` · 推定型 `None`
- [`00abb5d4`](#insn-00abb5d4) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abb5d8`](#insn-00abb5d8) → `002a4668`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb5dc`](#insn-00abb5dc) → [`00abb5a0`](#insn-00abb5a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb5e0`](#insn-00abb5e0) → `002a4678`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abb5e4`](#insn-00abb5e4) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb5e8`](#insn-00abb5e8) → [`00abb5a0`](#insn-00abb5a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb5f4`](#insn-00abb5f4) → [`00465780`](../00465/00465780.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465780` · 推定シンボル `None` · 推定型 `None`
- [`00abb604`](#insn-00abb604) → `00c1acc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abb608`](#insn-00abb608) → `00c1acc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abb60c`](#insn-00abb60c) → `00c13358`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`00abb614`](#insn-00abb614) → `00be8758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abb614`](#insn-00abb614) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb618`](#insn-00abb618) → `00c112f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abb618`](#insn-00abb618) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb61c`](#insn-00abb61c) → `00c112e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`00abb620`](#insn-00abb620) → `00c13370`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`00abb624`](#insn-00abb624) → `00c11320`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abb62c`](#insn-00abb62c) → `00c1acd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abb630`](#insn-00abb630) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb638`](#insn-00abb638) → `00c11078`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00abb638`](#insn-00abb638) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb63c`](#insn-00abb63c) → [`00abb648`](#insn-00abb648) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb640`](#insn-00abb640) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb644`](#insn-00abb644) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb64c`](#insn-00abb64c) → [`00bdb050`](../00bdb/00bdb050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb050` · 推定シンボル `None` · 推定型 `None`
- [`00abb650`](#insn-00abb650) → `00c13360`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`00abb658`](#insn-00abb658) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00abb664`](#insn-00abb664) → [`00bdb070`](../00bdb/00bdb070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb070` · 推定シンボル `None` · 推定型 `None`
- [`00abb668`](#insn-00abb668) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb66c`](#insn-00abb66c) → [`00abb678`](#insn-00abb678) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb670`](#insn-00abb670) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb674`](#insn-00abb674) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb678`](#insn-00abb678) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb67c`](#insn-00abb67c) → [`00abb688`](#insn-00abb688) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb680`](#insn-00abb680) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb684`](#insn-00abb684) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abb68c`](#insn-00abb68c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb694`](#insn-00abb694) → [`00abb820`](#insn-00abb820) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb69c`](#insn-00abb69c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb6a0`](#insn-00abb6a0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb6a4`](#insn-00abb6a4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb6a8`](#insn-00abb6a8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb6ac`](#insn-00abb6ac) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abb820`](#insn-00abb820) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abae5c`](#insn-00abae5c)

~~~json
{
  "source": "00abae5c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae60`](#insn-00abae60)

~~~json
{
  "source": "00abae60",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae64`](#insn-00abae64)

~~~json
{
  "source": "00abae64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae68`](#insn-00abae68)

~~~json
{
  "source": "00abae68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae6c`](#insn-00abae6c)

~~~json
{
  "source": "00abae6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae88`](#insn-00abae88)

~~~json
{
  "source": "00abae88",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae8c`](#insn-00abae8c)

~~~json
{
  "source": "00abae8c",
  "target": "00464f48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae98`](#insn-00abae98)

~~~json
{
  "source": "00abae98",
  "target": "00be7c78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be7c78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abae98`](#insn-00abae98)

~~~json
{
  "source": "00abae98",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaea4`](#insn-00abaea4)

~~~json
{
  "source": "00abaea4",
  "target": "00a3df28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaeb8`](#insn-00abaeb8)

~~~json
{
  "source": "00abaeb8",
  "target": "002b03d6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b03d6",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "45445f4d6573736167655f25402e63737600",
  "capture_start": "002b03d6",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abaebc`](#insn-00abaebc)

~~~json
{
  "source": "00abaebc",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaec8`](#insn-00abaec8)

~~~json
{
  "source": "00abaec8",
  "target": "Stack[-0x20b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaecc`](#insn-00abaecc)

~~~json
{
  "source": "00abaecc",
  "target": "Stack[-0x1cf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaed8`](#insn-00abaed8)

~~~json
{
  "source": "00abaed8",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaedc`](#insn-00abaedc)

~~~json
{
  "source": "00abaedc",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaee0`](#insn-00abaee0)

~~~json
{
  "source": "00abaee0",
  "target": "Stack[-0x20f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaeec`](#insn-00abaeec)

~~~json
{
  "source": "00abaeec",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaefc`](#insn-00abaefc)

~~~json
{
  "source": "00abaefc",
  "target": "0046ff30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaf10`](#insn-00abaf10)

~~~json
{
  "source": "00abaf10",
  "target": "00ab1128",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaf14`](#insn-00abaf14)

~~~json
{
  "source": "00abaf14",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf1c`](#insn-00abaf1c)

~~~json
{
  "source": "00abaf1c",
  "target": "00abaf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf20`](#insn-00abaf20)

~~~json
{
  "source": "00abaf20",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf24`](#insn-00abaf24)

~~~json
{
  "source": "00abaf24",
  "target": "00abaf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf28`](#insn-00abaf28)

~~~json
{
  "source": "00abaf28",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf2c`](#insn-00abaf2c)

~~~json
{
  "source": "00abaf2c",
  "target": "00abaf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf30`](#insn-00abaf30)

~~~json
{
  "source": "00abaf30",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf34`](#insn-00abaf34)

~~~json
{
  "source": "00abaf34",
  "target": "00abaf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf38`](#insn-00abaf38)

~~~json
{
  "source": "00abaf38",
  "target": "00abaf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf3c`](#insn-00abaf3c)

~~~json
{
  "source": "00abaf3c",
  "target": "00abb138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf40`](#insn-00abaf40)

~~~json
{
  "source": "00abaf40",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf44`](#insn-00abaf44)

~~~json
{
  "source": "00abaf44",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaf48`](#insn-00abaf48)

~~~json
{
  "source": "00abaf48",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf4c`](#insn-00abaf4c)

~~~json
{
  "source": "00abaf4c",
  "target": "00abaf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf50`](#insn-00abaf50)

~~~json
{
  "source": "00abaf50",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf54`](#insn-00abaf54)

~~~json
{
  "source": "00abaf54",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaf58`](#insn-00abaf58)

~~~json
{
  "source": "00abaf58",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf5c`](#insn-00abaf5c)

~~~json
{
  "source": "00abaf5c",
  "target": "00abaf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf60`](#insn-00abaf60)

~~~json
{
  "source": "00abaf60",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf64`](#insn-00abaf64)

~~~json
{
  "source": "00abaf64",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaf68`](#insn-00abaf68)

~~~json
{
  "source": "00abaf68",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf6c`](#insn-00abaf6c)

~~~json
{
  "source": "00abaf6c",
  "target": "00abaf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf70`](#insn-00abaf70)

~~~json
{
  "source": "00abaf70",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf74`](#insn-00abaf74)

~~~json
{
  "source": "00abaf74",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaf78`](#insn-00abaf78)

~~~json
{
  "source": "00abaf78",
  "target": "00abb138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf84`](#insn-00abaf84)

~~~json
{
  "source": "00abaf84",
  "target": "00465394",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaf94`](#insn-00abaf94)

~~~json
{
  "source": "00abaf94",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abafa0`](#insn-00abafa0)

~~~json
{
  "source": "00abafa0",
  "target": "0032b6b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6a9",
  "offset": 7,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "0032b6a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abafa4`](#insn-00abafa4)

~~~json
{
  "source": "00abafa4",
  "target": "00abafb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abafa8`](#insn-00abafa8)

~~~json
{
  "source": "00abafa8",
  "target": "0032b6c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6a9",
  "offset": 23,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "0032b6a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abafac`](#insn-00abafac)

~~~json
{
  "source": "00abafac",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abafb0`](#insn-00abafb0)

~~~json
{
  "source": "00abafb0",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abafb4`](#insn-00abafb4)

~~~json
{
  "source": "00abafb4",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abafb8`](#insn-00abafb8)

~~~json
{
  "source": "00abafb8",
  "target": "0032b6b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6a9",
  "offset": 7,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "0032b6a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abafbc`](#insn-00abafbc)

~~~json
{
  "source": "00abafbc",
  "target": "0032b6c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6a9",
  "offset": 23,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "0032b6a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abafcc`](#insn-00abafcc)

~~~json
{
  "source": "00abafcc",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abafd4`](#insn-00abafd4)

~~~json
{
  "source": "00abafd4",
  "target": "0032b6c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6a9",
  "offset": 31,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "0032b6a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abafd8`](#insn-00abafd8)

~~~json
{
  "source": "00abafd8",
  "target": "00abafe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abafdc`](#insn-00abafdc)

~~~json
{
  "source": "00abafdc",
  "target": "0032b6d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6d8",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34d00e00",
  "capture_start": "0032b6d8",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abafe0`](#insn-00abafe0)

~~~json
{
  "source": "00abafe0",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abafe4`](#insn-00abafe4)

~~~json
{
  "source": "00abafe4",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abafe8`](#insn-00abafe8)

~~~json
{
  "source": "00abafe8",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abafec`](#insn-00abafec)

~~~json
{
  "source": "00abafec",
  "target": "0032b6c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6a9",
  "offset": 31,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "0032b6a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abaff0`](#insn-00abaff0)

~~~json
{
  "source": "00abaff0",
  "target": "0032b6d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6d8",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34d00e00",
  "capture_start": "0032b6d8",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb000`](#insn-00abb000)

~~~json
{
  "source": "00abb000",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb008`](#insn-00abb008)

~~~json
{
  "source": "00abb008",
  "target": "0032b6e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6dc",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0032b6dc",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb00c`](#insn-00abb00c)

~~~json
{
  "source": "00abb00c",
  "target": "00abb018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb010`](#insn-00abb010)

~~~json
{
  "source": "00abb010",
  "target": "0032b6f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6f0",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0032b6f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb014`](#insn-00abb014)

~~~json
{
  "source": "00abb014",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb018`](#insn-00abb018)

~~~json
{
  "source": "00abb018",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb01c`](#insn-00abb01c)

~~~json
{
  "source": "00abb01c",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb020`](#insn-00abb020)

~~~json
{
  "source": "00abb020",
  "target": "0032b6e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6dc",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0032b6dc",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb024`](#insn-00abb024)

~~~json
{
  "source": "00abb024",
  "target": "0032b6f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6f0",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0032b6f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb034`](#insn-00abb034)

~~~json
{
  "source": "00abb034",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb03c`](#insn-00abb03c)

~~~json
{
  "source": "00abb03c",
  "target": "0032b6f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6f8",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0032b6f8",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb040`](#insn-00abb040)

~~~json
{
  "source": "00abb040",
  "target": "00abb04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb044`](#insn-00abb044)

~~~json
{
  "source": "00abb044",
  "target": "0032b708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b704",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0032b704",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb048`](#insn-00abb048)

~~~json
{
  "source": "00abb048",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb04c`](#insn-00abb04c)

~~~json
{
  "source": "00abb04c",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb050`](#insn-00abb050)

~~~json
{
  "source": "00abb050",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb054`](#insn-00abb054)

~~~json
{
  "source": "00abb054",
  "target": "0032b6f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b6f8",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0032b6f8",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb058`](#insn-00abb058)

~~~json
{
  "source": "00abb058",
  "target": "0032b708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b704",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0032b704",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb064`](#insn-00abb064)

~~~json
{
  "source": "00abb064",
  "target": "00465394",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb074`](#insn-00abb074)

~~~json
{
  "source": "00abb074",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb07c`](#insn-00abb07c)

~~~json
{
  "source": "00abb07c",
  "target": "0032b710",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b710",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "18020000",
  "capture_start": "0032b710",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb080`](#insn-00abb080)

~~~json
{
  "source": "00abb080",
  "target": "00abb08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb084`](#insn-00abb084)

~~~json
{
  "source": "00abb084",
  "target": "0032b720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b720",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0032b720",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb088`](#insn-00abb088)

~~~json
{
  "source": "00abb088",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb08c`](#insn-00abb08c)

~~~json
{
  "source": "00abb08c",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb090`](#insn-00abb090)

~~~json
{
  "source": "00abb090",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb094`](#insn-00abb094)

~~~json
{
  "source": "00abb094",
  "target": "0032b710",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b710",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "18020000",
  "capture_start": "0032b710",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb098`](#insn-00abb098)

~~~json
{
  "source": "00abb098",
  "target": "0032b720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b720",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0032b720",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0a8`](#insn-00abb0a8)

~~~json
{
  "source": "00abb0a8",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb0b0`](#insn-00abb0b0)

~~~json
{
  "source": "00abb0b0",
  "target": "0032b728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b728",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "24d00e00",
  "capture_start": "0032b728",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0b4`](#insn-00abb0b4)

~~~json
{
  "source": "00abb0b4",
  "target": "00abb0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0b8`](#insn-00abb0b8)

~~~json
{
  "source": "00abb0b8",
  "target": "0032b738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b738",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "40020000",
  "capture_start": "0032b738",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0bc`](#insn-00abb0bc)

~~~json
{
  "source": "00abb0bc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb0c0`](#insn-00abb0c0)

~~~json
{
  "source": "00abb0c0",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0c4`](#insn-00abb0c4)

~~~json
{
  "source": "00abb0c4",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0c8`](#insn-00abb0c8)

~~~json
{
  "source": "00abb0c8",
  "target": "0032b728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b728",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "24d00e00",
  "capture_start": "0032b728",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0cc`](#insn-00abb0cc)

~~~json
{
  "source": "00abb0cc",
  "target": "0032b738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b738",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "40020000",
  "capture_start": "0032b738",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0dc`](#insn-00abb0dc)

~~~json
{
  "source": "00abb0dc",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb0e4`](#insn-00abb0e4)

~~~json
{
  "source": "00abb0e4",
  "target": "0032b740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b740",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0032b740",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0e8`](#insn-00abb0e8)

~~~json
{
  "source": "00abb0e8",
  "target": "00abb0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0ec`](#insn-00abb0ec)

~~~json
{
  "source": "00abb0ec",
  "target": "0032b750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b750",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "1cd00e00",
  "capture_start": "0032b750",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb0f0`](#insn-00abb0f0)

~~~json
{
  "source": "00abb0f0",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb0f4`](#insn-00abb0f4)

~~~json
{
  "source": "00abb0f4",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0f8`](#insn-00abb0f8)

~~~json
{
  "source": "00abb0f8",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb0fc`](#insn-00abb0fc)

~~~json
{
  "source": "00abb0fc",
  "target": "0032b740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b740",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0032b740",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb100`](#insn-00abb100)

~~~json
{
  "source": "00abb100",
  "target": "0032b750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b750",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "1cd00e00",
  "capture_start": "0032b750",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb110`](#insn-00abb110)

~~~json
{
  "source": "00abb110",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb118`](#insn-00abb118)

~~~json
{
  "source": "00abb118",
  "target": "0032b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b758",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0032b758",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb11c`](#insn-00abb11c)

~~~json
{
  "source": "00abb11c",
  "target": "00abb128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb120`](#insn-00abb120)

~~~json
{
  "source": "00abb120",
  "target": "0032b768",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b759",
  "offset": 15,
  "size": 43,
  "datatype": "byte[43]",
  "bytes": "440e20480c1d20930294049e069d080a02980c1f20480e00d3d4dedd440b0c1f",
  "capture_start": "0032b759",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb124`](#insn-00abb124)

~~~json
{
  "source": "00abb124",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb128`](#insn-00abb128)

~~~json
{
  "source": "00abb128",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb12c`](#insn-00abb12c)

~~~json
{
  "source": "00abb12c",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb130`](#insn-00abb130)

~~~json
{
  "source": "00abb130",
  "target": "0032b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b758",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0032b758",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb134`](#insn-00abb134)

~~~json
{
  "source": "00abb134",
  "target": "0032b768",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032b759",
  "offset": 15,
  "size": 43,
  "datatype": "byte[43]",
  "bytes": "440e20480c1d20930294049e069d080a02980c1f20480e00d3d4dedd440b0c1f",
  "capture_start": "0032b759",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb13c`](#insn-00abb13c)

~~~json
{
  "source": "00abb13c",
  "target": "00465780",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb14c`](#insn-00abb14c)

~~~json
{
  "source": "00abb14c",
  "target": "00297354",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297354",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "4f505f25402e63737600",
  "capture_start": "00297354",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb154`](#insn-00abb154)

~~~json
{
  "source": "00abb154",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb15c`](#insn-00abb15c)

~~~json
{
  "source": "00abb15c",
  "target": "Stack[-0x1d7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb160`](#insn-00abb160)

~~~json
{
  "source": "00abb160",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb164`](#insn-00abb164)

~~~json
{
  "source": "00abb164",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb168`](#insn-00abb168)

~~~json
{
  "source": "00abb168",
  "target": "Stack[-0x20f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb16c`](#insn-00abb16c)

~~~json
{
  "source": "00abb16c",
  "target": "Stack[-0x20b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb178`](#insn-00abb178)

~~~json
{
  "source": "00abb178",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb188`](#insn-00abb188)

~~~json
{
  "source": "00abb188",
  "target": "0046ff30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb19c`](#insn-00abb19c)

~~~json
{
  "source": "00abb19c",
  "target": "00ab1128",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb1a0`](#insn-00abb1a0)

~~~json
{
  "source": "00abb1a0",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1a8`](#insn-00abb1a8)

~~~json
{
  "source": "00abb1a8",
  "target": "00abb2c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1ac`](#insn-00abb1ac)

~~~json
{
  "source": "00abb1ac",
  "target": "Stack[-0x228]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1b0`](#insn-00abb1b0)

~~~json
{
  "source": "00abb1b0",
  "target": "00abb2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1b4`](#insn-00abb1b4)

~~~json
{
  "source": "00abb1b4",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1b8`](#insn-00abb1b8)

~~~json
{
  "source": "00abb1b8",
  "target": "00abb2e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1bc`](#insn-00abb1bc)

~~~json
{
  "source": "00abb1bc",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1c0`](#insn-00abb1c0)

~~~json
{
  "source": "00abb1c0",
  "target": "00abb1cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1c4`](#insn-00abb1c4)

~~~json
{
  "source": "00abb1c4",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1c8`](#insn-00abb1c8)

~~~json
{
  "source": "00abb1c8",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb1d4`](#insn-00abb1d4)

~~~json
{
  "source": "00abb1d4",
  "target": "00abb230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1e0`](#insn-00abb1e0)

~~~json
{
  "source": "00abb1e0",
  "target": "00abb200",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1e4`](#insn-00abb1e4)

~~~json
{
  "source": "00abb1e4",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1e8`](#insn-00abb1e8)

~~~json
{
  "source": "00abb1e8",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb1f0`](#insn-00abb1f0)

~~~json
{
  "source": "00abb1f0",
  "target": "002a3180",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a317d",
  "offset": 3,
  "size": 17,
  "datatype": "string",
  "bytes": "726563656970745369676e617475726500",
  "capture_start": "002a317d",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb1f4`](#insn-00abb1f4)

~~~json
{
  "source": "00abb1f4",
  "target": "002a3190",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a318e",
  "offset": 2,
  "size": 15,
  "datatype": "string",
  "bytes": "2f76322f7472616e73666572732f00",
  "capture_start": "002a318e",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb1fc`](#insn-00abb1fc)

~~~json
{
  "source": "00abb1fc",
  "target": "00abb230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb208`](#insn-00abb208)

~~~json
{
  "source": "00abb208",
  "target": "00465394",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb218`](#insn-00abb218)

~~~json
{
  "source": "00abb218",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb21c`](#insn-00abb21c)

~~~json
{
  "source": "00abb21c",
  "target": "002a3180",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a317d",
  "offset": 3,
  "size": 17,
  "datatype": "string",
  "bytes": "726563656970745369676e617475726500",
  "capture_start": "002a317d",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb220`](#insn-00abb220)

~~~json
{
  "source": "00abb220",
  "target": "00abb1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb224`](#insn-00abb224)

~~~json
{
  "source": "00abb224",
  "target": "002a3190",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a318e",
  "offset": 2,
  "size": 15,
  "datatype": "string",
  "bytes": "2f76322f7472616e73666572732f00",
  "capture_start": "002a318e",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb228`](#insn-00abb228)

~~~json
{
  "source": "00abb228",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb22c`](#insn-00abb22c)

~~~json
{
  "source": "00abb22c",
  "target": "00abb1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb234`](#insn-00abb234)

~~~json
{
  "source": "00abb234",
  "target": "00465780",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb244`](#insn-00abb244)

~~~json
{
  "source": "00abb244",
  "target": "002ad1ab",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad1ab",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "4f504c6567656e645f25402e63737600",
  "capture_start": "002ad1ab",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb248`](#insn-00abb248)

~~~json
{
  "source": "00abb248",
  "target": "002ad1b2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad1ab",
  "offset": 7,
  "size": 16,
  "datatype": "string",
  "bytes": "4f504c6567656e645f25402e63737600",
  "capture_start": "002ad1ab",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb24c`](#insn-00abb24c)

~~~json
{
  "source": "00abb24c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb254`](#insn-00abb254)

~~~json
{
  "source": "00abb254",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb258`](#insn-00abb258)

~~~json
{
  "source": "00abb258",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb25c`](#insn-00abb25c)

~~~json
{
  "source": "00abb25c",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb260`](#insn-00abb260)

~~~json
{
  "source": "00abb260",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb264`](#insn-00abb264)

~~~json
{
  "source": "00abb264",
  "target": "Stack[-0x20f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb268`](#insn-00abb268)

~~~json
{
  "source": "00abb268",
  "target": "Stack[-0x20b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb274`](#insn-00abb274)

~~~json
{
  "source": "00abb274",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb284`](#insn-00abb284)

~~~json
{
  "source": "00abb284",
  "target": "0046ff30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb298`](#insn-00abb298)

~~~json
{
  "source": "00abb298",
  "target": "00ab1128",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb29c`](#insn-00abb29c)

~~~json
{
  "source": "00abb29c",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2a4`](#insn-00abb2a4)

~~~json
{
  "source": "00abb2a4",
  "target": "00abb2fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2a8`](#insn-00abb2a8)

~~~json
{
  "source": "00abb2a8",
  "target": "Stack[-0x240]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2ac`](#insn-00abb2ac)

~~~json
{
  "source": "00abb2ac",
  "target": "00abb30c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2b0`](#insn-00abb2b0)

~~~json
{
  "source": "00abb2b0",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2b4`](#insn-00abb2b4)

~~~json
{
  "source": "00abb2b4",
  "target": "00abb31c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2b8`](#insn-00abb2b8)

~~~json
{
  "source": "00abb2b8",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2bc`](#insn-00abb2bc)

~~~json
{
  "source": "00abb2bc",
  "target": "00abb32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2c0`](#insn-00abb2c0)

~~~json
{
  "source": "00abb2c0",
  "target": "00abb338",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2c4`](#insn-00abb2c4)

~~~json
{
  "source": "00abb2c4",
  "target": "00abb390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2c8`](#insn-00abb2c8)

~~~json
{
  "source": "00abb2c8",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2cc`](#insn-00abb2cc)

~~~json
{
  "source": "00abb2cc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb2d0`](#insn-00abb2d0)

~~~json
{
  "source": "00abb2d0",
  "target": "Stack[-0x228]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2d4`](#insn-00abb2d4)

~~~json
{
  "source": "00abb2d4",
  "target": "00abb1b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2d8`](#insn-00abb2d8)

~~~json
{
  "source": "00abb2d8",
  "target": "Stack[-0x218]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2dc`](#insn-00abb2dc)

~~~json
{
  "source": "00abb2dc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb2e0`](#insn-00abb2e0)

~~~json
{
  "source": "00abb2e0",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2e4`](#insn-00abb2e4)

~~~json
{
  "source": "00abb2e4",
  "target": "00abb1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2e8`](#insn-00abb2e8)

~~~json
{
  "source": "00abb2e8",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2ec`](#insn-00abb2ec)

~~~json
{
  "source": "00abb2ec",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb2f0`](#insn-00abb2f0)

~~~json
{
  "source": "00abb2f0",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2f4`](#insn-00abb2f4)

~~~json
{
  "source": "00abb2f4",
  "target": "00abb1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2f8`](#insn-00abb2f8)

~~~json
{
  "source": "00abb2f8",
  "target": "00abb1cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb2fc`](#insn-00abb2fc)

~~~json
{
  "source": "00abb2fc",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb300`](#insn-00abb300)

~~~json
{
  "source": "00abb300",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb304`](#insn-00abb304)

~~~json
{
  "source": "00abb304",
  "target": "Stack[-0x240]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb308`](#insn-00abb308)

~~~json
{
  "source": "00abb308",
  "target": "00abb2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb30c`](#insn-00abb30c)

~~~json
{
  "source": "00abb30c",
  "target": "Stack[-0x230]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb310`](#insn-00abb310)

~~~json
{
  "source": "00abb310",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb314`](#insn-00abb314)

~~~json
{
  "source": "00abb314",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb318`](#insn-00abb318)

~~~json
{
  "source": "00abb318",
  "target": "00abb2b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb31c`](#insn-00abb31c)

~~~json
{
  "source": "00abb31c",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb320`](#insn-00abb320)

~~~json
{
  "source": "00abb320",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb324`](#insn-00abb324)

~~~json
{
  "source": "00abb324",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb328`](#insn-00abb328)

~~~json
{
  "source": "00abb328",
  "target": "00abb2c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb32c`](#insn-00abb32c)

~~~json
{
  "source": "00abb32c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb330`](#insn-00abb330)

~~~json
{
  "source": "00abb330",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb334`](#insn-00abb334)

~~~json
{
  "source": "00abb334",
  "target": "00abb390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb340`](#insn-00abb340)

~~~json
{
  "source": "00abb340",
  "target": "00abb360",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb344`](#insn-00abb344)

~~~json
{
  "source": "00abb344",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb348`](#insn-00abb348)

~~~json
{
  "source": "00abb348",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb350`](#insn-00abb350)

~~~json
{
  "source": "00abb350",
  "target": "002a3858",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a37dd",
  "offset": 123,
  "size": 174,
  "datatype": "string",
  "bytes": "25732f76312f6e6f74696365733f706c6174666f726d3d257326636c69656e74",
  "capture_start": "002a37dd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb354`](#insn-00abb354)

~~~json
{
  "source": "00abb354",
  "target": "002a3868",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a37dd",
  "offset": 139,
  "size": 174,
  "datatype": "string",
  "bytes": "25732f76312f6e6f74696365733f706c6174666f726d3d257326636c69656e74",
  "capture_start": "002a37dd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb35c`](#insn-00abb35c)

~~~json
{
  "source": "00abb35c",
  "target": "00abb390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb368`](#insn-00abb368)

~~~json
{
  "source": "00abb368",
  "target": "00465394",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb378`](#insn-00abb378)

~~~json
{
  "source": "00abb378",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb37c`](#insn-00abb37c)

~~~json
{
  "source": "00abb37c",
  "target": "002a3858",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a37dd",
  "offset": 123,
  "size": 174,
  "datatype": "string",
  "bytes": "25732f76312f6e6f74696365733f706c6174666f726d3d257326636c69656e74",
  "capture_start": "002a37dd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb380`](#insn-00abb380)

~~~json
{
  "source": "00abb380",
  "target": "00abb344",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb384`](#insn-00abb384)

~~~json
{
  "source": "00abb384",
  "target": "002a3868",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a37dd",
  "offset": 139,
  "size": 174,
  "datatype": "string",
  "bytes": "25732f76312f6e6f74696365733f706c6174666f726d3d257326636c69656e74",
  "capture_start": "002a37dd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb388`](#insn-00abb388)

~~~json
{
  "source": "00abb388",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb38c`](#insn-00abb38c)

~~~json
{
  "source": "00abb38c",
  "target": "00abb344",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb394`](#insn-00abb394)

~~~json
{
  "source": "00abb394",
  "target": "00465780",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb3a4`](#insn-00abb3a4)

~~~json
{
  "source": "00abb3a4",
  "target": "0029ed03",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ed03",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "4f50325f25402e63737600",
  "capture_start": "0029ed03",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb3ac`](#insn-00abb3ac)

~~~json
{
  "source": "00abb3ac",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb3b4`](#insn-00abb3b4)

~~~json
{
  "source": "00abb3b4",
  "target": "Stack[-0x1d7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb3b8`](#insn-00abb3b8)

~~~json
{
  "source": "00abb3b8",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb3bc`](#insn-00abb3bc)

~~~json
{
  "source": "00abb3bc",
  "target": "Stack[-0x1d5]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb3c0`](#insn-00abb3c0)

~~~json
{
  "source": "00abb3c0",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb3c4`](#insn-00abb3c4)

~~~json
{
  "source": "00abb3c4",
  "target": "Stack[-0x20f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb3c8`](#insn-00abb3c8)

~~~json
{
  "source": "00abb3c8",
  "target": "Stack[-0x20b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb3d4`](#insn-00abb3d4)

~~~json
{
  "source": "00abb3d4",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb3e4`](#insn-00abb3e4)

~~~json
{
  "source": "00abb3e4",
  "target": "0046ff30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb3f8`](#insn-00abb3f8)

~~~json
{
  "source": "00abb3f8",
  "target": "00ab1128",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb3fc`](#insn-00abb3fc)

~~~json
{
  "source": "00abb3fc",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb404`](#insn-00abb404)

~~~json
{
  "source": "00abb404",
  "target": "00abb428",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb408`](#insn-00abb408)

~~~json
{
  "source": "00abb408",
  "target": "Stack[-0x258]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb40c`](#insn-00abb40c)

~~~json
{
  "source": "00abb40c",
  "target": "00abb438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb410`](#insn-00abb410)

~~~json
{
  "source": "00abb410",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb414`](#insn-00abb414)

~~~json
{
  "source": "00abb414",
  "target": "00abb448",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb418`](#insn-00abb418)

~~~json
{
  "source": "00abb418",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb41c`](#insn-00abb41c)

~~~json
{
  "source": "00abb41c",
  "target": "00abb458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb420`](#insn-00abb420)

~~~json
{
  "source": "00abb420",
  "target": "00abb464",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb424`](#insn-00abb424)

~~~json
{
  "source": "00abb424",
  "target": "00abb4bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb428`](#insn-00abb428)

~~~json
{
  "source": "00abb428",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb42c`](#insn-00abb42c)

~~~json
{
  "source": "00abb42c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb430`](#insn-00abb430)

~~~json
{
  "source": "00abb430",
  "target": "Stack[-0x258]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb434`](#insn-00abb434)

~~~json
{
  "source": "00abb434",
  "target": "00abb410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb438`](#insn-00abb438)

~~~json
{
  "source": "00abb438",
  "target": "Stack[-0x248]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb43c`](#insn-00abb43c)

~~~json
{
  "source": "00abb43c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb440`](#insn-00abb440)

~~~json
{
  "source": "00abb440",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb444`](#insn-00abb444)

~~~json
{
  "source": "00abb444",
  "target": "00abb418",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb448`](#insn-00abb448)

~~~json
{
  "source": "00abb448",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb44c`](#insn-00abb44c)

~~~json
{
  "source": "00abb44c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb450`](#insn-00abb450)

~~~json
{
  "source": "00abb450",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb454`](#insn-00abb454)

~~~json
{
  "source": "00abb454",
  "target": "00abb420",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb458`](#insn-00abb458)

~~~json
{
  "source": "00abb458",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb45c`](#insn-00abb45c)

~~~json
{
  "source": "00abb45c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb460`](#insn-00abb460)

~~~json
{
  "source": "00abb460",
  "target": "00abb4bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb46c`](#insn-00abb46c)

~~~json
{
  "source": "00abb46c",
  "target": "00abb48c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb470`](#insn-00abb470)

~~~json
{
  "source": "00abb470",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb474`](#insn-00abb474)

~~~json
{
  "source": "00abb474",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb47c`](#insn-00abb47c)

~~~json
{
  "source": "00abb47c",
  "target": "002a3f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3f20",
  "offset": 16,
  "size": 74,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b4c6a6176612f6c616e672f5374",
  "capture_start": "002a3f20",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb480`](#insn-00abb480)

~~~json
{
  "source": "00abb480",
  "target": "002a3f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3f20",
  "offset": 32,
  "size": 74,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b4c6a6176612f6c616e672f5374",
  "capture_start": "002a3f20",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb488`](#insn-00abb488)

~~~json
{
  "source": "00abb488",
  "target": "00abb4bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb494`](#insn-00abb494)

~~~json
{
  "source": "00abb494",
  "target": "00465394",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb4a4`](#insn-00abb4a4)

~~~json
{
  "source": "00abb4a4",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb4a8`](#insn-00abb4a8)

~~~json
{
  "source": "00abb4a8",
  "target": "002a3f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3f20",
  "offset": 16,
  "size": 74,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b4c6a6176612f6c616e672f5374",
  "capture_start": "002a3f20",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb4ac`](#insn-00abb4ac)

~~~json
{
  "source": "00abb4ac",
  "target": "00abb470",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb4b0`](#insn-00abb4b0)

~~~json
{
  "source": "00abb4b0",
  "target": "002a3f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3f20",
  "offset": 32,
  "size": 74,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b4c6a6176612f6c616e672f5374",
  "capture_start": "002a3f20",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb4b4`](#insn-00abb4b4)

~~~json
{
  "source": "00abb4b4",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb4b8`](#insn-00abb4b8)

~~~json
{
  "source": "00abb4b8",
  "target": "00abb470",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb4c0`](#insn-00abb4c0)

~~~json
{
  "source": "00abb4c0",
  "target": "00465780",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb4d0`](#insn-00abb4d0)

~~~json
{
  "source": "00abb4d0",
  "target": "00292226",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00292226",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "4f50335f25402e63737600",
  "capture_start": "00292226",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb4d8`](#insn-00abb4d8)

~~~json
{
  "source": "00abb4d8",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb4e0`](#insn-00abb4e0)

~~~json
{
  "source": "00abb4e0",
  "target": "Stack[-0x1d7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb4e4`](#insn-00abb4e4)

~~~json
{
  "source": "00abb4e4",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb4e8`](#insn-00abb4e8)

~~~json
{
  "source": "00abb4e8",
  "target": "Stack[-0x1d5]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb4ec`](#insn-00abb4ec)

~~~json
{
  "source": "00abb4ec",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb4f0`](#insn-00abb4f0)

~~~json
{
  "source": "00abb4f0",
  "target": "Stack[-0x20f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb4f4`](#insn-00abb4f4)

~~~json
{
  "source": "00abb4f4",
  "target": "Stack[-0x20b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb500`](#insn-00abb500)

~~~json
{
  "source": "00abb500",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb510`](#insn-00abb510)

~~~json
{
  "source": "00abb510",
  "target": "0046ff30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb524`](#insn-00abb524)

~~~json
{
  "source": "00abb524",
  "target": "00ab1128",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb528`](#insn-00abb528)

~~~json
{
  "source": "00abb528",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb530`](#insn-00abb530)

~~~json
{
  "source": "00abb530",
  "target": "00abb554",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb534`](#insn-00abb534)

~~~json
{
  "source": "00abb534",
  "target": "Stack[-0x270]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb538`](#insn-00abb538)

~~~json
{
  "source": "00abb538",
  "target": "00abb564",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb53c`](#insn-00abb53c)

~~~json
{
  "source": "00abb53c",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb540`](#insn-00abb540)

~~~json
{
  "source": "00abb540",
  "target": "00abb574",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb544`](#insn-00abb544)

~~~json
{
  "source": "00abb544",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb548`](#insn-00abb548)

~~~json
{
  "source": "00abb548",
  "target": "00abb584",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb54c`](#insn-00abb54c)

~~~json
{
  "source": "00abb54c",
  "target": "00abb590",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb550`](#insn-00abb550)

~~~json
{
  "source": "00abb550",
  "target": "00abb5ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb554`](#insn-00abb554)

~~~json
{
  "source": "00abb554",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb558`](#insn-00abb558)

~~~json
{
  "source": "00abb558",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb55c`](#insn-00abb55c)

~~~json
{
  "source": "00abb55c",
  "target": "Stack[-0x270]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb560`](#insn-00abb560)

~~~json
{
  "source": "00abb560",
  "target": "00abb53c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb564`](#insn-00abb564)

~~~json
{
  "source": "00abb564",
  "target": "Stack[-0x260]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb568`](#insn-00abb568)

~~~json
{
  "source": "00abb568",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb56c`](#insn-00abb56c)

~~~json
{
  "source": "00abb56c",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb570`](#insn-00abb570)

~~~json
{
  "source": "00abb570",
  "target": "00abb544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb574`](#insn-00abb574)

~~~json
{
  "source": "00abb574",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb578`](#insn-00abb578)

~~~json
{
  "source": "00abb578",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb57c`](#insn-00abb57c)

~~~json
{
  "source": "00abb57c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb580`](#insn-00abb580)

~~~json
{
  "source": "00abb580",
  "target": "00abb54c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb584`](#insn-00abb584)

~~~json
{
  "source": "00abb584",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb588`](#insn-00abb588)

~~~json
{
  "source": "00abb588",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb58c`](#insn-00abb58c)

~~~json
{
  "source": "00abb58c",
  "target": "00abb5ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb59c`](#insn-00abb59c)

~~~json
{
  "source": "00abb59c",
  "target": "00abb5bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb5a0`](#insn-00abb5a0)

~~~json
{
  "source": "00abb5a0",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb5a4`](#insn-00abb5a4)

~~~json
{
  "source": "00abb5a4",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb5ac`](#insn-00abb5ac)

~~~json
{
  "source": "00abb5ac",
  "target": "002a4668",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4631",
  "offset": 55,
  "size": 64,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b5a294c616e64726f69642f636f",
  "capture_start": "002a4631",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb5b0`](#insn-00abb5b0)

~~~json
{
  "source": "00abb5b0",
  "target": "002a4678",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4671",
  "offset": 7,
  "size": 64,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b49294c616e64726f69642f636f",
  "capture_start": "002a4671",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb5b8`](#insn-00abb5b8)

~~~json
{
  "source": "00abb5b8",
  "target": "00abb5ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb5c4`](#insn-00abb5c4)

~~~json
{
  "source": "00abb5c4",
  "target": "00465394",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb5d4`](#insn-00abb5d4)

~~~json
{
  "source": "00abb5d4",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb5d8`](#insn-00abb5d8)

~~~json
{
  "source": "00abb5d8",
  "target": "002a4668",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4631",
  "offset": 55,
  "size": 64,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b5a294c616e64726f69642f636f",
  "capture_start": "002a4631",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb5dc`](#insn-00abb5dc)

~~~json
{
  "source": "00abb5dc",
  "target": "00abb5a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb5e0`](#insn-00abb5e0)

~~~json
{
  "source": "00abb5e0",
  "target": "002a4678",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4671",
  "offset": 7,
  "size": 64,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b49294c616e64726f69642f636f",
  "capture_start": "002a4671",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abb5e4`](#insn-00abb5e4)

~~~json
{
  "source": "00abb5e4",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb5e8`](#insn-00abb5e8)

~~~json
{
  "source": "00abb5e8",
  "target": "00abb5a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb5f4`](#insn-00abb5f4)

~~~json
{
  "source": "00abb5f4",
  "target": "00465780",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb604`](#insn-00abb604)

~~~json
{
  "source": "00abb604",
  "target": "00c1acc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1acc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abb608`](#insn-00abb608)

~~~json
{
  "source": "00abb608",
  "target": "00c1acc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1acc8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abb60c`](#insn-00abb60c)

~~~json
{
  "source": "00abb60c",
  "target": "00c13358",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13358",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abb614`](#insn-00abb614)

~~~json
{
  "source": "00abb614",
  "target": "00be8758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abb614`](#insn-00abb614)

~~~json
{
  "source": "00abb614",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb618`](#insn-00abb618)

~~~json
{
  "source": "00abb618",
  "target": "00c112f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c112f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abb618`](#insn-00abb618)

~~~json
{
  "source": "00abb618",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb61c`](#insn-00abb61c)

~~~json
{
  "source": "00abb61c",
  "target": "00c112e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c112e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c112e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abb620`](#insn-00abb620)

~~~json
{
  "source": "00abb620",
  "target": "00c13370",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13370",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abb624`](#insn-00abb624)

~~~json
{
  "source": "00abb624",
  "target": "00c11320",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11320",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abb62c`](#insn-00abb62c)

~~~json
{
  "source": "00abb62c",
  "target": "00c1acd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1acd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abb630`](#insn-00abb630)

~~~json
{
  "source": "00abb630",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb638`](#insn-00abb638)

~~~json
{
  "source": "00abb638",
  "target": "00c11078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11068",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00abb638`](#insn-00abb638)

~~~json
{
  "source": "00abb638",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb63c`](#insn-00abb63c)

~~~json
{
  "source": "00abb63c",
  "target": "00abb648",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb640`](#insn-00abb640)

~~~json
{
  "source": "00abb640",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb644`](#insn-00abb644)

~~~json
{
  "source": "00abb644",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb64c`](#insn-00abb64c)

~~~json
{
  "source": "00abb64c",
  "target": "00bdb050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb650`](#insn-00abb650)

~~~json
{
  "source": "00abb650",
  "target": "00c13360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13360",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abb658`](#insn-00abb658)

~~~json
{
  "source": "00abb658",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb664`](#insn-00abb664)

~~~json
{
  "source": "00abb664",
  "target": "00bdb070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb668`](#insn-00abb668)

~~~json
{
  "source": "00abb668",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb66c`](#insn-00abb66c)

~~~json
{
  "source": "00abb66c",
  "target": "00abb678",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb670`](#insn-00abb670)

~~~json
{
  "source": "00abb670",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb674`](#insn-00abb674)

~~~json
{
  "source": "00abb674",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb678`](#insn-00abb678)

~~~json
{
  "source": "00abb678",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb67c`](#insn-00abb67c)

~~~json
{
  "source": "00abb67c",
  "target": "00abb688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb680`](#insn-00abb680)

~~~json
{
  "source": "00abb680",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb684`](#insn-00abb684)

~~~json
{
  "source": "00abb684",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abb68c`](#insn-00abb68c)

~~~json
{
  "source": "00abb68c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb694`](#insn-00abb694)

~~~json
{
  "source": "00abb694",
  "target": "00abb820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb69c`](#insn-00abb69c)

~~~json
{
  "source": "00abb69c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb6a0`](#insn-00abb6a0)

~~~json
{
  "source": "00abb6a0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb6a4`](#insn-00abb6a4)

~~~json
{
  "source": "00abb6a4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb6a8`](#insn-00abb6a8)

~~~json
{
  "source": "00abb6a8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb6ac`](#insn-00abb6ac)

~~~json
{
  "source": "00abb6ac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abb820`](#insn-00abb820)

~~~json
{
  "source": "00abb820",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
