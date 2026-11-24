# 00b1aebc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0081.md#review-28ebcbc3c7aa8a1d86a6197393e09c0c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0043.md#review-28ebcbc3c7aa8a1d86a6197393e09c0c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "0501b9f357d7a4b140ad513cac6fd16f7ba04452716fee90caf1ec9adc17b15b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b1aebc",
        "00b1b713"
      ],
      [
        "00b1b880",
        "00b1b883"
      ]
    ],
    "bytes_sha256": "d99e86d992c3d0fd9b5d8cbaa3969f74df86599cd0d9d8520c62402a2881911a",
    "instruction_count": 535,
    "instruction_bytes": 2140,
    "body_bytes": 2140,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b1aebc"></a> `00b1aebc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00b1aec0"></a> `00b1aec0` | `fc 67 01 a9` | stp x28,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b1aec4"></a> `00b1aec4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b1aec8"></a> `00b1aec8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b1aecc"></a> `00b1aecc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b1aed0"></a> `00b1aed0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b1aed4"></a> `00b1aed4` | `ff 83 08 d1` | sub sp,sp,#0x220 | `FALL_THROUGH`
<a id="insn-00b1aed8"></a> `00b1aed8` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b1aedc"></a> `00b1aedc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b1aee0"></a> `00b1aee0` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1aee4"></a> `00b1aee4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b1aee8"></a> `00b1aee8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b1aeec"></a> `00b1aeec` | `dd b3 e5 97` | bl 0x00487e60 | `UNCONDITIONAL_CALL`
<a id="insn-00b1aef0"></a> `00b1aef0` | `48 0a 00 d0` | adrp x8,0xc64000 | `FALL_THROUGH`
<a id="insn-00b1aef4"></a> `00b1aef4` | `08 21 38 91` | add x8,x8,#0xe08 | `FALL_THROUGH`
<a id="insn-00b1aef8"></a> `00b1aef8` | `e8 63 00 f9` | str x8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b1aefc"></a> `00b1aefc` | `68 3a 51 91` | add x8,x19,#0x44e, LSL #12 | `FALL_THROUGH`
<a id="insn-00b1af00"></a> `00b1af00` | `00 21 07 91` | add x0,x8,#0x1c8 | `FALL_THROUGH`
<a id="insn-00b1af04"></a> `00b1af04` | `74 04 fe 97` | bl 0x00a9c0d4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1af08"></a> `00b1af08` | `48 04 80 52` | mov w8,#0x22 | `FALL_THROUGH`
<a id="insn-00b1af0c"></a> `00b1af0c` | `29 bd ff f0` | adrp x9,0x2c1000 | `FALL_THROUGH`
<a id="insn-00b1af10"></a> `00b1af10` | `29 b1 29 91` | add x9,x9,#0xa6c | `FALL_THROUGH`
<a id="insn-00b1af14"></a> `00b1af14` | `f6 43 02 91` | add x22,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00b1af18"></a> `00b1af18` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00b1af1c"></a> `00b1af1c` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1af20"></a> `00b1af20` | `c8 0e 80 52` | mov w8,#0x76 | `FALL_THROUGH`
<a id="insn-00b1af24"></a> `00b1af24` | `97 2d 8c 52` | mov w23,#0x616c | `FALL_THROUGH`
<a id="insn-00b1af28"></a> `00b1af28` | `ff 97 01 39` | strb wzr,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00b1af2c"></a> `00b1af2c` | `c8 12 01 78` | sturh w8,[x22, #0x11] | `FALL_THROUGH`
<a id="insn-00b1af30"></a> `00b1af30` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00b1af34"></a> `00b1af34` | `d7 ed ac 72` | movk w23,#0x676e, LSL #16 | `FALL_THROUGH`
<a id="insn-00b1af38"></a> `00b1af38` | `c0 12 80 3c` | stur q0,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00b1af3c"></a> `00b1af3c` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1af40"></a> `00b1af40` | `f7 13 06 b8` | stur w23,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00b1af44"></a> `00b1af44` | `e8 e3 01 91` | add x8,sp,#0x78 | `FALL_THROUGH`
<a id="insn-00b1af48"></a> `00b1af48` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b1af4c"></a> `00b1af4c` | `d2 c7 e5 97` | bl 0x0048ce94 | `UNCONDITIONAL_CALL`
<a id="insn-00b1af50"></a> `00b1af50` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1af54"></a> `00b1af54` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00b1af58"></a> `00b1af58` | `e1 e3 01 91` | add x1,sp,#0x78 | `FALL_THROUGH`
<a id="insn-00b1af5c"></a> `00b1af5c` | `bb df e5 97` | bl 0x00492e48 | `UNCONDITIONAL_CALL`
<a id="insn-00b1af60"></a> `00b1af60` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1af64"></a> `00b1af64` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1af68"></a> `00b1af68` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00b1af6c"></a> `00b1af6c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00b1af70"></a> `00b1af70` | `86 d8 ff 97` | bl 0x00b11188 | `UNCONDITIONAL_CALL`
<a id="insn-00b1af74"></a> `00b1af74` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00b1af78"></a> `00b1af78` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00b1af7c"></a> `00b1af7c` | `28 01 00 37` | tbnz w8,#0x0,0x00b1afa0 | `CONDITIONAL_JUMP`
<a id="insn-00b1af80"></a> `00b1af80` | `e8 e3 41 39` | ldrb w8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00b1af84"></a> `00b1af84` | `68 01 00 37` | tbnz w8,#0x0,0x00b1afb0 | `CONDITIONAL_JUMP`
<a id="insn-00b1af88"></a> `00b1af88` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1af8c"></a> `00b1af8c` | `a8 01 00 37` | tbnz w8,#0x0,0x00b1afc0 | `CONDITIONAL_JUMP`
<a id="insn-00b1af90"></a> `00b1af90` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1af94"></a> `00b1af94` | `e8 01 00 37` | tbnz w8,#0x0,0x00b1afd0 | `CONDITIONAL_JUMP`
<a id="insn-00b1af98"></a> `00b1af98` | `34 02 00 37` | tbnz w20,#0x0,0x00b1afdc | `CONDITIONAL_JUMP`
<a id="insn-00b1af9c"></a> `00b1af9c` | `7f 00 00 14` | b 0x00b1b198 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1afa0"></a> `00b1afa0` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1afa4"></a> `00b1afa4` | `f7 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1afa8"></a> `00b1afa8` | `e8 e3 41 39` | ldrb w8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00b1afac"></a> `00b1afac` | `e8 fe 07 36` | tbz w8,#0x0,0x00b1af88 | `CONDITIONAL_JUMP`
<a id="insn-00b1afb0"></a> `00b1afb0` | `e0 47 40 f9` | ldr x0,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00b1afb4"></a> `00b1afb4` | `f3 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1afb8"></a> `00b1afb8` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1afbc"></a> `00b1afbc` | `a8 fe 07 36` | tbz w8,#0x0,0x00b1af90 | `CONDITIONAL_JUMP`
<a id="insn-00b1afc0"></a> `00b1afc0` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b1afc4"></a> `00b1afc4` | `ef f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1afc8"></a> `00b1afc8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1afcc"></a> `00b1afcc` | `68 fe 07 36` | tbz w8,#0x0,0x00b1af98 | `CONDITIONAL_JUMP`
<a id="insn-00b1afd0"></a> `00b1afd0` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b1afd4"></a> `00b1afd4` | `eb f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1afd8"></a> `00b1afd8` | `14 0e 00 36` | tbz w20,#0x0,0x00b1b198 | `CONDITIONAL_JUMP`
<a id="insn-00b1afdc"></a> `00b1afdc` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1afe0"></a> `00b1afe0` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00b1afe4"></a> `00b1afe4` | `b2 b4 e5 97` | bl 0x004882ac | `UNCONDITIONAL_CALL`
<a id="insn-00b1afe8"></a> `00b1afe8` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1afec"></a> `00b1afec` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1aff0"></a> `00b1aff0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b1aff4"></a> `00b1aff4` | `ac b2 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1aff8"></a> `00b1aff8` | `68 be 4c 91` | add x8,x19,#0x32f, LSL #12 | `FALL_THROUGH`
<a id="insn-00b1affc"></a> `00b1affc` | `14 61 1b 91` | add x20,x8,#0x6d8 | `FALL_THROUGH`
<a id="insn-00b1b000"></a> `00b1b000` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00b1b004"></a> `00b1b004` | `68 00 00 36` | tbz w8,#0x0,0x00b1b010 | `CONDITIONAL_JUMP`
<a id="insn-00b1b008"></a> `00b1b008` | `80 0a 40 f9` | ldr x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b00c"></a> `00b1b00c` | `dd f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b010"></a> `00b1b010` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b014"></a> `00b1b014` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b018"></a> `00b1b018` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00b1b01c"></a> `00b1b01c` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b020"></a> `00b1b020` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b024"></a> `00b1b024` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b028"></a> `00b1b028` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00b1b02c"></a> `00b1b02c` | `9e b2 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b030"></a> `00b1b030` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00b1b034"></a> `00b1b034` | `08 8f 41 38` | ldrb w8,[x24, #0x18]! | `FALL_THROUGH`
<a id="insn-00b1b038"></a> `00b1b038` | `68 00 00 36` | tbz w8,#0x0,0x00b1b044 | `CONDITIONAL_JUMP`
<a id="insn-00b1b03c"></a> `00b1b03c` | `80 16 40 f9` | ldr x0,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b1b040"></a> `00b1b040` | `d0 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b044"></a> `00b1b044` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b048"></a> `00b1b048` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b04c"></a> `00b1b04c` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00b1b050"></a> `00b1b050` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b054"></a> `00b1b054` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b058"></a> `00b1b058` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b05c"></a> `00b1b05c` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00b1b060"></a> `00b1b060` | `91 b2 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b064"></a> `00b1b064` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00b1b068"></a> `00b1b068` | `08 0f 43 38` | ldrb w8,[x24, #0x30]! | `FALL_THROUGH`
<a id="insn-00b1b06c"></a> `00b1b06c` | `68 00 00 36` | tbz w8,#0x0,0x00b1b078 | `CONDITIONAL_JUMP`
<a id="insn-00b1b070"></a> `00b1b070` | `80 22 40 f9` | ldr x0,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00b1b074"></a> `00b1b074` | `c3 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b078"></a> `00b1b078` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b07c"></a> `00b1b07c` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b080"></a> `00b1b080` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00b1b084"></a> `00b1b084` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b088"></a> `00b1b088` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b08c"></a> `00b1b08c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b090"></a> `00b1b090` | `61 00 80 52` | mov w1,#0x3 | `FALL_THROUGH`
<a id="insn-00b1b094"></a> `00b1b094` | `84 b2 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b098"></a> `00b1b098` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00b1b09c"></a> `00b1b09c` | `08 8f 44 38` | ldrb w8,[x24, #0x48]! | `FALL_THROUGH`
<a id="insn-00b1b0a0"></a> `00b1b0a0` | `68 00 00 36` | tbz w8,#0x0,0x00b1b0ac | `CONDITIONAL_JUMP`
<a id="insn-00b1b0a4"></a> `00b1b0a4` | `80 2e 40 f9` | ldr x0,[x20, #0x58] | `FALL_THROUGH`
<a id="insn-00b1b0a8"></a> `00b1b0a8` | `b6 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b0ac"></a> `00b1b0ac` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b0b0"></a> `00b1b0b0` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b0b4"></a> `00b1b0b4` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00b1b0b8"></a> `00b1b0b8` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b0bc"></a> `00b1b0bc` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b0c0"></a> `00b1b0c0` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00b1b0c4"></a> `00b1b0c4` | `7a b4 e5 97` | bl 0x004882ac | `UNCONDITIONAL_CALL`
<a id="insn-00b1b0c8"></a> `00b1b0c8` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b0cc"></a> `00b1b0cc` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b0d0"></a> `00b1b0d0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b1b0d4"></a> `00b1b0d4` | `74 b2 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b0d8"></a> `00b1b0d8` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00b1b0dc"></a> `00b1b0dc` | `08 0f 46 38` | ldrb w8,[x24, #0x60]! | `FALL_THROUGH`
<a id="insn-00b1b0e0"></a> `00b1b0e0` | `68 00 00 36` | tbz w8,#0x0,0x00b1b0ec | `CONDITIONAL_JUMP`
<a id="insn-00b1b0e4"></a> `00b1b0e4` | `80 3a 40 f9` | ldr x0,[x20, #0x70] | `FALL_THROUGH`
<a id="insn-00b1b0e8"></a> `00b1b0e8` | `a6 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b0ec"></a> `00b1b0ec` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b0f0"></a> `00b1b0f0` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b0f4"></a> `00b1b0f4` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00b1b0f8"></a> `00b1b0f8` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b0fc"></a> `00b1b0fc` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b100"></a> `00b1b100` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b104"></a> `00b1b104` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00b1b108"></a> `00b1b108` | `67 b2 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b10c"></a> `00b1b10c` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00b1b110"></a> `00b1b110` | `08 8f 47 38` | ldrb w8,[x24, #0x78]! | `FALL_THROUGH`
<a id="insn-00b1b114"></a> `00b1b114` | `68 00 00 36` | tbz w8,#0x0,0x00b1b120 | `CONDITIONAL_JUMP`
<a id="insn-00b1b118"></a> `00b1b118` | `80 46 40 f9` | ldr x0,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00b1b11c"></a> `00b1b11c` | `99 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b120"></a> `00b1b120` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b124"></a> `00b1b124` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b128"></a> `00b1b128` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00b1b12c"></a> `00b1b12c` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b130"></a> `00b1b130` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b134"></a> `00b1b134` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b138"></a> `00b1b138` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00b1b13c"></a> `00b1b13c` | `5a b2 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b140"></a> `00b1b140` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00b1b144"></a> `00b1b144` | `08 0f 49 38` | ldrb w8,[x24, #0x90]! | `FALL_THROUGH`
<a id="insn-00b1b148"></a> `00b1b148` | `68 00 00 36` | tbz w8,#0x0,0x00b1b154 | `CONDITIONAL_JUMP`
<a id="insn-00b1b14c"></a> `00b1b14c` | `80 52 40 f9` | ldr x0,[x20, #0xa0] | `FALL_THROUGH`
<a id="insn-00b1b150"></a> `00b1b150` | `8c f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b154"></a> `00b1b154` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b158"></a> `00b1b158` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b15c"></a> `00b1b15c` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00b1b160"></a> `00b1b160` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b164"></a> `00b1b164` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b168"></a> `00b1b168` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b16c"></a> `00b1b16c` | `61 00 80 52` | mov w1,#0x3 | `FALL_THROUGH`
<a id="insn-00b1b170"></a> `00b1b170` | `4d b2 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b174"></a> `00b1b174` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00b1b178"></a> `00b1b178` | `08 8f 4a 38` | ldrb w8,[x24, #0xa8]! | `FALL_THROUGH`
<a id="insn-00b1b17c"></a> `00b1b17c` | `68 00 00 36` | tbz w8,#0x0,0x00b1b188 | `CONDITIONAL_JUMP`
<a id="insn-00b1b180"></a> `00b1b180` | `80 5e 40 f9` | ldr x0,[x20, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b184"></a> `00b1b184` | `7f f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b188"></a> `00b1b188` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b18c"></a> `00b1b18c` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b190"></a> `00b1b190` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00b1b194"></a> `00b1b194` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b198"></a> `00b1b198` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b19c"></a> `00b1b19c` | `3f b5 e5 97` | bl 0x00488698 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b1a0"></a> `00b1b1a0` | `49 bc ff f0` | adrp x9,0x2a6000 | `FALL_THROUGH`
<a id="insn-00b1b1a4"></a> `00b1b1a4` | `29 d5 3d 91` | add x9,x9,#0xf75 | `FALL_THROUGH`
<a id="insn-00b1b1a8"></a> `00b1b1a8` | `48 02 80 52` | mov w8,#0x12 | `FALL_THROUGH`
<a id="insn-00b1b1ac"></a> `00b1b1ac` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00b1b1b0"></a> `00b1b1b0` | `ca 0e 80 52` | mov w10,#0x76 | `FALL_THROUGH`
<a id="insn-00b1b1b4"></a> `00b1b1b4` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b1b8"></a> `00b1b1b8` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00b1b1bc"></a> `00b1b1bc` | `ca 92 00 78` | sturh w10,[x22, #0x9] | `FALL_THROUGH`
<a id="insn-00b1b1c0"></a> `00b1b1c0` | `c9 12 00 f8` | stur x9,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00b1b1c4"></a> `00b1b1c4` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b1c8"></a> `00b1b1c8` | `f7 13 06 b8` | stur w23,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00b1b1cc"></a> `00b1b1cc` | `ff 97 01 39` | strb wzr,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00b1b1d0"></a> `00b1b1d0` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00b1b1d4"></a> `00b1b1d4` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b1b1d8"></a> `00b1b1d8` | `2f c7 e5 97` | bl 0x0048ce94 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b1dc"></a> `00b1b1dc` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b1e0"></a> `00b1b1e0` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00b1b1e4"></a> `00b1b1e4` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00b1b1e8"></a> `00b1b1e8` | `18 df e5 97` | bl 0x00492e48 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b1ec"></a> `00b1b1ec` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b1f0"></a> `00b1b1f0` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b1f4"></a> `00b1b1f4` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00b1b1f8"></a> `00b1b1f8` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00b1b1fc"></a> `00b1b1fc` | `e3 d7 ff 97` | bl 0x00b11188 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b200"></a> `00b1b200` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00b1b204"></a> `00b1b204` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00b1b208"></a> `00b1b208` | `08 09 00 37` | tbnz w8,#0x0,0x00b1b328 | `CONDITIONAL_JUMP`
<a id="insn-00b1b20c"></a> `00b1b20c` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00b1b210"></a> `00b1b210` | `48 09 00 37` | tbnz w8,#0x0,0x00b1b338 | `CONDITIONAL_JUMP`
<a id="insn-00b1b214"></a> `00b1b214` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b218"></a> `00b1b218` | `88 09 00 37` | tbnz w8,#0x0,0x00b1b348 | `CONDITIONAL_JUMP`
<a id="insn-00b1b21c"></a> `00b1b21c` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b220"></a> `00b1b220` | `68 00 00 36` | tbz w8,#0x0,0x00b1b22c | `CONDITIONAL_JUMP`
<a id="insn-00b1b224"></a> `00b1b224` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b1b228"></a> `00b1b228` | `56 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b22c"></a> `00b1b22c` | `68 9a 4a 91` | add x8,x19,#0x2a6, LSL #12 | `FALL_THROUGH`
<a id="insn-00b1b230"></a> `00b1b230` | `18 a1 19 91` | add x24,x8,#0x668 | `FALL_THROUGH`
<a id="insn-00b1b234"></a> `00b1b234` | `f4 02 00 36` | tbz w20,#0x0,0x00b1b290 | `CONDITIONAL_JUMP`
<a id="insn-00b1b238"></a> `00b1b238` | `34 09 80 52` | mov w20,#0x49 | `FALL_THROUGH`
<a id="insn-00b1b23c"></a> `00b1b23c` | `f9 03 18 aa` | mov x25,x24 | `FALL_THROUGH`
<a id="insn-00b1b240"></a> `00b1b240` | `08 00 00 14` | b 0x00b1b260 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b244"></a> `00b1b244` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b248"></a> `00b1b248` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b24c"></a> `00b1b24c` | `94 06 00 f1` | subs x20,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00b1b250"></a> `00b1b250` | `20 03 80 3d` | str q0,[x25] | `FALL_THROUGH`
<a id="insn-00b1b254"></a> `00b1b254` | `28 0b 00 f9` | str x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b258"></a> `00b1b258` | `39 63 00 91` | add x25,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00b1b25c"></a> `00b1b25c` | `a0 01 00 54` | b.eq 0x00b1b290 | `CONDITIONAL_JUMP`
<a id="insn-00b1b260"></a> `00b1b260` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b264"></a> `00b1b264` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00b1b268"></a> `00b1b268` | `11 b4 e5 97` | bl 0x004882ac | `UNCONDITIONAL_CALL`
<a id="insn-00b1b26c"></a> `00b1b26c` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b270"></a> `00b1b270` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b274"></a> `00b1b274` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b1b278"></a> `00b1b278` | `0b b2 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b27c"></a> `00b1b27c` | `28 03 40 39` | ldrb w8,[x25] | `FALL_THROUGH`
<a id="insn-00b1b280"></a> `00b1b280` | `28 fe 07 36` | tbz w8,#0x0,0x00b1b244 | `CONDITIONAL_JUMP`
<a id="insn-00b1b284"></a> `00b1b284` | `20 0b 40 f9` | ldr x0,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b288"></a> `00b1b288` | `3e f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b28c"></a> `00b1b28c` | `ee ff ff 17` | b 0x00b1b244 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b290"></a> `00b1b290` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b294"></a> `00b1b294` | `01 b5 e5 97` | bl 0x00488698 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b298"></a> `00b1b298` | `09 bd ff f0` | adrp x9,0x2be000 | `FALL_THROUGH`
<a id="insn-00b1b29c"></a> `00b1b29c` | `29 99 0f 91` | add x9,x9,#0x3e6 | `FALL_THROUGH`
<a id="insn-00b1b2a0"></a> `00b1b2a0` | `c8 03 80 52` | mov w8,#0x1e | `FALL_THROUGH`
<a id="insn-00b1b2a4"></a> `00b1b2a4` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00b1b2a8"></a> `00b1b2a8` | `29 71 40 f8` | ldur x9,[x9, #0x7] | `FALL_THROUGH`
<a id="insn-00b1b2ac"></a> `00b1b2ac` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b2b0"></a> `00b1b2b0` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00b1b2b4"></a> `00b1b2b4` | `ff 83 02 39` | strb wzr,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b1b2b8"></a> `00b1b2b8` | `ca 12 00 f8` | stur x10,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00b1b2bc"></a> `00b1b2bc` | `e9 4f 00 f9` | str x9,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00b1b2c0"></a> `00b1b2c0` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b2c4"></a> `00b1b2c4` | `f7 13 06 b8` | stur w23,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00b1b2c8"></a> `00b1b2c8` | `ff 97 01 39` | strb wzr,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00b1b2cc"></a> `00b1b2cc` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b1b2d0"></a> `00b1b2d0` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b1b2d4"></a> `00b1b2d4` | `f0 c6 e5 97` | bl 0x0048ce94 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b2d8"></a> `00b1b2d8` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b2dc"></a> `00b1b2dc` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00b1b2e0"></a> `00b1b2e0` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b1b2e4"></a> `00b1b2e4` | `d9 de e5 97` | bl 0x00492e48 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b2e8"></a> `00b1b2e8` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b2ec"></a> `00b1b2ec` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b2f0"></a> `00b1b2f0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00b1b2f4"></a> `00b1b2f4` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00b1b2f8"></a> `00b1b2f8` | `a4 d7 ff 97` | bl 0x00b11188 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b2fc"></a> `00b1b2fc` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00b1b300"></a> `00b1b300` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00b1b304"></a> `00b1b304` | `c8 02 00 37` | tbnz w8,#0x0,0x00b1b35c | `CONDITIONAL_JUMP`
<a id="insn-00b1b308"></a> `00b1b308` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b1b30c"></a> `00b1b30c` | `08 03 00 37` | tbnz w8,#0x0,0x00b1b36c | `CONDITIONAL_JUMP`
<a id="insn-00b1b310"></a> `00b1b310` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b314"></a> `00b1b314` | `48 03 00 37` | tbnz w8,#0x0,0x00b1b37c | `CONDITIONAL_JUMP`
<a id="insn-00b1b318"></a> `00b1b318` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b31c"></a> `00b1b31c` | `88 03 00 37` | tbnz w8,#0x0,0x00b1b38c | `CONDITIONAL_JUMP`
<a id="insn-00b1b320"></a> `00b1b320` | `d4 03 00 37` | tbnz w20,#0x0,0x00b1b398 | `CONDITIONAL_JUMP`
<a id="insn-00b1b324"></a> `00b1b324` | `33 00 00 14` | b 0x00b1b3f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b328"></a> `00b1b328` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b32c"></a> `00b1b32c` | `15 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b330"></a> `00b1b330` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00b1b334"></a> `00b1b334` | `08 f7 07 36` | tbz w8,#0x0,0x00b1b214 | `CONDITIONAL_JUMP`
<a id="insn-00b1b338"></a> `00b1b338` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00b1b33c"></a> `00b1b33c` | `11 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b340"></a> `00b1b340` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b344"></a> `00b1b344` | `c8 f6 07 36` | tbz w8,#0x0,0x00b1b21c | `CONDITIONAL_JUMP`
<a id="insn-00b1b348"></a> `00b1b348` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b1b34c"></a> `00b1b34c` | `0d f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b350"></a> `00b1b350` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b354"></a> `00b1b354` | `88 f6 07 37` | tbnz w8,#0x0,0x00b1b224 | `CONDITIONAL_JUMP`
<a id="insn-00b1b358"></a> `00b1b358` | `b5 ff ff 17` | b 0x00b1b22c | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b35c"></a> `00b1b35c` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b360"></a> `00b1b360` | `08 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b364"></a> `00b1b364` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b1b368"></a> `00b1b368` | `48 fd 07 36` | tbz w8,#0x0,0x00b1b310 | `CONDITIONAL_JUMP`
<a id="insn-00b1b36c"></a> `00b1b36c` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b1b370"></a> `00b1b370` | `04 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b374"></a> `00b1b374` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b378"></a> `00b1b378` | `08 fd 07 36` | tbz w8,#0x0,0x00b1b318 | `CONDITIONAL_JUMP`
<a id="insn-00b1b37c"></a> `00b1b37c` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b1b380"></a> `00b1b380` | `00 f3 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b384"></a> `00b1b384` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b388"></a> `00b1b388` | `c8 fc 07 36` | tbz w8,#0x0,0x00b1b320 | `CONDITIONAL_JUMP`
<a id="insn-00b1b38c"></a> `00b1b38c` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b1b390"></a> `00b1b390` | `fc f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b394"></a> `00b1b394` | `f4 02 00 36` | tbz w20,#0x0,0x00b1b3f0 | `CONDITIONAL_JUMP`
<a id="insn-00b1b398"></a> `00b1b398` | `14 63 1b 91` | add x20,x24,#0x6d8 | `FALL_THROUGH`
<a id="insn-00b1b39c"></a> `00b1b39c` | `39 09 80 52` | mov w25,#0x49 | `FALL_THROUGH`
<a id="insn-00b1b3a0"></a> `00b1b3a0` | `08 00 00 14` | b 0x00b1b3c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b3a4"></a> `00b1b3a4` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b3a8"></a> `00b1b3a8` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b3ac"></a> `00b1b3ac` | `39 07 00 f1` | subs x25,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00b1b3b0"></a> `00b1b3b0` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00b1b3b4"></a> `00b1b3b4` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b3b8"></a> `00b1b3b8` | `94 62 00 91` | add x20,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00b1b3bc"></a> `00b1b3bc` | `a0 01 00 54` | b.eq 0x00b1b3f0 | `CONDITIONAL_JUMP`
<a id="insn-00b1b3c0"></a> `00b1b3c0` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b3c4"></a> `00b1b3c4` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00b1b3c8"></a> `00b1b3c8` | `b9 b3 e5 97` | bl 0x004882ac | `UNCONDITIONAL_CALL`
<a id="insn-00b1b3cc"></a> `00b1b3cc` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b3d0"></a> `00b1b3d0` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b3d4"></a> `00b1b3d4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b1b3d8"></a> `00b1b3d8` | `b3 b1 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b3dc"></a> `00b1b3dc` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00b1b3e0"></a> `00b1b3e0` | `28 fe 07 36` | tbz w8,#0x0,0x00b1b3a4 | `CONDITIONAL_JUMP`
<a id="insn-00b1b3e4"></a> `00b1b3e4` | `80 0a 40 f9` | ldr x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b3e8"></a> `00b1b3e8` | `e6 f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b3ec"></a> `00b1b3ec` | `ee ff ff 17` | b 0x00b1b3a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b3f0"></a> `00b1b3f0` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b3f4"></a> `00b1b3f4` | `a9 b4 e5 97` | bl 0x00488698 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b3f8"></a> `00b1b3f8` | `a9 bc ff 90` | adrp x9,0x2af000 | `FALL_THROUGH`
<a id="insn-00b1b3fc"></a> `00b1b3fc` | `29 89 08 91` | add x9,x9,#0x222 | `FALL_THROUGH`
<a id="insn-00b1b400"></a> `00b1b400` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00b1b404"></a> `00b1b404` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00b1b408"></a> `00b1b408` | `6a ce 8e 52` | mov w10,#0x7673 | `FALL_THROUGH`
<a id="insn-00b1b40c"></a> `00b1b40c` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b410"></a> `00b1b410` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00b1b414"></a> `00b1b414` | `ca 92 00 78` | sturh w10,[x22, #0x9] | `FALL_THROUGH`
<a id="insn-00b1b418"></a> `00b1b418` | `c9 12 00 f8` | stur x9,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00b1b41c"></a> `00b1b41c` | `ff 6f 02 39` | strb wzr,[sp, #0x9b] | `FALL_THROUGH`
<a id="insn-00b1b420"></a> `00b1b420` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b424"></a> `00b1b424` | `f7 13 06 b8` | stur w23,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00b1b428"></a> `00b1b428` | `ff 97 01 39` | strb wzr,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00b1b42c"></a> `00b1b42c` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b1b430"></a> `00b1b430` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b1b434"></a> `00b1b434` | `98 c6 e5 97` | bl 0x0048ce94 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b438"></a> `00b1b438` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b43c"></a> `00b1b43c` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00b1b440"></a> `00b1b440` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b1b444"></a> `00b1b444` | `81 de e5 97` | bl 0x00492e48 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b448"></a> `00b1b448` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b44c"></a> `00b1b44c` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b450"></a> `00b1b450` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00b1b454"></a> `00b1b454` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00b1b458"></a> `00b1b458` | `4c d7 ff 97` | bl 0x00b11188 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b45c"></a> `00b1b45c` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00b1b460"></a> `00b1b460` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00b1b464"></a> `00b1b464` | `28 01 00 37` | tbnz w8,#0x0,0x00b1b488 | `CONDITIONAL_JUMP`
<a id="insn-00b1b468"></a> `00b1b468` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b46c"></a> `00b1b46c` | `68 01 00 37` | tbnz w8,#0x0,0x00b1b498 | `CONDITIONAL_JUMP`
<a id="insn-00b1b470"></a> `00b1b470` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b474"></a> `00b1b474` | `a8 01 00 37` | tbnz w8,#0x0,0x00b1b4a8 | `CONDITIONAL_JUMP`
<a id="insn-00b1b478"></a> `00b1b478` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b47c"></a> `00b1b47c` | `e8 01 00 37` | tbnz w8,#0x0,0x00b1b4b8 | `CONDITIONAL_JUMP`
<a id="insn-00b1b480"></a> `00b1b480` | `34 02 00 37` | tbnz w20,#0x0,0x00b1b4c4 | `CONDITIONAL_JUMP`
<a id="insn-00b1b484"></a> `00b1b484` | `26 00 00 14` | b 0x00b1b51c | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b488"></a> `00b1b488` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b48c"></a> `00b1b48c` | `bd f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b490"></a> `00b1b490` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b494"></a> `00b1b494` | `e8 fe 07 36` | tbz w8,#0x0,0x00b1b470 | `CONDITIONAL_JUMP`
<a id="insn-00b1b498"></a> `00b1b498` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b1b49c"></a> `00b1b49c` | `b9 f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b4a0"></a> `00b1b4a0` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b4a4"></a> `00b1b4a4` | `a8 fe 07 36` | tbz w8,#0x0,0x00b1b478 | `CONDITIONAL_JUMP`
<a id="insn-00b1b4a8"></a> `00b1b4a8` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b1b4ac"></a> `00b1b4ac` | `b5 f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b4b0"></a> `00b1b4b0` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b4b4"></a> `00b1b4b4` | `68 fe 07 36` | tbz w8,#0x0,0x00b1b480 | `CONDITIONAL_JUMP`
<a id="insn-00b1b4b8"></a> `00b1b4b8` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b1b4bc"></a> `00b1b4bc` | `b1 f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b4c0"></a> `00b1b4c0` | `f4 02 00 36` | tbz w20,#0x0,0x00b1b51c | `CONDITIONAL_JUMP`
<a id="insn-00b1b4c4"></a> `00b1b4c4` | `14 c3 36 91` | add x20,x24,#0xdb0 | `FALL_THROUGH`
<a id="insn-00b1b4c8"></a> `00b1b4c8` | `b8 09 80 52` | mov w24,#0x4d | `FALL_THROUGH`
<a id="insn-00b1b4cc"></a> `00b1b4cc` | `08 00 00 14` | b 0x00b1b4ec | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b4d0"></a> `00b1b4d0` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b4d4"></a> `00b1b4d4` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b4d8"></a> `00b1b4d8` | `18 07 00 f1` | subs x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00b1b4dc"></a> `00b1b4dc` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00b1b4e0"></a> `00b1b4e0` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b4e4"></a> `00b1b4e4` | `94 62 00 91` | add x20,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00b1b4e8"></a> `00b1b4e8` | `a0 01 00 54` | b.eq 0x00b1b51c | `CONDITIONAL_JUMP`
<a id="insn-00b1b4ec"></a> `00b1b4ec` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b4f0"></a> `00b1b4f0` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00b1b4f4"></a> `00b1b4f4` | `6e b3 e5 97` | bl 0x004882ac | `UNCONDITIONAL_CALL`
<a id="insn-00b1b4f8"></a> `00b1b4f8` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b4fc"></a> `00b1b4fc` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b500"></a> `00b1b500` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b1b504"></a> `00b1b504` | `68 b1 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b508"></a> `00b1b508` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00b1b50c"></a> `00b1b50c` | `28 fe 07 36` | tbz w8,#0x0,0x00b1b4d0 | `CONDITIONAL_JUMP`
<a id="insn-00b1b510"></a> `00b1b510` | `80 0a 40 f9` | ldr x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b514"></a> `00b1b514` | `9b f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b518"></a> `00b1b518` | `ee ff ff 17` | b 0x00b1b4d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b51c"></a> `00b1b51c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b520"></a> `00b1b520` | `5e b4 e5 97` | bl 0x00488698 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b524"></a> `00b1b524` | `29 bc ff d0` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00b1b528"></a> `00b1b528` | `29 dd 22 91` | add x9,x9,#0x8b7 | `FALL_THROUGH`
<a id="insn-00b1b52c"></a> `00b1b52c` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00b1b530"></a> `00b1b530` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00b1b534"></a> `00b1b534` | `6a ce 8e 52` | mov w10,#0x7673 | `FALL_THROUGH`
<a id="insn-00b1b538"></a> `00b1b538` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b53c"></a> `00b1b53c` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00b1b540"></a> `00b1b540` | `ca 92 00 78` | sturh w10,[x22, #0x9] | `FALL_THROUGH`
<a id="insn-00b1b544"></a> `00b1b544` | `c9 12 00 f8` | stur x9,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00b1b548"></a> `00b1b548` | `ff 6f 02 39` | strb wzr,[sp, #0x9b] | `FALL_THROUGH`
<a id="insn-00b1b54c"></a> `00b1b54c` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b550"></a> `00b1b550` | `f7 13 06 b8` | stur w23,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00b1b554"></a> `00b1b554` | `ff 97 01 39` | strb wzr,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00b1b558"></a> `00b1b558` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00b1b55c"></a> `00b1b55c` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b1b560"></a> `00b1b560` | `4d c6 e5 97` | bl 0x0048ce94 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b564"></a> `00b1b564` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b568"></a> `00b1b568` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00b1b56c"></a> `00b1b56c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00b1b570"></a> `00b1b570` | `36 de e5 97` | bl 0x00492e48 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b574"></a> `00b1b574` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b578"></a> `00b1b578` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b57c"></a> `00b1b57c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00b1b580"></a> `00b1b580` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00b1b584"></a> `00b1b584` | `01 d7 ff 97` | bl 0x00b11188 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b588"></a> `00b1b588` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00b1b58c"></a> `00b1b58c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00b1b590"></a> `00b1b590` | `28 01 00 37` | tbnz w8,#0x0,0x00b1b5b4 | `CONDITIONAL_JUMP`
<a id="insn-00b1b594"></a> `00b1b594` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b1b598"></a> `00b1b598` | `68 01 00 37` | tbnz w8,#0x0,0x00b1b5c4 | `CONDITIONAL_JUMP`
<a id="insn-00b1b59c"></a> `00b1b59c` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b5a0"></a> `00b1b5a0` | `a8 01 00 37` | tbnz w8,#0x0,0x00b1b5d4 | `CONDITIONAL_JUMP`
<a id="insn-00b1b5a4"></a> `00b1b5a4` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b5a8"></a> `00b1b5a8` | `e8 01 00 37` | tbnz w8,#0x0,0x00b1b5e4 | `CONDITIONAL_JUMP`
<a id="insn-00b1b5ac"></a> `00b1b5ac` | `34 02 00 37` | tbnz w20,#0x0,0x00b1b5f0 | `CONDITIONAL_JUMP`
<a id="insn-00b1b5b0"></a> `00b1b5b0` | `27 00 00 14` | b 0x00b1b64c | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b5b4"></a> `00b1b5b4` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b5b8"></a> `00b1b5b8` | `72 f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b5bc"></a> `00b1b5bc` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b1b5c0"></a> `00b1b5c0` | `e8 fe 07 36` | tbz w8,#0x0,0x00b1b59c | `CONDITIONAL_JUMP`
<a id="insn-00b1b5c4"></a> `00b1b5c4` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b5c8"></a> `00b1b5c8` | `6e f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b5cc"></a> `00b1b5cc` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1b5d0"></a> `00b1b5d0` | `a8 fe 07 36` | tbz w8,#0x0,0x00b1b5a4 | `CONDITIONAL_JUMP`
<a id="insn-00b1b5d4"></a> `00b1b5d4` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b1b5d8"></a> `00b1b5d8` | `6a f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b5dc"></a> `00b1b5dc` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1b5e0"></a> `00b1b5e0` | `68 fe 07 36` | tbz w8,#0x0,0x00b1b5ac | `CONDITIONAL_JUMP`
<a id="insn-00b1b5e4"></a> `00b1b5e4` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b1b5e8"></a> `00b1b5e8` | `66 f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b5ec"></a> `00b1b5ec` | `14 03 00 36` | tbz w20,#0x0,0x00b1b64c | `CONDITIONAL_JUMP`
<a id="insn-00b1b5f0"></a> `00b1b5f0` | `68 9e 4a 91` | add x8,x19,#0x2a7, LSL #12 | `FALL_THROUGH`
<a id="insn-00b1b5f4"></a> `00b1b5f4` | `b4 09 80 52` | mov w20,#0x4d | `FALL_THROUGH`
<a id="insn-00b1b5f8"></a> `00b1b5f8` | `13 41 2d 91` | add x19,x8,#0xb50 | `FALL_THROUGH`
<a id="insn-00b1b5fc"></a> `00b1b5fc` | `08 00 00 14` | b 0x00b1b61c | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b600"></a> `00b1b600` | `c0 82 c1 3c` | ldur q0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b604"></a> `00b1b604` | `e8 5f 40 f9` | ldr x8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00b1b608"></a> `00b1b608` | `94 06 00 f1` | subs x20,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00b1b60c"></a> `00b1b60c` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00b1b610"></a> `00b1b610` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b614"></a> `00b1b614` | `73 62 00 91` | add x19,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00b1b618"></a> `00b1b618` | `a0 01 00 54` | b.eq 0x00b1b64c | `CONDITIONAL_JUMP`
<a id="insn-00b1b61c"></a> `00b1b61c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b620"></a> `00b1b620` | `81 05 80 52` | mov w1,#0x2c | `FALL_THROUGH`
<a id="insn-00b1b624"></a> `00b1b624` | `22 b3 e5 97` | bl 0x004882ac | `UNCONDITIONAL_CALL`
<a id="insn-00b1b628"></a> `00b1b628` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00b1b62c"></a> `00b1b62c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b630"></a> `00b1b630` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b1b634"></a> `00b1b634` | `1c b1 e5 97` | bl 0x00487aa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b638"></a> `00b1b638` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00b1b63c"></a> `00b1b63c` | `28 fe 07 36` | tbz w8,#0x0,0x00b1b600 | `CONDITIONAL_JUMP`
<a id="insn-00b1b640"></a> `00b1b640` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b644"></a> `00b1b644` | `4f f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b648"></a> `00b1b648` | `ee ff ff 17` | b 0x00b1b600 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1b64c"></a> `00b1b64c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b650"></a> `00b1b650` | `f4 03 03 91` | add x20,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b654"></a> `00b1b654` | `11 b4 e5 97` | bl 0x00488698 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b658"></a> `00b1b658` | `e8 0b 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00b1b65c"></a> `00b1b65c` | `f6 0b 00 f0` | adrp x22,0xc9a000 | `FALL_THROUGH`
<a id="insn-00b1b660"></a> `00b1b660` | `93 22 01 91` | add x19,x20,#0x48 | `FALL_THROUGH`
<a id="insn-00b1b664"></a> `00b1b664` | `08 41 46 f9` | ldr x8,[x8, #0xc80] | `FALL_THROUGH`
<a id="insn-00b1b668"></a> `00b1b668` | `d6 46 46 f9` | ldr x22,[x22, #0xc88] | `FALL_THROUGH`
<a id="insn-00b1b66c"></a> `00b1b66c` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-00b1b670"></a> `00b1b670` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b1b674"></a> `00b1b674` | `e8 63 00 f9` | str x8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b1b678"></a> `00b1b678` | `e9 87 00 f9` | str x9,[sp, #0x108] | `FALL_THROUGH`
<a id="insn-00b1b67c"></a> `00b1b67c` | `28 81 5e f8` | ldur x8,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00b1b680"></a> `00b1b680` | `c9 0e 40 f9` | ldr x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b1b684"></a> `00b1b684` | `69 6a 28 f8` | str x9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b1b688"></a> `00b1b688` | `e8 0b 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00b1b68c"></a> `00b1b68c` | `08 49 46 f9` | ldr x8,[x8, #0xc90] | `FALL_THROUGH`
<a id="insn-00b1b690"></a> `00b1b690` | `e9 43 45 39` | ldrb w9,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00b1b694"></a> `00b1b694` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b1b698"></a> `00b1b698` | `e8 8b 00 f9` | str x8,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b1b69c"></a> `00b1b69c` | `69 00 00 36` | tbz w9,#0x0,0x00b1b6a8 | `CONDITIONAL_JUMP`
<a id="insn-00b1b6a0"></a> `00b1b6a0` | `e0 b3 40 f9` | ldr x0,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00b1b6a4"></a> `00b1b6a4` | `37 f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b6a8"></a> `00b1b6a8` | `80 42 01 91` | add x0,x20,#0x50 | `FALL_THROUGH`
<a id="insn-00b1b6ac"></a> `00b1b6ac` | `71 f2 04 94` | bl 0x00c58070 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b6b0"></a> `00b1b6b0` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00b1b6b4"></a> `00b1b6b4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b1b6b8"></a> `00b1b6b8` | `72 f2 04 94` | bl 0x00c58080 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b6bc"></a> `00b1b6bc` | `e8 03 03 91` | add x8,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00b1b6c0"></a> `00b1b6c0` | `00 e1 02 91` | add x0,x8,#0xb8 | `FALL_THROUGH`
<a id="insn-00b1b6c4"></a> `00b1b6c4` | `73 f2 04 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b6c8"></a> `00b1b6c8` | `e8 83 43 39` | ldrb w8,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00b1b6cc"></a> `00b1b6cc` | `68 00 00 36` | tbz w8,#0x0,0x00b1b6d8 | `CONDITIONAL_JUMP`
<a id="insn-00b1b6d0"></a> `00b1b6d0` | `e0 7b 40 f9` | ldr x0,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00b1b6d4"></a> `00b1b6d4` | `2b f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b6d8"></a> `00b1b6d8` | `e0 67 40 f9` | ldr x0,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00b1b6dc"></a> `00b1b6dc` | `60 00 00 b4` | cbz x0,0x00b1b6e8 | `CONDITIONAL_JUMP`
<a id="insn-00b1b6e0"></a> `00b1b6e0` | `e0 6b 00 f9` | str x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b1b6e4"></a> `00b1b6e4` | `27 f2 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b1b6e8"></a> `00b1b6e8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b1b6ec"></a> `00b1b6ec` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b1b6f0"></a> `00b1b6f0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b1b6f4"></a> `00b1b6f4` | `61 0c 00 54` | b.ne 0x00b1b880 | `CONDITIONAL_JUMP`
<a id="insn-00b1b6f8"></a> `00b1b6f8` | `ff 83 08 91` | add sp,sp,#0x220 | `FALL_THROUGH`
<a id="insn-00b1b6fc"></a> `00b1b6fc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b1b700"></a> `00b1b700` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b1b704"></a> `00b1b704` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b1b708"></a> `00b1b708` | `fc 67 41 a9` | ldp x28,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b1b70c"></a> `00b1b70c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00b1b710"></a> `00b1b710` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b1b880"></a> `00b1b880` | `cc f1 04 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b1aebc`](#insn-00b1aebc) 範囲 `[['00b1aebc', '00b1aed3']]`
  - `FALL_THROUGH` [`00b1aed0`](#insn-00b1aed0) → [`00b1aed4`](#insn-00b1aed4)
- ブロック [`00b1aed4`](#insn-00b1aed4) 範囲 `[['00b1aed4', '00b1af7f']]`
  - `CONDITIONAL_JUMP` [`00b1af7c`](#insn-00b1af7c) → [`00b1afa0`](#insn-00b1afa0)
  - `FALL_THROUGH` [`00b1af7c`](#insn-00b1af7c) → [`00b1af80`](#insn-00b1af80)
- ブロック [`00b1af80`](#insn-00b1af80) 範囲 `[['00b1af80', '00b1af87']]`
  - `CONDITIONAL_JUMP` [`00b1af84`](#insn-00b1af84) → [`00b1afb0`](#insn-00b1afb0)
  - `FALL_THROUGH` [`00b1af84`](#insn-00b1af84) → [`00b1af88`](#insn-00b1af88)
- ブロック [`00b1af88`](#insn-00b1af88) 範囲 `[['00b1af88', '00b1af8f']]`
  - `CONDITIONAL_JUMP` [`00b1af8c`](#insn-00b1af8c) → [`00b1afc0`](#insn-00b1afc0)
  - `FALL_THROUGH` [`00b1af8c`](#insn-00b1af8c) → [`00b1af90`](#insn-00b1af90)
- ブロック [`00b1af90`](#insn-00b1af90) 範囲 `[['00b1af90', '00b1af97']]`
  - `CONDITIONAL_JUMP` [`00b1af94`](#insn-00b1af94) → [`00b1afd0`](#insn-00b1afd0)
  - `FALL_THROUGH` [`00b1af94`](#insn-00b1af94) → [`00b1af98`](#insn-00b1af98)
- ブロック [`00b1af98`](#insn-00b1af98) 範囲 `[['00b1af98', '00b1af9b']]`
  - `CONDITIONAL_JUMP` [`00b1af98`](#insn-00b1af98) → [`00b1afdc`](#insn-00b1afdc)
  - `FALL_THROUGH` [`00b1af98`](#insn-00b1af98) → [`00b1af9c`](#insn-00b1af9c)
- ブロック [`00b1af9c`](#insn-00b1af9c) 範囲 `[['00b1af9c', '00b1af9f']]`
  - `UNCONDITIONAL_JUMP` [`00b1af9c`](#insn-00b1af9c) → [`00b1b198`](#insn-00b1b198)
- ブロック [`00b1afa0`](#insn-00b1afa0) 範囲 `[['00b1afa0', '00b1afaf']]`
  - `CONDITIONAL_JUMP` [`00b1afac`](#insn-00b1afac) → [`00b1af88`](#insn-00b1af88)
  - `FALL_THROUGH` [`00b1afac`](#insn-00b1afac) → [`00b1afb0`](#insn-00b1afb0)
- ブロック [`00b1afb0`](#insn-00b1afb0) 範囲 `[['00b1afb0', '00b1afbf']]`
  - `CONDITIONAL_JUMP` [`00b1afbc`](#insn-00b1afbc) → [`00b1af90`](#insn-00b1af90)
  - `FALL_THROUGH` [`00b1afbc`](#insn-00b1afbc) → [`00b1afc0`](#insn-00b1afc0)
- ブロック [`00b1afc0`](#insn-00b1afc0) 範囲 `[['00b1afc0', '00b1afcf']]`
  - `CONDITIONAL_JUMP` [`00b1afcc`](#insn-00b1afcc) → [`00b1af98`](#insn-00b1af98)
  - `FALL_THROUGH` [`00b1afcc`](#insn-00b1afcc) → [`00b1afd0`](#insn-00b1afd0)
- ブロック [`00b1afd0`](#insn-00b1afd0) 範囲 `[['00b1afd0', '00b1afdb']]`
  - `CONDITIONAL_JUMP` [`00b1afd8`](#insn-00b1afd8) → [`00b1b198`](#insn-00b1b198)
  - `FALL_THROUGH` [`00b1afd8`](#insn-00b1afd8) → [`00b1afdc`](#insn-00b1afdc)
- ブロック [`00b1afdc`](#insn-00b1afdc) 範囲 `[['00b1afdc', '00b1b007']]`
  - `CONDITIONAL_JUMP` [`00b1b004`](#insn-00b1b004) → [`00b1b010`](#insn-00b1b010)
  - `FALL_THROUGH` [`00b1b004`](#insn-00b1b004) → [`00b1b008`](#insn-00b1b008)
- ブロック [`00b1b008`](#insn-00b1b008) 範囲 `[['00b1b008', '00b1b00f']]`
  - `FALL_THROUGH` [`00b1b00c`](#insn-00b1b00c) → [`00b1b010`](#insn-00b1b010)
- ブロック [`00b1b010`](#insn-00b1b010) 範囲 `[['00b1b010', '00b1b03b']]`
  - `CONDITIONAL_JUMP` [`00b1b038`](#insn-00b1b038) → [`00b1b044`](#insn-00b1b044)
  - `FALL_THROUGH` [`00b1b038`](#insn-00b1b038) → [`00b1b03c`](#insn-00b1b03c)
- ブロック [`00b1b03c`](#insn-00b1b03c) 範囲 `[['00b1b03c', '00b1b043']]`
  - `FALL_THROUGH` [`00b1b040`](#insn-00b1b040) → [`00b1b044`](#insn-00b1b044)
- ブロック [`00b1b044`](#insn-00b1b044) 範囲 `[['00b1b044', '00b1b06f']]`
  - `CONDITIONAL_JUMP` [`00b1b06c`](#insn-00b1b06c) → [`00b1b078`](#insn-00b1b078)
  - `FALL_THROUGH` [`00b1b06c`](#insn-00b1b06c) → [`00b1b070`](#insn-00b1b070)
- ブロック [`00b1b070`](#insn-00b1b070) 範囲 `[['00b1b070', '00b1b077']]`
  - `FALL_THROUGH` [`00b1b074`](#insn-00b1b074) → [`00b1b078`](#insn-00b1b078)
- ブロック [`00b1b078`](#insn-00b1b078) 範囲 `[['00b1b078', '00b1b087']]`
  - `FALL_THROUGH` [`00b1b084`](#insn-00b1b084) → [`00b1b088`](#insn-00b1b088)
- ブロック [`00b1b088`](#insn-00b1b088) 範囲 `[['00b1b088', '00b1b0a3']]`
  - `CONDITIONAL_JUMP` [`00b1b0a0`](#insn-00b1b0a0) → [`00b1b0ac`](#insn-00b1b0ac)
  - `FALL_THROUGH` [`00b1b0a0`](#insn-00b1b0a0) → [`00b1b0a4`](#insn-00b1b0a4)
- ブロック [`00b1b0a4`](#insn-00b1b0a4) 範囲 `[['00b1b0a4', '00b1b0ab']]`
  - `FALL_THROUGH` [`00b1b0a8`](#insn-00b1b0a8) → [`00b1b0ac`](#insn-00b1b0ac)
- ブロック [`00b1b0ac`](#insn-00b1b0ac) 範囲 `[['00b1b0ac', '00b1b0cb']]`
  - `FALL_THROUGH` [`00b1b0c8`](#insn-00b1b0c8) → [`00b1b0cc`](#insn-00b1b0cc)
- ブロック [`00b1b0cc`](#insn-00b1b0cc) 範囲 `[['00b1b0cc', '00b1b0e3']]`
  - `CONDITIONAL_JUMP` [`00b1b0e0`](#insn-00b1b0e0) → [`00b1b0ec`](#insn-00b1b0ec)
  - `FALL_THROUGH` [`00b1b0e0`](#insn-00b1b0e0) → [`00b1b0e4`](#insn-00b1b0e4)
- ブロック [`00b1b0e4`](#insn-00b1b0e4) 範囲 `[['00b1b0e4', '00b1b0eb']]`
  - `FALL_THROUGH` [`00b1b0e8`](#insn-00b1b0e8) → [`00b1b0ec`](#insn-00b1b0ec)
- ブロック [`00b1b0ec`](#insn-00b1b0ec) 範囲 `[['00b1b0ec', '00b1b117']]`
  - `CONDITIONAL_JUMP` [`00b1b114`](#insn-00b1b114) → [`00b1b120`](#insn-00b1b120)
  - `FALL_THROUGH` [`00b1b114`](#insn-00b1b114) → [`00b1b118`](#insn-00b1b118)
- ブロック [`00b1b118`](#insn-00b1b118) 範囲 `[['00b1b118', '00b1b11f']]`
  - `FALL_THROUGH` [`00b1b11c`](#insn-00b1b11c) → [`00b1b120`](#insn-00b1b120)
- ブロック [`00b1b120`](#insn-00b1b120) 範囲 `[['00b1b120', '00b1b14b']]`
  - `CONDITIONAL_JUMP` [`00b1b148`](#insn-00b1b148) → [`00b1b154`](#insn-00b1b154)
  - `FALL_THROUGH` [`00b1b148`](#insn-00b1b148) → [`00b1b14c`](#insn-00b1b14c)
- ブロック [`00b1b14c`](#insn-00b1b14c) 範囲 `[['00b1b14c', '00b1b153']]`
  - `FALL_THROUGH` [`00b1b150`](#insn-00b1b150) → [`00b1b154`](#insn-00b1b154)
- ブロック [`00b1b154`](#insn-00b1b154) 範囲 `[['00b1b154', '00b1b173']]`
  - `FALL_THROUGH` [`00b1b170`](#insn-00b1b170) → [`00b1b174`](#insn-00b1b174)
- ブロック [`00b1b174`](#insn-00b1b174) 範囲 `[['00b1b174', '00b1b17f']]`
  - `CONDITIONAL_JUMP` [`00b1b17c`](#insn-00b1b17c) → [`00b1b188`](#insn-00b1b188)
  - `FALL_THROUGH` [`00b1b17c`](#insn-00b1b17c) → [`00b1b180`](#insn-00b1b180)
- ブロック [`00b1b180`](#insn-00b1b180) 範囲 `[['00b1b180', '00b1b187']]`
  - `FALL_THROUGH` [`00b1b184`](#insn-00b1b184) → [`00b1b188`](#insn-00b1b188)
- ブロック [`00b1b188`](#insn-00b1b188) 範囲 `[['00b1b188', '00b1b197']]`
  - `FALL_THROUGH` [`00b1b194`](#insn-00b1b194) → [`00b1b198`](#insn-00b1b198)
- ブロック [`00b1b198`](#insn-00b1b198) 範囲 `[['00b1b198', '00b1b1a3']]`
  - `FALL_THROUGH` [`00b1b1a0`](#insn-00b1b1a0) → [`00b1b1a4`](#insn-00b1b1a4)
- ブロック [`00b1b1a4`](#insn-00b1b1a4) 範囲 `[['00b1b1a4', '00b1b1eb']]`
  - `FALL_THROUGH` [`00b1b1e8`](#insn-00b1b1e8) → [`00b1b1ec`](#insn-00b1b1ec)
- ブロック [`00b1b1ec`](#insn-00b1b1ec) 範囲 `[['00b1b1ec', '00b1b20b']]`
  - `CONDITIONAL_JUMP` [`00b1b208`](#insn-00b1b208) → [`00b1b328`](#insn-00b1b328)
  - `FALL_THROUGH` [`00b1b208`](#insn-00b1b208) → [`00b1b20c`](#insn-00b1b20c)
- ブロック [`00b1b20c`](#insn-00b1b20c) 範囲 `[['00b1b20c', '00b1b213']]`
  - `CONDITIONAL_JUMP` [`00b1b210`](#insn-00b1b210) → [`00b1b338`](#insn-00b1b338)
  - `FALL_THROUGH` [`00b1b210`](#insn-00b1b210) → [`00b1b214`](#insn-00b1b214)
- ブロック [`00b1b214`](#insn-00b1b214) 範囲 `[['00b1b214', '00b1b21b']]`
  - `CONDITIONAL_JUMP` [`00b1b218`](#insn-00b1b218) → [`00b1b348`](#insn-00b1b348)
  - `FALL_THROUGH` [`00b1b218`](#insn-00b1b218) → [`00b1b21c`](#insn-00b1b21c)
- ブロック [`00b1b21c`](#insn-00b1b21c) 範囲 `[['00b1b21c', '00b1b223']]`
  - `CONDITIONAL_JUMP` [`00b1b220`](#insn-00b1b220) → [`00b1b22c`](#insn-00b1b22c)
  - `FALL_THROUGH` [`00b1b220`](#insn-00b1b220) → [`00b1b224`](#insn-00b1b224)
- ブロック [`00b1b224`](#insn-00b1b224) 範囲 `[['00b1b224', '00b1b22b']]`
  - `FALL_THROUGH` [`00b1b228`](#insn-00b1b228) → [`00b1b22c`](#insn-00b1b22c)
- ブロック [`00b1b22c`](#insn-00b1b22c) 範囲 `[['00b1b22c', '00b1b237']]`
  - `CONDITIONAL_JUMP` [`00b1b234`](#insn-00b1b234) → [`00b1b290`](#insn-00b1b290)
  - `FALL_THROUGH` [`00b1b234`](#insn-00b1b234) → [`00b1b238`](#insn-00b1b238)
- ブロック [`00b1b238`](#insn-00b1b238) 範囲 `[['00b1b238', '00b1b243']]`
  - `UNCONDITIONAL_JUMP` [`00b1b240`](#insn-00b1b240) → [`00b1b260`](#insn-00b1b260)
- ブロック [`00b1b244`](#insn-00b1b244) 範囲 `[['00b1b244', '00b1b25f']]`
  - `CONDITIONAL_JUMP` [`00b1b25c`](#insn-00b1b25c) → [`00b1b290`](#insn-00b1b290)
  - `FALL_THROUGH` [`00b1b25c`](#insn-00b1b25c) → [`00b1b260`](#insn-00b1b260)
- ブロック [`00b1b260`](#insn-00b1b260) 範囲 `[['00b1b260', '00b1b26f']]`
  - `FALL_THROUGH` [`00b1b26c`](#insn-00b1b26c) → [`00b1b270`](#insn-00b1b270)
- ブロック [`00b1b270`](#insn-00b1b270) 範囲 `[['00b1b270', '00b1b283']]`
  - `CONDITIONAL_JUMP` [`00b1b280`](#insn-00b1b280) → [`00b1b244`](#insn-00b1b244)
  - `FALL_THROUGH` [`00b1b280`](#insn-00b1b280) → [`00b1b284`](#insn-00b1b284)
- ブロック [`00b1b284`](#insn-00b1b284) 範囲 `[['00b1b284', '00b1b28f']]`
  - `UNCONDITIONAL_JUMP` [`00b1b28c`](#insn-00b1b28c) → [`00b1b244`](#insn-00b1b244)
- ブロック [`00b1b290`](#insn-00b1b290) 範囲 `[['00b1b290', '00b1b303']]`
  - `FALL_THROUGH` [`00b1b300`](#insn-00b1b300) → [`00b1b304`](#insn-00b1b304)
- ブロック [`00b1b304`](#insn-00b1b304) 範囲 `[['00b1b304', '00b1b307']]`
  - `CONDITIONAL_JUMP` [`00b1b304`](#insn-00b1b304) → [`00b1b35c`](#insn-00b1b35c)
  - `FALL_THROUGH` [`00b1b304`](#insn-00b1b304) → [`00b1b308`](#insn-00b1b308)
- ブロック [`00b1b308`](#insn-00b1b308) 範囲 `[['00b1b308', '00b1b30f']]`
  - `CONDITIONAL_JUMP` [`00b1b30c`](#insn-00b1b30c) → [`00b1b36c`](#insn-00b1b36c)
  - `FALL_THROUGH` [`00b1b30c`](#insn-00b1b30c) → [`00b1b310`](#insn-00b1b310)
- ブロック [`00b1b310`](#insn-00b1b310) 範囲 `[['00b1b310', '00b1b317']]`
  - `CONDITIONAL_JUMP` [`00b1b314`](#insn-00b1b314) → [`00b1b37c`](#insn-00b1b37c)
  - `FALL_THROUGH` [`00b1b314`](#insn-00b1b314) → [`00b1b318`](#insn-00b1b318)
- ブロック [`00b1b318`](#insn-00b1b318) 範囲 `[['00b1b318', '00b1b31f']]`
  - `CONDITIONAL_JUMP` [`00b1b31c`](#insn-00b1b31c) → [`00b1b38c`](#insn-00b1b38c)
  - `FALL_THROUGH` [`00b1b31c`](#insn-00b1b31c) → [`00b1b320`](#insn-00b1b320)
- ブロック [`00b1b320`](#insn-00b1b320) 範囲 `[['00b1b320', '00b1b323']]`
  - `CONDITIONAL_JUMP` [`00b1b320`](#insn-00b1b320) → [`00b1b398`](#insn-00b1b398)
  - `FALL_THROUGH` [`00b1b320`](#insn-00b1b320) → [`00b1b324`](#insn-00b1b324)
- ブロック [`00b1b324`](#insn-00b1b324) 範囲 `[['00b1b324', '00b1b327']]`
  - `UNCONDITIONAL_JUMP` [`00b1b324`](#insn-00b1b324) → [`00b1b3f0`](#insn-00b1b3f0)
- ブロック [`00b1b328`](#insn-00b1b328) 範囲 `[['00b1b328', '00b1b337']]`
  - `CONDITIONAL_JUMP` [`00b1b334`](#insn-00b1b334) → [`00b1b214`](#insn-00b1b214)
  - `FALL_THROUGH` [`00b1b334`](#insn-00b1b334) → [`00b1b338`](#insn-00b1b338)
- ブロック [`00b1b338`](#insn-00b1b338) 範囲 `[['00b1b338', '00b1b33f']]`
  - `FALL_THROUGH` [`00b1b33c`](#insn-00b1b33c) → [`00b1b340`](#insn-00b1b340)
- ブロック [`00b1b340`](#insn-00b1b340) 範囲 `[['00b1b340', '00b1b347']]`
  - `CONDITIONAL_JUMP` [`00b1b344`](#insn-00b1b344) → [`00b1b21c`](#insn-00b1b21c)
  - `FALL_THROUGH` [`00b1b344`](#insn-00b1b344) → [`00b1b348`](#insn-00b1b348)
- ブロック [`00b1b348`](#insn-00b1b348) 範囲 `[['00b1b348', '00b1b357']]`
  - `CONDITIONAL_JUMP` [`00b1b354`](#insn-00b1b354) → [`00b1b224`](#insn-00b1b224)
  - `FALL_THROUGH` [`00b1b354`](#insn-00b1b354) → [`00b1b358`](#insn-00b1b358)
- ブロック [`00b1b358`](#insn-00b1b358) 範囲 `[['00b1b358', '00b1b35b']]`
  - `UNCONDITIONAL_JUMP` [`00b1b358`](#insn-00b1b358) → [`00b1b22c`](#insn-00b1b22c)
- ブロック [`00b1b35c`](#insn-00b1b35c) 範囲 `[['00b1b35c', '00b1b36b']]`
  - `CONDITIONAL_JUMP` [`00b1b368`](#insn-00b1b368) → [`00b1b310`](#insn-00b1b310)
  - `FALL_THROUGH` [`00b1b368`](#insn-00b1b368) → [`00b1b36c`](#insn-00b1b36c)
- ブロック [`00b1b36c`](#insn-00b1b36c) 範囲 `[['00b1b36c', '00b1b37b']]`
  - `CONDITIONAL_JUMP` [`00b1b378`](#insn-00b1b378) → [`00b1b318`](#insn-00b1b318)
  - `FALL_THROUGH` [`00b1b378`](#insn-00b1b378) → [`00b1b37c`](#insn-00b1b37c)
- ブロック [`00b1b37c`](#insn-00b1b37c) 範囲 `[['00b1b37c', '00b1b38b']]`
  - `CONDITIONAL_JUMP` [`00b1b388`](#insn-00b1b388) → [`00b1b320`](#insn-00b1b320)
  - `FALL_THROUGH` [`00b1b388`](#insn-00b1b388) → [`00b1b38c`](#insn-00b1b38c)
- ブロック [`00b1b38c`](#insn-00b1b38c) 範囲 `[['00b1b38c', '00b1b38f']]`
  - `FALL_THROUGH` [`00b1b38c`](#insn-00b1b38c) → [`00b1b390`](#insn-00b1b390)
- ブロック [`00b1b390`](#insn-00b1b390) 範囲 `[['00b1b390', '00b1b397']]`
  - `CONDITIONAL_JUMP` [`00b1b394`](#insn-00b1b394) → [`00b1b3f0`](#insn-00b1b3f0)
  - `FALL_THROUGH` [`00b1b394`](#insn-00b1b394) → [`00b1b398`](#insn-00b1b398)
- ブロック [`00b1b398`](#insn-00b1b398) 範囲 `[['00b1b398', '00b1b3a3']]`
  - `UNCONDITIONAL_JUMP` [`00b1b3a0`](#insn-00b1b3a0) → [`00b1b3c0`](#insn-00b1b3c0)
- ブロック [`00b1b3a4`](#insn-00b1b3a4) 範囲 `[['00b1b3a4', '00b1b3bf']]`
  - `CONDITIONAL_JUMP` [`00b1b3bc`](#insn-00b1b3bc) → [`00b1b3f0`](#insn-00b1b3f0)
  - `FALL_THROUGH` [`00b1b3bc`](#insn-00b1b3bc) → [`00b1b3c0`](#insn-00b1b3c0)
- ブロック [`00b1b3c0`](#insn-00b1b3c0) 範囲 `[['00b1b3c0', '00b1b3cb']]`
  - `FALL_THROUGH` [`00b1b3c8`](#insn-00b1b3c8) → [`00b1b3cc`](#insn-00b1b3cc)
- ブロック [`00b1b3cc`](#insn-00b1b3cc) 範囲 `[['00b1b3cc', '00b1b3e3']]`
  - `CONDITIONAL_JUMP` [`00b1b3e0`](#insn-00b1b3e0) → [`00b1b3a4`](#insn-00b1b3a4)
  - `FALL_THROUGH` [`00b1b3e0`](#insn-00b1b3e0) → [`00b1b3e4`](#insn-00b1b3e4)
- ブロック [`00b1b3e4`](#insn-00b1b3e4) 範囲 `[['00b1b3e4', '00b1b3ef']]`
  - `UNCONDITIONAL_JUMP` [`00b1b3ec`](#insn-00b1b3ec) → [`00b1b3a4`](#insn-00b1b3a4)
- ブロック [`00b1b3f0`](#insn-00b1b3f0) 範囲 `[['00b1b3f0', '00b1b417']]`
  - `FALL_THROUGH` [`00b1b414`](#insn-00b1b414) → [`00b1b418`](#insn-00b1b418)
- ブロック [`00b1b418`](#insn-00b1b418) 範囲 `[['00b1b418', '00b1b453']]`
  - `FALL_THROUGH` [`00b1b450`](#insn-00b1b450) → [`00b1b454`](#insn-00b1b454)
- ブロック [`00b1b454`](#insn-00b1b454) 範囲 `[['00b1b454', '00b1b467']]`
  - `CONDITIONAL_JUMP` [`00b1b464`](#insn-00b1b464) → [`00b1b488`](#insn-00b1b488)
  - `FALL_THROUGH` [`00b1b464`](#insn-00b1b464) → [`00b1b468`](#insn-00b1b468)
- ブロック [`00b1b468`](#insn-00b1b468) 範囲 `[['00b1b468', '00b1b46f']]`
  - `CONDITIONAL_JUMP` [`00b1b46c`](#insn-00b1b46c) → [`00b1b498`](#insn-00b1b498)
  - `FALL_THROUGH` [`00b1b46c`](#insn-00b1b46c) → [`00b1b470`](#insn-00b1b470)
- ブロック [`00b1b470`](#insn-00b1b470) 範囲 `[['00b1b470', '00b1b477']]`
  - `CONDITIONAL_JUMP` [`00b1b474`](#insn-00b1b474) → [`00b1b4a8`](#insn-00b1b4a8)
  - `FALL_THROUGH` [`00b1b474`](#insn-00b1b474) → [`00b1b478`](#insn-00b1b478)
- ブロック [`00b1b478`](#insn-00b1b478) 範囲 `[['00b1b478', '00b1b47f']]`
  - `CONDITIONAL_JUMP` [`00b1b47c`](#insn-00b1b47c) → [`00b1b4b8`](#insn-00b1b4b8)
  - `FALL_THROUGH` [`00b1b47c`](#insn-00b1b47c) → [`00b1b480`](#insn-00b1b480)
- ブロック [`00b1b480`](#insn-00b1b480) 範囲 `[['00b1b480', '00b1b483']]`
  - `CONDITIONAL_JUMP` [`00b1b480`](#insn-00b1b480) → [`00b1b4c4`](#insn-00b1b4c4)
  - `FALL_THROUGH` [`00b1b480`](#insn-00b1b480) → [`00b1b484`](#insn-00b1b484)
- ブロック [`00b1b484`](#insn-00b1b484) 範囲 `[['00b1b484', '00b1b487']]`
  - `UNCONDITIONAL_JUMP` [`00b1b484`](#insn-00b1b484) → [`00b1b51c`](#insn-00b1b51c)
- ブロック [`00b1b488`](#insn-00b1b488) 範囲 `[['00b1b488', '00b1b497']]`
  - `CONDITIONAL_JUMP` [`00b1b494`](#insn-00b1b494) → [`00b1b470`](#insn-00b1b470)
  - `FALL_THROUGH` [`00b1b494`](#insn-00b1b494) → [`00b1b498`](#insn-00b1b498)
- ブロック [`00b1b498`](#insn-00b1b498) 範囲 `[['00b1b498', '00b1b4a7']]`
  - `CONDITIONAL_JUMP` [`00b1b4a4`](#insn-00b1b4a4) → [`00b1b478`](#insn-00b1b478)
  - `FALL_THROUGH` [`00b1b4a4`](#insn-00b1b4a4) → [`00b1b4a8`](#insn-00b1b4a8)
- ブロック [`00b1b4a8`](#insn-00b1b4a8) 範囲 `[['00b1b4a8', '00b1b4b3']]`
  - `FALL_THROUGH` [`00b1b4b0`](#insn-00b1b4b0) → [`00b1b4b4`](#insn-00b1b4b4)
- ブロック [`00b1b4b4`](#insn-00b1b4b4) 範囲 `[['00b1b4b4', '00b1b4b7']]`
  - `CONDITIONAL_JUMP` [`00b1b4b4`](#insn-00b1b4b4) → [`00b1b480`](#insn-00b1b480)
  - `FALL_THROUGH` [`00b1b4b4`](#insn-00b1b4b4) → [`00b1b4b8`](#insn-00b1b4b8)
- ブロック [`00b1b4b8`](#insn-00b1b4b8) 範囲 `[['00b1b4b8', '00b1b4c3']]`
  - `CONDITIONAL_JUMP` [`00b1b4c0`](#insn-00b1b4c0) → [`00b1b51c`](#insn-00b1b51c)
  - `FALL_THROUGH` [`00b1b4c0`](#insn-00b1b4c0) → [`00b1b4c4`](#insn-00b1b4c4)
- ブロック [`00b1b4c4`](#insn-00b1b4c4) 範囲 `[['00b1b4c4', '00b1b4cf']]`
  - `UNCONDITIONAL_JUMP` [`00b1b4cc`](#insn-00b1b4cc) → [`00b1b4ec`](#insn-00b1b4ec)
- ブロック [`00b1b4d0`](#insn-00b1b4d0) 範囲 `[['00b1b4d0', '00b1b4eb']]`
  - `CONDITIONAL_JUMP` [`00b1b4e8`](#insn-00b1b4e8) → [`00b1b51c`](#insn-00b1b51c)
  - `FALL_THROUGH` [`00b1b4e8`](#insn-00b1b4e8) → [`00b1b4ec`](#insn-00b1b4ec)
- ブロック [`00b1b4ec`](#insn-00b1b4ec) 範囲 `[['00b1b4ec', '00b1b4ef']]`
  - `FALL_THROUGH` [`00b1b4ec`](#insn-00b1b4ec) → [`00b1b4f0`](#insn-00b1b4f0)
- ブロック [`00b1b4f0`](#insn-00b1b4f0) 範囲 `[['00b1b4f0', '00b1b50f']]`
  - `CONDITIONAL_JUMP` [`00b1b50c`](#insn-00b1b50c) → [`00b1b4d0`](#insn-00b1b4d0)
  - `FALL_THROUGH` [`00b1b50c`](#insn-00b1b50c) → [`00b1b510`](#insn-00b1b510)
- ブロック [`00b1b510`](#insn-00b1b510) 範囲 `[['00b1b510', '00b1b51b']]`
  - `UNCONDITIONAL_JUMP` [`00b1b518`](#insn-00b1b518) → [`00b1b4d0`](#insn-00b1b4d0)
- ブロック [`00b1b51c`](#insn-00b1b51c) 範囲 `[['00b1b51c', '00b1b52f']]`
  - `FALL_THROUGH` [`00b1b52c`](#insn-00b1b52c) → [`00b1b530`](#insn-00b1b530)
- ブロック [`00b1b530`](#insn-00b1b530) 範囲 `[['00b1b530', '00b1b557']]`
  - `FALL_THROUGH` [`00b1b554`](#insn-00b1b554) → [`00b1b558`](#insn-00b1b558)
- ブロック [`00b1b558`](#insn-00b1b558) 範囲 `[['00b1b558', '00b1b573']]`
  - `FALL_THROUGH` [`00b1b570`](#insn-00b1b570) → [`00b1b574`](#insn-00b1b574)
- ブロック [`00b1b574`](#insn-00b1b574) 範囲 `[['00b1b574', '00b1b593']]`
  - `CONDITIONAL_JUMP` [`00b1b590`](#insn-00b1b590) → [`00b1b5b4`](#insn-00b1b5b4)
  - `FALL_THROUGH` [`00b1b590`](#insn-00b1b590) → [`00b1b594`](#insn-00b1b594)
- ブロック [`00b1b594`](#insn-00b1b594) 範囲 `[['00b1b594', '00b1b59b']]`
  - `CONDITIONAL_JUMP` [`00b1b598`](#insn-00b1b598) → [`00b1b5c4`](#insn-00b1b5c4)
  - `FALL_THROUGH` [`00b1b598`](#insn-00b1b598) → [`00b1b59c`](#insn-00b1b59c)
- ブロック [`00b1b59c`](#insn-00b1b59c) 範囲 `[['00b1b59c', '00b1b5a3']]`
  - `CONDITIONAL_JUMP` [`00b1b5a0`](#insn-00b1b5a0) → [`00b1b5d4`](#insn-00b1b5d4)
  - `FALL_THROUGH` [`00b1b5a0`](#insn-00b1b5a0) → [`00b1b5a4`](#insn-00b1b5a4)
- ブロック [`00b1b5a4`](#insn-00b1b5a4) 範囲 `[['00b1b5a4', '00b1b5ab']]`
  - `CONDITIONAL_JUMP` [`00b1b5a8`](#insn-00b1b5a8) → [`00b1b5e4`](#insn-00b1b5e4)
  - `FALL_THROUGH` [`00b1b5a8`](#insn-00b1b5a8) → [`00b1b5ac`](#insn-00b1b5ac)
- ブロック [`00b1b5ac`](#insn-00b1b5ac) 範囲 `[['00b1b5ac', '00b1b5af']]`
  - `CONDITIONAL_JUMP` [`00b1b5ac`](#insn-00b1b5ac) → [`00b1b5f0`](#insn-00b1b5f0)
  - `FALL_THROUGH` [`00b1b5ac`](#insn-00b1b5ac) → [`00b1b5b0`](#insn-00b1b5b0)
- ブロック [`00b1b5b0`](#insn-00b1b5b0) 範囲 `[['00b1b5b0', '00b1b5b3']]`
  - `UNCONDITIONAL_JUMP` [`00b1b5b0`](#insn-00b1b5b0) → [`00b1b64c`](#insn-00b1b64c)
- ブロック [`00b1b5b4`](#insn-00b1b5b4) 範囲 `[['00b1b5b4', '00b1b5c3']]`
  - `CONDITIONAL_JUMP` [`00b1b5c0`](#insn-00b1b5c0) → [`00b1b59c`](#insn-00b1b59c)
  - `FALL_THROUGH` [`00b1b5c0`](#insn-00b1b5c0) → [`00b1b5c4`](#insn-00b1b5c4)
- ブロック [`00b1b5c4`](#insn-00b1b5c4) 範囲 `[['00b1b5c4', '00b1b5cb']]`
  - `FALL_THROUGH` [`00b1b5c8`](#insn-00b1b5c8) → [`00b1b5cc`](#insn-00b1b5cc)
- ブロック [`00b1b5cc`](#insn-00b1b5cc) 範囲 `[['00b1b5cc', '00b1b5d3']]`
  - `CONDITIONAL_JUMP` [`00b1b5d0`](#insn-00b1b5d0) → [`00b1b5a4`](#insn-00b1b5a4)
  - `FALL_THROUGH` [`00b1b5d0`](#insn-00b1b5d0) → [`00b1b5d4`](#insn-00b1b5d4)
- ブロック [`00b1b5d4`](#insn-00b1b5d4) 範囲 `[['00b1b5d4', '00b1b5e3']]`
  - `CONDITIONAL_JUMP` [`00b1b5e0`](#insn-00b1b5e0) → [`00b1b5ac`](#insn-00b1b5ac)
  - `FALL_THROUGH` [`00b1b5e0`](#insn-00b1b5e0) → [`00b1b5e4`](#insn-00b1b5e4)
- ブロック [`00b1b5e4`](#insn-00b1b5e4) 範囲 `[['00b1b5e4', '00b1b5ef']]`
  - `CONDITIONAL_JUMP` [`00b1b5ec`](#insn-00b1b5ec) → [`00b1b64c`](#insn-00b1b64c)
  - `FALL_THROUGH` [`00b1b5ec`](#insn-00b1b5ec) → [`00b1b5f0`](#insn-00b1b5f0)
- ブロック [`00b1b5f0`](#insn-00b1b5f0) 範囲 `[['00b1b5f0', '00b1b5fb']]`
  - `FALL_THROUGH` [`00b1b5f8`](#insn-00b1b5f8) → [`00b1b5fc`](#insn-00b1b5fc)
- ブロック [`00b1b5fc`](#insn-00b1b5fc) 範囲 `[['00b1b5fc', '00b1b5ff']]`
  - `UNCONDITIONAL_JUMP` [`00b1b5fc`](#insn-00b1b5fc) → [`00b1b61c`](#insn-00b1b61c)
- ブロック [`00b1b600`](#insn-00b1b600) 範囲 `[['00b1b600', '00b1b61b']]`
  - `CONDITIONAL_JUMP` [`00b1b618`](#insn-00b1b618) → [`00b1b64c`](#insn-00b1b64c)
  - `FALL_THROUGH` [`00b1b618`](#insn-00b1b618) → [`00b1b61c`](#insn-00b1b61c)
- ブロック [`00b1b61c`](#insn-00b1b61c) 範囲 `[['00b1b61c', '00b1b623']]`
  - `FALL_THROUGH` [`00b1b620`](#insn-00b1b620) → [`00b1b624`](#insn-00b1b624)
- ブロック [`00b1b624`](#insn-00b1b624) 範囲 `[['00b1b624', '00b1b63f']]`
  - `CONDITIONAL_JUMP` [`00b1b63c`](#insn-00b1b63c) → [`00b1b600`](#insn-00b1b600)
  - `FALL_THROUGH` [`00b1b63c`](#insn-00b1b63c) → [`00b1b640`](#insn-00b1b640)
- ブロック [`00b1b640`](#insn-00b1b640) 範囲 `[['00b1b640', '00b1b64b']]`
  - `UNCONDITIONAL_JUMP` [`00b1b648`](#insn-00b1b648) → [`00b1b600`](#insn-00b1b600)
- ブロック [`00b1b64c`](#insn-00b1b64c) 範囲 `[['00b1b64c', '00b1b663']]`
  - `FALL_THROUGH` [`00b1b660`](#insn-00b1b660) → [`00b1b664`](#insn-00b1b664)
- ブロック [`00b1b664`](#insn-00b1b664) 範囲 `[['00b1b664', '00b1b68f']]`
  - `FALL_THROUGH` [`00b1b68c`](#insn-00b1b68c) → [`00b1b690`](#insn-00b1b690)
- ブロック [`00b1b690`](#insn-00b1b690) 範囲 `[['00b1b690', '00b1b69f']]`
  - `CONDITIONAL_JUMP` [`00b1b69c`](#insn-00b1b69c) → [`00b1b6a8`](#insn-00b1b6a8)
  - `FALL_THROUGH` [`00b1b69c`](#insn-00b1b69c) → [`00b1b6a0`](#insn-00b1b6a0)
- ブロック [`00b1b6a0`](#insn-00b1b6a0) 範囲 `[['00b1b6a0', '00b1b6a7']]`
  - `FALL_THROUGH` [`00b1b6a4`](#insn-00b1b6a4) → [`00b1b6a8`](#insn-00b1b6a8)
- ブロック [`00b1b6a8`](#insn-00b1b6a8) 範囲 `[['00b1b6a8', '00b1b6cf']]`
  - `CONDITIONAL_JUMP` [`00b1b6cc`](#insn-00b1b6cc) → [`00b1b6d8`](#insn-00b1b6d8)
  - `FALL_THROUGH` [`00b1b6cc`](#insn-00b1b6cc) → [`00b1b6d0`](#insn-00b1b6d0)
- ブロック [`00b1b6d0`](#insn-00b1b6d0) 範囲 `[['00b1b6d0', '00b1b6d7']]`
  - `FALL_THROUGH` [`00b1b6d4`](#insn-00b1b6d4) → [`00b1b6d8`](#insn-00b1b6d8)
- ブロック [`00b1b6d8`](#insn-00b1b6d8) 範囲 `[['00b1b6d8', '00b1b6df']]`
  - `CONDITIONAL_JUMP` [`00b1b6dc`](#insn-00b1b6dc) → [`00b1b6e8`](#insn-00b1b6e8)
  - `FALL_THROUGH` [`00b1b6dc`](#insn-00b1b6dc) → [`00b1b6e0`](#insn-00b1b6e0)
- ブロック [`00b1b6e0`](#insn-00b1b6e0) 範囲 `[['00b1b6e0', '00b1b6e7']]`
  - `FALL_THROUGH` [`00b1b6e4`](#insn-00b1b6e4) → [`00b1b6e8`](#insn-00b1b6e8)
- ブロック [`00b1b6e8`](#insn-00b1b6e8) 範囲 `[['00b1b6e8', '00b1b6f7']]`
  - `CONDITIONAL_JUMP` [`00b1b6f4`](#insn-00b1b6f4) → [`00b1b880`](#insn-00b1b880)
  - `FALL_THROUGH` [`00b1b6f4`](#insn-00b1b6f4) → [`00b1b6f8`](#insn-00b1b6f8)
- ブロック [`00b1b6f8`](#insn-00b1b6f8) 範囲 `[['00b1b6f8', '00b1b713']]`
- ブロック [`00b1b880`](#insn-00b1b880) 範囲 `[['00b1b880', '00b1b883']]`

## 命令位置別の参照

- [`00b1aebc`](#insn-00b1aebc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1aec0`](#insn-00b1aec0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1aec4`](#insn-00b1aec4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1aec8`](#insn-00b1aec8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1aecc`](#insn-00b1aecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1aee8`](#insn-00b1aee8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1aeec`](#insn-00b1aeec) → [`00487e60`](../00487/00487e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487e60` · 推定シンボル `None` · 推定型 `None`
- [`00b1aef8`](#insn-00b1aef8) → `00c64e08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00b1aef8`](#insn-00b1aef8) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af04`](#insn-00b1af04) → [`00a9c0d4`](../00a9c/00a9c0d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a9c0d4` · 推定シンボル `None` · 推定型 `None`
- [`00b1af18`](#insn-00b1af18) → `002c1a6c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1af1c`](#insn-00b1af1c) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af28`](#insn-00b1af28) → `Stack[-0x20b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af2c`](#insn-00b1af2c) → `Stack[-0x1cf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af38`](#insn-00b1af38) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af3c`](#insn-00b1af3c) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af40`](#insn-00b1af40) → `Stack[-0x20f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af4c`](#insn-00b1af4c) → [`0048ce94`](../0048c/0048ce94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce94` · 推定シンボル `None` · 推定型 `None`
- [`00b1af5c`](#insn-00b1af5c) → [`00492e48`](../00492/00492e48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492e48` · 推定シンボル `None` · 推定型 `None`
- [`00b1af70`](#insn-00b1af70) → [`00b11188`](../00b11/00b11188.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b11188` · 推定シンボル `None` · 推定型 `None`
- [`00b1af74`](#insn-00b1af74) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af7c`](#insn-00b1af7c) → [`00b1afa0`](#insn-00b1afa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af80`](#insn-00b1af80) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af84`](#insn-00b1af84) → [`00b1afb0`](#insn-00b1afb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af88`](#insn-00b1af88) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af8c`](#insn-00b1af8c) → [`00b1afc0`](#insn-00b1afc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af90`](#insn-00b1af90) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af94`](#insn-00b1af94) → [`00b1afd0`](#insn-00b1afd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af98`](#insn-00b1af98) → [`00b1afdc`](#insn-00b1afdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1af9c`](#insn-00b1af9c) → [`00b1b198`](#insn-00b1b198) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afa0`](#insn-00b1afa0) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afa4`](#insn-00b1afa4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1afa8`](#insn-00b1afa8) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afac`](#insn-00b1afac) → [`00b1af88`](#insn-00b1af88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afb0`](#insn-00b1afb0) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afb4`](#insn-00b1afb4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1afb8`](#insn-00b1afb8) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afbc`](#insn-00b1afbc) → [`00b1af90`](#insn-00b1af90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afc0`](#insn-00b1afc0) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afc4`](#insn-00b1afc4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1afc8`](#insn-00b1afc8) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afcc`](#insn-00b1afcc) → [`00b1af98`](#insn-00b1af98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afd0`](#insn-00b1afd0) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afd4`](#insn-00b1afd4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1afd8`](#insn-00b1afd8) → [`00b1b198`](#insn-00b1b198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1afe4`](#insn-00b1afe4) → [`004882ac`](../00488/004882ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004882ac` · 推定シンボル `None` · 推定型 `None`
- [`00b1aff4`](#insn-00b1aff4) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b000`](#insn-00b1b000) → `0032f6d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b004`](#insn-00b1b004) → [`00b1b010`](#insn-00b1b010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b008`](#insn-00b1b008) → `0032f6e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b00c`](#insn-00b1b00c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b010`](#insn-00b1b010) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b014`](#insn-00b1b014) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b018`](#insn-00b1b018) → `0032f6d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b01c`](#insn-00b1b01c) → `0032f6e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b02c`](#insn-00b1b02c) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b034`](#insn-00b1b034) → `0032f6f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b038`](#insn-00b1b038) → [`00b1b044`](#insn-00b1b044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b03c`](#insn-00b1b03c) → `0032f700`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b040`](#insn-00b1b040) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b044`](#insn-00b1b044) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b048`](#insn-00b1b048) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b04c`](#insn-00b1b04c) → `0032f6f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b050`](#insn-00b1b050) → `0032f700`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b060`](#insn-00b1b060) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b068`](#insn-00b1b068) → `0032f708`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b06c`](#insn-00b1b06c) → [`00b1b078`](#insn-00b1b078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b070`](#insn-00b1b070) → `0032f718`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b074`](#insn-00b1b074) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b078`](#insn-00b1b078) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b07c`](#insn-00b1b07c) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b080`](#insn-00b1b080) → `0032f708`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b084`](#insn-00b1b084) → `0032f718`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b094`](#insn-00b1b094) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b09c`](#insn-00b1b09c) → `0032f720`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b0a0`](#insn-00b1b0a0) → [`00b1b0ac`](#insn-00b1b0ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b0a4`](#insn-00b1b0a4) → `0032f730`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b0a8`](#insn-00b1b0a8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b0ac`](#insn-00b1b0ac) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b0b0`](#insn-00b1b0b0) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b0b4`](#insn-00b1b0b4) → `0032f720`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b0b8`](#insn-00b1b0b8) → `0032f730`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b0c4`](#insn-00b1b0c4) → [`004882ac`](../00488/004882ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004882ac` · 推定シンボル `None` · 推定型 `None`
- [`00b1b0d4`](#insn-00b1b0d4) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b0dc`](#insn-00b1b0dc) → `0032f738`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b0e0`](#insn-00b1b0e0) → [`00b1b0ec`](#insn-00b1b0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b0e4`](#insn-00b1b0e4) → `0032f748`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b0e8`](#insn-00b1b0e8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b0ec`](#insn-00b1b0ec) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b0f0`](#insn-00b1b0f0) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b0f4`](#insn-00b1b0f4) → `0032f738`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b0f8`](#insn-00b1b0f8) → `0032f748`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b108`](#insn-00b1b108) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b110`](#insn-00b1b110) → `0032f750`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b114`](#insn-00b1b114) → [`00b1b120`](#insn-00b1b120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b118`](#insn-00b1b118) → `0032f760`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b11c`](#insn-00b1b11c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b120`](#insn-00b1b120) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b124`](#insn-00b1b124) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b128`](#insn-00b1b128) → `0032f750`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b12c`](#insn-00b1b12c) → `0032f760`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b13c`](#insn-00b1b13c) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b144`](#insn-00b1b144) → `0032f768`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b148`](#insn-00b1b148) → [`00b1b154`](#insn-00b1b154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b14c`](#insn-00b1b14c) → `0032f778`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b150`](#insn-00b1b150) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b154`](#insn-00b1b154) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b158`](#insn-00b1b158) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b15c`](#insn-00b1b15c) → `0032f768`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b160`](#insn-00b1b160) → `0032f778`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b170`](#insn-00b1b170) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b178`](#insn-00b1b178) → `0032f780`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b17c`](#insn-00b1b17c) → [`00b1b188`](#insn-00b1b188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b180`](#insn-00b1b180) → `0032f790`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b184`](#insn-00b1b184) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b188`](#insn-00b1b188) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b18c`](#insn-00b1b18c) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b190`](#insn-00b1b190) → `0032f780`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b194`](#insn-00b1b194) → `0032f790`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00b1b19c`](#insn-00b1b19c) → [`00488698`](../00488/00488698.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488698` · 推定シンボル `None` · 推定型 `None`
- [`00b1b1ac`](#insn-00b1b1ac) → `002a6f75`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b1b4`](#insn-00b1b1b4) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b1bc`](#insn-00b1b1bc) → `Stack[-0x1d7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b1c0`](#insn-00b1b1c0) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b1c4`](#insn-00b1b1c4) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b1c8`](#insn-00b1b1c8) → `Stack[-0x20f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b1cc`](#insn-00b1b1cc) → `Stack[-0x20b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b1d8`](#insn-00b1b1d8) → [`0048ce94`](../0048c/0048ce94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce94` · 推定シンボル `None` · 推定型 `None`
- [`00b1b1e8`](#insn-00b1b1e8) → [`00492e48`](../00492/00492e48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492e48` · 推定シンボル `None` · 推定型 `None`
- [`00b1b1fc`](#insn-00b1b1fc) → [`00b11188`](../00b11/00b11188.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b11188` · 推定シンボル `None` · 推定型 `None`
- [`00b1b200`](#insn-00b1b200) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b208`](#insn-00b1b208) → [`00b1b328`](#insn-00b1b328) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b20c`](#insn-00b1b20c) → `Stack[-0x228]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b210`](#insn-00b1b210) → [`00b1b338`](#insn-00b1b338) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b214`](#insn-00b1b214) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b218`](#insn-00b1b218) → [`00b1b348`](#insn-00b1b348) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b21c`](#insn-00b1b21c) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b220`](#insn-00b1b220) → [`00b1b22c`](#insn-00b1b22c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b224`](#insn-00b1b224) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b228`](#insn-00b1b228) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b234`](#insn-00b1b234) → [`00b1b290`](#insn-00b1b290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b240`](#insn-00b1b240) → [`00b1b260`](#insn-00b1b260) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b244`](#insn-00b1b244) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b248`](#insn-00b1b248) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b250`](#insn-00b1b250) → `002a6668`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b254`](#insn-00b1b254) → `002a6678`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b25c`](#insn-00b1b25c) → [`00b1b290`](#insn-00b1b290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b268`](#insn-00b1b268) → [`004882ac`](../00488/004882ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004882ac` · 推定シンボル `None` · 推定型 `None`
- [`00b1b278`](#insn-00b1b278) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b27c`](#insn-00b1b27c) → `002a6668`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b280`](#insn-00b1b280) → [`00b1b244`](#insn-00b1b244) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b284`](#insn-00b1b284) → `002a6678`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b288`](#insn-00b1b288) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b28c`](#insn-00b1b28c) → [`00b1b244`](#insn-00b1b244) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b294`](#insn-00b1b294) → [`00488698`](../00488/00488698.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488698` · 推定シンボル `None` · 推定型 `None`
- [`00b1b2a4`](#insn-00b1b2a4) → `002be3e6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b2a8`](#insn-00b1b2a8) → `002be3ed`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b2ac`](#insn-00b1b2ac) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b2b4`](#insn-00b1b2b4) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b2b8`](#insn-00b1b2b8) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b2bc`](#insn-00b1b2bc) → `Stack[-0x1d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b2c0`](#insn-00b1b2c0) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b2c4`](#insn-00b1b2c4) → `Stack[-0x20f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b2c8`](#insn-00b1b2c8) → `Stack[-0x20b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b2d4`](#insn-00b1b2d4) → [`0048ce94`](../0048c/0048ce94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce94` · 推定シンボル `None` · 推定型 `None`
- [`00b1b2e4`](#insn-00b1b2e4) → [`00492e48`](../00492/00492e48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492e48` · 推定シンボル `None` · 推定型 `None`
- [`00b1b2f8`](#insn-00b1b2f8) → [`00b11188`](../00b11/00b11188.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b11188` · 推定シンボル `None` · 推定型 `None`
- [`00b1b2fc`](#insn-00b1b2fc) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b304`](#insn-00b1b304) → [`00b1b35c`](#insn-00b1b35c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b308`](#insn-00b1b308) → `Stack[-0x240]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b30c`](#insn-00b1b30c) → [`00b1b36c`](#insn-00b1b36c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b310`](#insn-00b1b310) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b314`](#insn-00b1b314) → [`00b1b37c`](#insn-00b1b37c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b318`](#insn-00b1b318) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b31c`](#insn-00b1b31c) → [`00b1b38c`](#insn-00b1b38c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b320`](#insn-00b1b320) → [`00b1b398`](#insn-00b1b398) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b324`](#insn-00b1b324) → [`00b1b3f0`](#insn-00b1b3f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b328`](#insn-00b1b328) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b32c`](#insn-00b1b32c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b330`](#insn-00b1b330) → `Stack[-0x228]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b334`](#insn-00b1b334) → [`00b1b214`](#insn-00b1b214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b338`](#insn-00b1b338) → `Stack[-0x218]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b33c`](#insn-00b1b33c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b340`](#insn-00b1b340) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b344`](#insn-00b1b344) → [`00b1b21c`](#insn-00b1b21c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b348`](#insn-00b1b348) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b34c`](#insn-00b1b34c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b350`](#insn-00b1b350) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b354`](#insn-00b1b354) → [`00b1b224`](#insn-00b1b224) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b358`](#insn-00b1b358) → [`00b1b22c`](#insn-00b1b22c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b35c`](#insn-00b1b35c) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b360`](#insn-00b1b360) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b364`](#insn-00b1b364) → `Stack[-0x240]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b368`](#insn-00b1b368) → [`00b1b310`](#insn-00b1b310) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b36c`](#insn-00b1b36c) → `Stack[-0x230]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b370`](#insn-00b1b370) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b374`](#insn-00b1b374) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b378`](#insn-00b1b378) → [`00b1b318`](#insn-00b1b318) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b37c`](#insn-00b1b37c) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b380`](#insn-00b1b380) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b384`](#insn-00b1b384) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b388`](#insn-00b1b388) → [`00b1b320`](#insn-00b1b320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b38c`](#insn-00b1b38c) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b390`](#insn-00b1b390) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b394`](#insn-00b1b394) → [`00b1b3f0`](#insn-00b1b3f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b3a0`](#insn-00b1b3a0) → [`00b1b3c0`](#insn-00b1b3c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b3a4`](#insn-00b1b3a4) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b3a8`](#insn-00b1b3a8) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b3b0`](#insn-00b1b3b0) → `002a6d40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b3b4`](#insn-00b1b3b4) → `002a6d50`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b3bc`](#insn-00b1b3bc) → [`00b1b3f0`](#insn-00b1b3f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b3c8`](#insn-00b1b3c8) → [`004882ac`](../00488/004882ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004882ac` · 推定シンボル `None` · 推定型 `None`
- [`00b1b3d8`](#insn-00b1b3d8) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b3dc`](#insn-00b1b3dc) → `002a6d40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b3e0`](#insn-00b1b3e0) → [`00b1b3a4`](#insn-00b1b3a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b3e4`](#insn-00b1b3e4) → `002a6d50`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b3e8`](#insn-00b1b3e8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b3ec`](#insn-00b1b3ec) → [`00b1b3a4`](#insn-00b1b3a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b3f4`](#insn-00b1b3f4) → [`00488698`](../00488/00488698.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488698` · 推定シンボル `None` · 推定型 `None`
- [`00b1b404`](#insn-00b1b404) → `002af222`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b40c`](#insn-00b1b40c) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b414`](#insn-00b1b414) → `Stack[-0x1d7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b418`](#insn-00b1b418) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b41c`](#insn-00b1b41c) → `Stack[-0x1d5]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b420`](#insn-00b1b420) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b424`](#insn-00b1b424) → `Stack[-0x20f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b428`](#insn-00b1b428) → `Stack[-0x20b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b434`](#insn-00b1b434) → [`0048ce94`](../0048c/0048ce94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce94` · 推定シンボル `None` · 推定型 `None`
- [`00b1b444`](#insn-00b1b444) → [`00492e48`](../00492/00492e48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492e48` · 推定シンボル `None` · 推定型 `None`
- [`00b1b458`](#insn-00b1b458) → [`00b11188`](../00b11/00b11188.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b11188` · 推定シンボル `None` · 推定型 `None`
- [`00b1b45c`](#insn-00b1b45c) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b464`](#insn-00b1b464) → [`00b1b488`](#insn-00b1b488) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b468`](#insn-00b1b468) → `Stack[-0x258]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b46c`](#insn-00b1b46c) → [`00b1b498`](#insn-00b1b498) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b470`](#insn-00b1b470) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b474`](#insn-00b1b474) → [`00b1b4a8`](#insn-00b1b4a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b478`](#insn-00b1b478) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b47c`](#insn-00b1b47c) → [`00b1b4b8`](#insn-00b1b4b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b480`](#insn-00b1b480) → [`00b1b4c4`](#insn-00b1b4c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b484`](#insn-00b1b484) → [`00b1b51c`](#insn-00b1b51c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b488`](#insn-00b1b488) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b48c`](#insn-00b1b48c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b490`](#insn-00b1b490) → `Stack[-0x258]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b494`](#insn-00b1b494) → [`00b1b470`](#insn-00b1b470) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b498`](#insn-00b1b498) → `Stack[-0x248]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b49c`](#insn-00b1b49c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4a0`](#insn-00b1b4a0) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4a4`](#insn-00b1b4a4) → [`00b1b478`](#insn-00b1b478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4a8`](#insn-00b1b4a8) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4ac`](#insn-00b1b4ac) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4b0`](#insn-00b1b4b0) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4b4`](#insn-00b1b4b4) → [`00b1b480`](#insn-00b1b480) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4b8`](#insn-00b1b4b8) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4bc`](#insn-00b1b4bc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4c0`](#insn-00b1b4c0) → [`00b1b51c`](#insn-00b1b51c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4cc`](#insn-00b1b4cc) → [`00b1b4ec`](#insn-00b1b4ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4d0`](#insn-00b1b4d0) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4d4`](#insn-00b1b4d4) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4dc`](#insn-00b1b4dc) → `002a7418`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b4e0`](#insn-00b1b4e0) → `002a7428`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b4e8`](#insn-00b1b4e8) → [`00b1b51c`](#insn-00b1b51c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b4f4`](#insn-00b1b4f4) → [`004882ac`](../00488/004882ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004882ac` · 推定シンボル `None` · 推定型 `None`
- [`00b1b504`](#insn-00b1b504) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b508`](#insn-00b1b508) → `002a7418`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b50c`](#insn-00b1b50c) → [`00b1b4d0`](#insn-00b1b4d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b510`](#insn-00b1b510) → `002a7428`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b514`](#insn-00b1b514) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b518`](#insn-00b1b518) → [`00b1b4d0`](#insn-00b1b4d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b520`](#insn-00b1b520) → [`00488698`](../00488/00488698.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488698` · 推定シンボル `None` · 推定型 `None`
- [`00b1b530`](#insn-00b1b530) → `002a18b7`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b538`](#insn-00b1b538) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b540`](#insn-00b1b540) → `Stack[-0x1d7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b544`](#insn-00b1b544) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b548`](#insn-00b1b548) → `Stack[-0x1d5]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b54c`](#insn-00b1b54c) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b550`](#insn-00b1b550) → `Stack[-0x20f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b554`](#insn-00b1b554) → `Stack[-0x20b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b560`](#insn-00b1b560) → [`0048ce94`](../0048c/0048ce94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce94` · 推定シンボル `None` · 推定型 `None`
- [`00b1b570`](#insn-00b1b570) → [`00492e48`](../00492/00492e48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492e48` · 推定シンボル `None` · 推定型 `None`
- [`00b1b584`](#insn-00b1b584) → [`00b11188`](../00b11/00b11188.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b11188` · 推定シンボル `None` · 推定型 `None`
- [`00b1b588`](#insn-00b1b588) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b590`](#insn-00b1b590) → [`00b1b5b4`](#insn-00b1b5b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b594`](#insn-00b1b594) → `Stack[-0x270]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b598`](#insn-00b1b598) → [`00b1b5c4`](#insn-00b1b5c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b59c`](#insn-00b1b59c) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5a0`](#insn-00b1b5a0) → [`00b1b5d4`](#insn-00b1b5d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5a4`](#insn-00b1b5a4) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5a8`](#insn-00b1b5a8) → [`00b1b5e4`](#insn-00b1b5e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5ac`](#insn-00b1b5ac) → [`00b1b5f0`](#insn-00b1b5f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5b0`](#insn-00b1b5b0) → [`00b1b64c`](#insn-00b1b64c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5b4`](#insn-00b1b5b4) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5b8`](#insn-00b1b5b8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5bc`](#insn-00b1b5bc) → `Stack[-0x270]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5c0`](#insn-00b1b5c0) → [`00b1b59c`](#insn-00b1b59c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5c4`](#insn-00b1b5c4) → `Stack[-0x260]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5c8`](#insn-00b1b5c8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5cc`](#insn-00b1b5cc) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5d0`](#insn-00b1b5d0) → [`00b1b5a4`](#insn-00b1b5a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5d4`](#insn-00b1b5d4) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5d8`](#insn-00b1b5d8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5dc`](#insn-00b1b5dc) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5e0`](#insn-00b1b5e0) → [`00b1b5ac`](#insn-00b1b5ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5e4`](#insn-00b1b5e4) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5e8`](#insn-00b1b5e8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5ec`](#insn-00b1b5ec) → [`00b1b64c`](#insn-00b1b64c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b5fc`](#insn-00b1b5fc) → [`00b1b61c`](#insn-00b1b61c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b600`](#insn-00b1b600) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b604`](#insn-00b1b604) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b60c`](#insn-00b1b60c) → `002a7b50`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b610`](#insn-00b1b610) → `002a7b60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b618`](#insn-00b1b618) → [`00b1b64c`](#insn-00b1b64c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b624`](#insn-00b1b624) → [`004882ac`](../00488/004882ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004882ac` · 推定シンボル `None` · 推定型 `None`
- [`00b1b634`](#insn-00b1b634) → [`00487aa4`](../00487/00487aa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487aa4` · 推定シンボル `None` · 推定型 `None`
- [`00b1b638`](#insn-00b1b638) → `002a7b50`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b63c`](#insn-00b1b63c) → [`00b1b600`](#insn-00b1b600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b640`](#insn-00b1b640) → `002a7b60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1b644`](#insn-00b1b644) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b648`](#insn-00b1b648) → [`00b1b600`](#insn-00b1b600) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b654`](#insn-00b1b654) → [`00488698`](../00488/00488698.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488698` · 推定シンボル `None` · 推定型 `None`
- [`00b1b664`](#insn-00b1b664) → `00c9ac80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1b668`](#insn-00b1b668) → `00c9ac88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1b66c`](#insn-00b1b66c) → `00c932d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`00b1b674`](#insn-00b1b674) → `00c658e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00b1b674`](#insn-00b1b674) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b678`](#insn-00b1b678) → `00c910e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1b678`](#insn-00b1b678) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b67c`](#insn-00b1b67c) → `00c910c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`00b1b680`](#insn-00b1b680) → `00c932e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`00b1b684`](#insn-00b1b684) → `00c91108`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1b68c`](#insn-00b1b68c) → `00c9ac90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1b690`](#insn-00b1b690) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b698`](#insn-00b1b698) → `00c90cd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00b1b698`](#insn-00b1b698) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b69c`](#insn-00b1b69c) → [`00b1b6a8`](#insn-00b1b6a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6a0`](#insn-00b1b6a0) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6a4`](#insn-00b1b6a4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6ac`](#insn-00b1b6ac) → [`00c58070`](../00c58/00c58070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58070` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6b0`](#insn-00b1b6b0) → `00c932d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`00b1b6b8`](#insn-00b1b6b8) → [`00c58080`](../00c58/00c58080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58080` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6c4`](#insn-00b1b6c4) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6c8`](#insn-00b1b6c8) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6cc`](#insn-00b1b6cc) → [`00b1b6d8`](#insn-00b1b6d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6d0`](#insn-00b1b6d0) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6d4`](#insn-00b1b6d4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6d8`](#insn-00b1b6d8) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6dc`](#insn-00b1b6dc) → [`00b1b6e8`](#insn-00b1b6e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6e0`](#insn-00b1b6e0) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6e4`](#insn-00b1b6e4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6ec`](#insn-00b1b6ec) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6f4`](#insn-00b1b6f4) → [`00b1b880`](#insn-00b1b880) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b6fc`](#insn-00b1b6fc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b700`](#insn-00b1b700) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b704`](#insn-00b1b704) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b708`](#insn-00b1b708) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b70c`](#insn-00b1b70c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1b880`](#insn-00b1b880) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b1aebc`](#insn-00b1aebc)

~~~json
{
  "source": "00b1aebc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1aec0`](#insn-00b1aec0)

~~~json
{
  "source": "00b1aec0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1aec4`](#insn-00b1aec4)

~~~json
{
  "source": "00b1aec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1aec8`](#insn-00b1aec8)

~~~json
{
  "source": "00b1aec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1aecc`](#insn-00b1aecc)

~~~json
{
  "source": "00b1aecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1aee8`](#insn-00b1aee8)

~~~json
{
  "source": "00b1aee8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1aeec`](#insn-00b1aeec)

~~~json
{
  "source": "00b1aeec",
  "target": "00487e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1aef8`](#insn-00b1aef8)

~~~json
{
  "source": "00b1aef8",
  "target": "00c64e08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c64e08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1aef8`](#insn-00b1aef8)

~~~json
{
  "source": "00b1aef8",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af04`](#insn-00b1af04)

~~~json
{
  "source": "00b1af04",
  "target": "00a9c0d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1af18`](#insn-00b1af18)

~~~json
{
  "source": "00b1af18",
  "target": "002c1a6c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c1a6c",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "45445f4d6573736167655f25402e63737600",
  "capture_start": "002c1a6c",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1af1c`](#insn-00b1af1c)

~~~json
{
  "source": "00b1af1c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af28`](#insn-00b1af28)

~~~json
{
  "source": "00b1af28",
  "target": "Stack[-0x20b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af2c`](#insn-00b1af2c)

~~~json
{
  "source": "00b1af2c",
  "target": "Stack[-0x1cf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af38`](#insn-00b1af38)

~~~json
{
  "source": "00b1af38",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af3c`](#insn-00b1af3c)

~~~json
{
  "source": "00b1af3c",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af40`](#insn-00b1af40)

~~~json
{
  "source": "00b1af40",
  "target": "Stack[-0x20f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af4c`](#insn-00b1af4c)

~~~json
{
  "source": "00b1af4c",
  "target": "0048ce94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1af5c`](#insn-00b1af5c)

~~~json
{
  "source": "00b1af5c",
  "target": "00492e48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1af70`](#insn-00b1af70)

~~~json
{
  "source": "00b1af70",
  "target": "00b11188",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1af74`](#insn-00b1af74)

~~~json
{
  "source": "00b1af74",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af7c`](#insn-00b1af7c)

~~~json
{
  "source": "00b1af7c",
  "target": "00b1afa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af80`](#insn-00b1af80)

~~~json
{
  "source": "00b1af80",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af84`](#insn-00b1af84)

~~~json
{
  "source": "00b1af84",
  "target": "00b1afb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af88`](#insn-00b1af88)

~~~json
{
  "source": "00b1af88",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af8c`](#insn-00b1af8c)

~~~json
{
  "source": "00b1af8c",
  "target": "00b1afc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af90`](#insn-00b1af90)

~~~json
{
  "source": "00b1af90",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af94`](#insn-00b1af94)

~~~json
{
  "source": "00b1af94",
  "target": "00b1afd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af98`](#insn-00b1af98)

~~~json
{
  "source": "00b1af98",
  "target": "00b1afdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1af9c`](#insn-00b1af9c)

~~~json
{
  "source": "00b1af9c",
  "target": "00b1b198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afa0`](#insn-00b1afa0)

~~~json
{
  "source": "00b1afa0",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afa4`](#insn-00b1afa4)

~~~json
{
  "source": "00b1afa4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1afa8`](#insn-00b1afa8)

~~~json
{
  "source": "00b1afa8",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afac`](#insn-00b1afac)

~~~json
{
  "source": "00b1afac",
  "target": "00b1af88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afb0`](#insn-00b1afb0)

~~~json
{
  "source": "00b1afb0",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afb4`](#insn-00b1afb4)

~~~json
{
  "source": "00b1afb4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1afb8`](#insn-00b1afb8)

~~~json
{
  "source": "00b1afb8",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afbc`](#insn-00b1afbc)

~~~json
{
  "source": "00b1afbc",
  "target": "00b1af90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afc0`](#insn-00b1afc0)

~~~json
{
  "source": "00b1afc0",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afc4`](#insn-00b1afc4)

~~~json
{
  "source": "00b1afc4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1afc8`](#insn-00b1afc8)

~~~json
{
  "source": "00b1afc8",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afcc`](#insn-00b1afcc)

~~~json
{
  "source": "00b1afcc",
  "target": "00b1af98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afd0`](#insn-00b1afd0)

~~~json
{
  "source": "00b1afd0",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afd4`](#insn-00b1afd4)

~~~json
{
  "source": "00b1afd4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1afd8`](#insn-00b1afd8)

~~~json
{
  "source": "00b1afd8",
  "target": "00b1b198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1afe4`](#insn-00b1afe4)

~~~json
{
  "source": "00b1afe4",
  "target": "004882ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1aff4`](#insn-00b1aff4)

~~~json
{
  "source": "00b1aff4",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b000`](#insn-00b1b000)

~~~json
{
  "source": "00b1b000",
  "target": "0032f6d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f6d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "3c2e5a00a89d0800",
  "capture_start": "0032f6d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b004`](#insn-00b1b004)

~~~json
{
  "source": "00b1b004",
  "target": "00b1b010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b008`](#insn-00b1b008)

~~~json
{
  "source": "00b1b008",
  "target": "0032f6e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f6e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "4c2e5a00d09d0800",
  "capture_start": "0032f6e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b00c`](#insn-00b1b00c)

~~~json
{
  "source": "00b1b00c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b010`](#insn-00b1b010)

~~~json
{
  "source": "00b1b010",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b014`](#insn-00b1b014)

~~~json
{
  "source": "00b1b014",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b018`](#insn-00b1b018)

~~~json
{
  "source": "00b1b018",
  "target": "0032f6d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f6d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "3c2e5a00a89d0800",
  "capture_start": "0032f6d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b01c`](#insn-00b1b01c)

~~~json
{
  "source": "00b1b01c",
  "target": "0032f6e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f6e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "4c2e5a00d09d0800",
  "capture_start": "0032f6e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b02c`](#insn-00b1b02c)

~~~json
{
  "source": "00b1b02c",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b034`](#insn-00b1b034)

~~~json
{
  "source": "00b1b034",
  "target": "0032f6f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f6f0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "542e5a00e49d0800",
  "capture_start": "0032f6f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b038`](#insn-00b1b038)

~~~json
{
  "source": "00b1b038",
  "target": "00b1b044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b03c`](#insn-00b1b03c)

~~~json
{
  "source": "00b1b03c",
  "target": "0032f700",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f700",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c8325a00109e0800",
  "capture_start": "0032f700",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b040`](#insn-00b1b040)

~~~json
{
  "source": "00b1b040",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b044`](#insn-00b1b044)

~~~json
{
  "source": "00b1b044",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b048`](#insn-00b1b048)

~~~json
{
  "source": "00b1b048",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b04c`](#insn-00b1b04c)

~~~json
{
  "source": "00b1b04c",
  "target": "0032f6f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f6f0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "542e5a00e49d0800",
  "capture_start": "0032f6f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b050`](#insn-00b1b050)

~~~json
{
  "source": "00b1b050",
  "target": "0032f700",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f700",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c8325a00109e0800",
  "capture_start": "0032f700",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b060`](#insn-00b1b060)

~~~json
{
  "source": "00b1b060",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b068`](#insn-00b1b068)

~~~json
{
  "source": "00b1b068",
  "target": "0032f708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f708",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "98335a0054a91000",
  "capture_start": "0032f708",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b06c`](#insn-00b1b06c)

~~~json
{
  "source": "00b1b06c",
  "target": "00b1b078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b070`](#insn-00b1b070)

~~~json
{
  "source": "00b1b070",
  "target": "0032f718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f718",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "44385a00589e0800",
  "capture_start": "0032f718",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b074`](#insn-00b1b074)

~~~json
{
  "source": "00b1b074",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b078`](#insn-00b1b078)

~~~json
{
  "source": "00b1b078",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b07c`](#insn-00b1b07c)

~~~json
{
  "source": "00b1b07c",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b080`](#insn-00b1b080)

~~~json
{
  "source": "00b1b080",
  "target": "0032f708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f708",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "98335a0054a91000",
  "capture_start": "0032f708",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b084`](#insn-00b1b084)

~~~json
{
  "source": "00b1b084",
  "target": "0032f718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f718",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "44385a00589e0800",
  "capture_start": "0032f718",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b094`](#insn-00b1b094)

~~~json
{
  "source": "00b1b094",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b09c`](#insn-00b1b09c)

~~~json
{
  "source": "00b1b09c",
  "target": "0032f720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f720",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "90385a00849e0800",
  "capture_start": "0032f720",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b0a0`](#insn-00b1b0a0)

~~~json
{
  "source": "00b1b0a0",
  "target": "00b1b0ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b0a4`](#insn-00b1b0a4)

~~~json
{
  "source": "00b1b0a4",
  "target": "0032f730",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f730",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "0c395a00c49e0800",
  "capture_start": "0032f730",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b0a8`](#insn-00b1b0a8)

~~~json
{
  "source": "00b1b0a8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b0ac`](#insn-00b1b0ac)

~~~json
{
  "source": "00b1b0ac",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b0b0`](#insn-00b1b0b0)

~~~json
{
  "source": "00b1b0b0",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b0b4`](#insn-00b1b0b4)

~~~json
{
  "source": "00b1b0b4",
  "target": "0032f720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f720",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "90385a00849e0800",
  "capture_start": "0032f720",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b0b8`](#insn-00b1b0b8)

~~~json
{
  "source": "00b1b0b8",
  "target": "0032f730",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f730",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "0c395a00c49e0800",
  "capture_start": "0032f730",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b0c4`](#insn-00b1b0c4)

~~~json
{
  "source": "00b1b0c4",
  "target": "004882ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b0d4`](#insn-00b1b0d4)

~~~json
{
  "source": "00b1b0d4",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b0dc`](#insn-00b1b0dc)

~~~json
{
  "source": "00b1b0dc",
  "target": "0032f738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f738",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "14395a00d89e0800",
  "capture_start": "0032f738",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b0e0`](#insn-00b1b0e0)

~~~json
{
  "source": "00b1b0e0",
  "target": "00b1b0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b0e4`](#insn-00b1b0e4)

~~~json
{
  "source": "00b1b0e4",
  "target": "0032f748",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f748",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "483b5a00189f0800",
  "capture_start": "0032f748",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b0e8`](#insn-00b1b0e8)

~~~json
{
  "source": "00b1b0e8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b0ec`](#insn-00b1b0ec)

~~~json
{
  "source": "00b1b0ec",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b0f0`](#insn-00b1b0f0)

~~~json
{
  "source": "00b1b0f0",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b0f4`](#insn-00b1b0f4)

~~~json
{
  "source": "00b1b0f4",
  "target": "0032f738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f738",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "14395a00d89e0800",
  "capture_start": "0032f738",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b0f8`](#insn-00b1b0f8)

~~~json
{
  "source": "00b1b0f8",
  "target": "0032f748",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f748",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "483b5a00189f0800",
  "capture_start": "0032f748",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b108`](#insn-00b1b108)

~~~json
{
  "source": "00b1b108",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b110`](#insn-00b1b110)

~~~json
{
  "source": "00b1b110",
  "target": "0032f750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f750",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "1c3c5a00e4a91000",
  "capture_start": "0032f750",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b114`](#insn-00b1b114)

~~~json
{
  "source": "00b1b114",
  "target": "00b1b120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b118`](#insn-00b1b118)

~~~json
{
  "source": "00b1b118",
  "target": "0032f760",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f760",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "00425a00449f0800",
  "capture_start": "0032f760",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b11c`](#insn-00b1b11c)

~~~json
{
  "source": "00b1b11c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b120`](#insn-00b1b120)

~~~json
{
  "source": "00b1b120",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b124`](#insn-00b1b124)

~~~json
{
  "source": "00b1b124",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b128`](#insn-00b1b128)

~~~json
{
  "source": "00b1b128",
  "target": "0032f750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f750",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "1c3c5a00e4a91000",
  "capture_start": "0032f750",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b12c`](#insn-00b1b12c)

~~~json
{
  "source": "00b1b12c",
  "target": "0032f760",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f760",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "00425a00449f0800",
  "capture_start": "0032f760",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b13c`](#insn-00b1b13c)

~~~json
{
  "source": "00b1b13c",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b144`](#insn-00b1b144)

~~~json
{
  "source": "00b1b144",
  "target": "0032f768",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f768",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "50425a0078aa1000",
  "capture_start": "0032f768",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b148`](#insn-00b1b148)

~~~json
{
  "source": "00b1b148",
  "target": "00b1b154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b14c`](#insn-00b1b14c)

~~~json
{
  "source": "00b1b14c",
  "target": "0032f778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f778",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "74505a00c09f0800",
  "capture_start": "0032f778",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b150`](#insn-00b1b150)

~~~json
{
  "source": "00b1b150",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b154`](#insn-00b1b154)

~~~json
{
  "source": "00b1b154",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b158`](#insn-00b1b158)

~~~json
{
  "source": "00b1b158",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b15c`](#insn-00b1b15c)

~~~json
{
  "source": "00b1b15c",
  "target": "0032f768",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f768",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "50425a0078aa1000",
  "capture_start": "0032f768",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b160`](#insn-00b1b160)

~~~json
{
  "source": "00b1b160",
  "target": "0032f778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f778",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "74505a00c09f0800",
  "capture_start": "0032f778",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b170`](#insn-00b1b170)

~~~json
{
  "source": "00b1b170",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b178`](#insn-00b1b178)

~~~json
{
  "source": "00b1b178",
  "target": "0032f780",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f780",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "00515a00ec9f0800",
  "capture_start": "0032f780",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b17c`](#insn-00b1b17c)

~~~json
{
  "source": "00b1b17c",
  "target": "00b1b188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b180`](#insn-00b1b180)

~~~json
{
  "source": "00b1b180",
  "target": "0032f790",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f790",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "94515a002ca00800",
  "capture_start": "0032f790",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b184`](#insn-00b1b184)

~~~json
{
  "source": "00b1b184",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b188`](#insn-00b1b188)

~~~json
{
  "source": "00b1b188",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b18c`](#insn-00b1b18c)

~~~json
{
  "source": "00b1b18c",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b190`](#insn-00b1b190)

~~~json
{
  "source": "00b1b190",
  "target": "0032f780",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f780",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "00515a00ec9f0800",
  "capture_start": "0032f780",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b194`](#insn-00b1b194)

~~~json
{
  "source": "00b1b194",
  "target": "0032f790",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f790",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "94515a002ca00800",
  "capture_start": "0032f790",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b19c`](#insn-00b1b19c)

~~~json
{
  "source": "00b1b19c",
  "target": "00488698",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b1ac`](#insn-00b1b1ac)

~~~json
{
  "source": "00b1b1ac",
  "target": "002a6f75",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6f75",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "4f505f25402e63737600",
  "capture_start": "002a6f75",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b1b4`](#insn-00b1b1b4)

~~~json
{
  "source": "00b1b1b4",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b1bc`](#insn-00b1b1bc)

~~~json
{
  "source": "00b1b1bc",
  "target": "Stack[-0x1d7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b1c0`](#insn-00b1b1c0)

~~~json
{
  "source": "00b1b1c0",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b1c4`](#insn-00b1b1c4)

~~~json
{
  "source": "00b1b1c4",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b1c8`](#insn-00b1b1c8)

~~~json
{
  "source": "00b1b1c8",
  "target": "Stack[-0x20f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b1cc`](#insn-00b1b1cc)

~~~json
{
  "source": "00b1b1cc",
  "target": "Stack[-0x20b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b1d8`](#insn-00b1b1d8)

~~~json
{
  "source": "00b1b1d8",
  "target": "0048ce94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b1e8`](#insn-00b1b1e8)

~~~json
{
  "source": "00b1b1e8",
  "target": "00492e48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b1fc`](#insn-00b1b1fc)

~~~json
{
  "source": "00b1b1fc",
  "target": "00b11188",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b200`](#insn-00b1b200)

~~~json
{
  "source": "00b1b200",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b208`](#insn-00b1b208)

~~~json
{
  "source": "00b1b208",
  "target": "00b1b328",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b20c`](#insn-00b1b20c)

~~~json
{
  "source": "00b1b20c",
  "target": "Stack[-0x228]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b210`](#insn-00b1b210)

~~~json
{
  "source": "00b1b210",
  "target": "00b1b338",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b214`](#insn-00b1b214)

~~~json
{
  "source": "00b1b214",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b218`](#insn-00b1b218)

~~~json
{
  "source": "00b1b218",
  "target": "00b1b348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b21c`](#insn-00b1b21c)

~~~json
{
  "source": "00b1b21c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b220`](#insn-00b1b220)

~~~json
{
  "source": "00b1b220",
  "target": "00b1b22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b224`](#insn-00b1b224)

~~~json
{
  "source": "00b1b224",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b228`](#insn-00b1b228)

~~~json
{
  "source": "00b1b228",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b234`](#insn-00b1b234)

~~~json
{
  "source": "00b1b234",
  "target": "00b1b290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b240`](#insn-00b1b240)

~~~json
{
  "source": "00b1b240",
  "target": "00b1b260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b244`](#insn-00b1b244)

~~~json
{
  "source": "00b1b244",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b248`](#insn-00b1b248)

~~~json
{
  "source": "00b1b248",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b250`](#insn-00b1b250)

~~~json
{
  "source": "00b1b250",
  "target": "002a6668",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6644",
  "offset": 36,
  "size": 43,
  "datatype": "string",
  "bytes": "5369676e6174757265206f6e204f43535020726573706f6e7365207761732066",
  "capture_start": "002a6644",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b1b254`](#insn-00b1b254)

~~~json
{
  "source": "00b1b254",
  "target": "002a6678",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a666f",
  "offset": 9,
  "size": 29,
  "datatype": "string",
  "bytes": "4365727469666963617465206973206e6f74207965742076616c696400",
  "capture_start": "002a666f",
  "capture_bytes": 29,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b25c`](#insn-00b1b25c)

~~~json
{
  "source": "00b1b25c",
  "target": "00b1b290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b268`](#insn-00b1b268)

~~~json
{
  "source": "00b1b268",
  "target": "004882ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b278`](#insn-00b1b278)

~~~json
{
  "source": "00b1b278",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b27c`](#insn-00b1b27c)

~~~json
{
  "source": "00b1b27c",
  "target": "002a6668",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6644",
  "offset": 36,
  "size": 43,
  "datatype": "string",
  "bytes": "5369676e6174757265206f6e204f43535020726573706f6e7365207761732066",
  "capture_start": "002a6644",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b1b280`](#insn-00b1b280)

~~~json
{
  "source": "00b1b280",
  "target": "00b1b244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b284`](#insn-00b1b284)

~~~json
{
  "source": "00b1b284",
  "target": "002a6678",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a666f",
  "offset": 9,
  "size": 29,
  "datatype": "string",
  "bytes": "4365727469666963617465206973206e6f74207965742076616c696400",
  "capture_start": "002a666f",
  "capture_bytes": 29,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b288`](#insn-00b1b288)

~~~json
{
  "source": "00b1b288",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b28c`](#insn-00b1b28c)

~~~json
{
  "source": "00b1b28c",
  "target": "00b1b244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b294`](#insn-00b1b294)

~~~json
{
  "source": "00b1b294",
  "target": "00488698",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b2a4`](#insn-00b1b2a4)

~~~json
{
  "source": "00b1b2a4",
  "target": "002be3e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be3e6",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "4f504c6567656e645f25402e63737600",
  "capture_start": "002be3e6",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b2a8`](#insn-00b1b2a8)

~~~json
{
  "source": "00b1b2a8",
  "target": "002be3ed",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be3e6",
  "offset": 7,
  "size": 16,
  "datatype": "string",
  "bytes": "4f504c6567656e645f25402e63737600",
  "capture_start": "002be3e6",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b2ac`](#insn-00b1b2ac)

~~~json
{
  "source": "00b1b2ac",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b2b4`](#insn-00b1b2b4)

~~~json
{
  "source": "00b1b2b4",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b2b8`](#insn-00b1b2b8)

~~~json
{
  "source": "00b1b2b8",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b2bc`](#insn-00b1b2bc)

~~~json
{
  "source": "00b1b2bc",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b2c0`](#insn-00b1b2c0)

~~~json
{
  "source": "00b1b2c0",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b2c4`](#insn-00b1b2c4)

~~~json
{
  "source": "00b1b2c4",
  "target": "Stack[-0x20f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b2c8`](#insn-00b1b2c8)

~~~json
{
  "source": "00b1b2c8",
  "target": "Stack[-0x20b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b2d4`](#insn-00b1b2d4)

~~~json
{
  "source": "00b1b2d4",
  "target": "0048ce94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b2e4`](#insn-00b1b2e4)

~~~json
{
  "source": "00b1b2e4",
  "target": "00492e48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b2f8`](#insn-00b1b2f8)

~~~json
{
  "source": "00b1b2f8",
  "target": "00b11188",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b2fc`](#insn-00b1b2fc)

~~~json
{
  "source": "00b1b2fc",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b304`](#insn-00b1b304)

~~~json
{
  "source": "00b1b304",
  "target": "00b1b35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b308`](#insn-00b1b308)

~~~json
{
  "source": "00b1b308",
  "target": "Stack[-0x240]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b30c`](#insn-00b1b30c)

~~~json
{
  "source": "00b1b30c",
  "target": "00b1b36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b310`](#insn-00b1b310)

~~~json
{
  "source": "00b1b310",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b314`](#insn-00b1b314)

~~~json
{
  "source": "00b1b314",
  "target": "00b1b37c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b318`](#insn-00b1b318)

~~~json
{
  "source": "00b1b318",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b31c`](#insn-00b1b31c)

~~~json
{
  "source": "00b1b31c",
  "target": "00b1b38c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b320`](#insn-00b1b320)

~~~json
{
  "source": "00b1b320",
  "target": "00b1b398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b324`](#insn-00b1b324)

~~~json
{
  "source": "00b1b324",
  "target": "00b1b3f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b328`](#insn-00b1b328)

~~~json
{
  "source": "00b1b328",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b32c`](#insn-00b1b32c)

~~~json
{
  "source": "00b1b32c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b330`](#insn-00b1b330)

~~~json
{
  "source": "00b1b330",
  "target": "Stack[-0x228]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b334`](#insn-00b1b334)

~~~json
{
  "source": "00b1b334",
  "target": "00b1b214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b338`](#insn-00b1b338)

~~~json
{
  "source": "00b1b338",
  "target": "Stack[-0x218]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b33c`](#insn-00b1b33c)

~~~json
{
  "source": "00b1b33c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b340`](#insn-00b1b340)

~~~json
{
  "source": "00b1b340",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b344`](#insn-00b1b344)

~~~json
{
  "source": "00b1b344",
  "target": "00b1b21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b348`](#insn-00b1b348)

~~~json
{
  "source": "00b1b348",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b34c`](#insn-00b1b34c)

~~~json
{
  "source": "00b1b34c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b350`](#insn-00b1b350)

~~~json
{
  "source": "00b1b350",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b354`](#insn-00b1b354)

~~~json
{
  "source": "00b1b354",
  "target": "00b1b224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b358`](#insn-00b1b358)

~~~json
{
  "source": "00b1b358",
  "target": "00b1b22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b35c`](#insn-00b1b35c)

~~~json
{
  "source": "00b1b35c",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b360`](#insn-00b1b360)

~~~json
{
  "source": "00b1b360",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b364`](#insn-00b1b364)

~~~json
{
  "source": "00b1b364",
  "target": "Stack[-0x240]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b368`](#insn-00b1b368)

~~~json
{
  "source": "00b1b368",
  "target": "00b1b310",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b36c`](#insn-00b1b36c)

~~~json
{
  "source": "00b1b36c",
  "target": "Stack[-0x230]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b370`](#insn-00b1b370)

~~~json
{
  "source": "00b1b370",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b374`](#insn-00b1b374)

~~~json
{
  "source": "00b1b374",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b378`](#insn-00b1b378)

~~~json
{
  "source": "00b1b378",
  "target": "00b1b318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b37c`](#insn-00b1b37c)

~~~json
{
  "source": "00b1b37c",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b380`](#insn-00b1b380)

~~~json
{
  "source": "00b1b380",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b384`](#insn-00b1b384)

~~~json
{
  "source": "00b1b384",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b388`](#insn-00b1b388)

~~~json
{
  "source": "00b1b388",
  "target": "00b1b320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b38c`](#insn-00b1b38c)

~~~json
{
  "source": "00b1b38c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b390`](#insn-00b1b390)

~~~json
{
  "source": "00b1b390",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b394`](#insn-00b1b394)

~~~json
{
  "source": "00b1b394",
  "target": "00b1b3f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b3a0`](#insn-00b1b3a0)

~~~json
{
  "source": "00b1b3a0",
  "target": "00b1b3c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b3a4`](#insn-00b1b3a4)

~~~json
{
  "source": "00b1b3a4",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b3a8`](#insn-00b1b3a8)

~~~json
{
  "source": "00b1b3a8",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b3b0`](#insn-00b1b3b0)

~~~json
{
  "source": "00b1b3b0",
  "target": "002a6d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6d3d",
  "offset": 3,
  "size": 30,
  "datatype": "string",
  "bytes": "73657456697369626c652827636c6561725f6e61303030272c2025732900",
  "capture_start": "002a6d3d",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b3b4`](#insn-00b1b3b4)

~~~json
{
  "source": "00b1b3b4",
  "target": "002a6d50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6d3d",
  "offset": 19,
  "size": 30,
  "datatype": "string",
  "bytes": "73657456697369626c652827636c6561725f6e61303030272c2025732900",
  "capture_start": "002a6d3d",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b3bc`](#insn-00b1b3bc)

~~~json
{
  "source": "00b1b3bc",
  "target": "00b1b3f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b3c8`](#insn-00b1b3c8)

~~~json
{
  "source": "00b1b3c8",
  "target": "004882ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b3d8`](#insn-00b1b3d8)

~~~json
{
  "source": "00b1b3d8",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b3dc`](#insn-00b1b3dc)

~~~json
{
  "source": "00b1b3dc",
  "target": "002a6d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6d3d",
  "offset": 3,
  "size": 30,
  "datatype": "string",
  "bytes": "73657456697369626c652827636c6561725f6e61303030272c2025732900",
  "capture_start": "002a6d3d",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b3e0`](#insn-00b1b3e0)

~~~json
{
  "source": "00b1b3e0",
  "target": "00b1b3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b3e4`](#insn-00b1b3e4)

~~~json
{
  "source": "00b1b3e4",
  "target": "002a6d50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6d3d",
  "offset": 19,
  "size": 30,
  "datatype": "string",
  "bytes": "73657456697369626c652827636c6561725f6e61303030272c2025732900",
  "capture_start": "002a6d3d",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b3e8`](#insn-00b1b3e8)

~~~json
{
  "source": "00b1b3e8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b3ec`](#insn-00b1b3ec)

~~~json
{
  "source": "00b1b3ec",
  "target": "00b1b3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b3f4`](#insn-00b1b3f4)

~~~json
{
  "source": "00b1b3f4",
  "target": "00488698",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b404`](#insn-00b1b404)

~~~json
{
  "source": "00b1b404",
  "target": "002af222",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af222",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "4f50325f25402e63737600",
  "capture_start": "002af222",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b40c`](#insn-00b1b40c)

~~~json
{
  "source": "00b1b40c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b414`](#insn-00b1b414)

~~~json
{
  "source": "00b1b414",
  "target": "Stack[-0x1d7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b418`](#insn-00b1b418)

~~~json
{
  "source": "00b1b418",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b41c`](#insn-00b1b41c)

~~~json
{
  "source": "00b1b41c",
  "target": "Stack[-0x1d5]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b420`](#insn-00b1b420)

~~~json
{
  "source": "00b1b420",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b424`](#insn-00b1b424)

~~~json
{
  "source": "00b1b424",
  "target": "Stack[-0x20f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b428`](#insn-00b1b428)

~~~json
{
  "source": "00b1b428",
  "target": "Stack[-0x20b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b434`](#insn-00b1b434)

~~~json
{
  "source": "00b1b434",
  "target": "0048ce94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b444`](#insn-00b1b444)

~~~json
{
  "source": "00b1b444",
  "target": "00492e48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b458`](#insn-00b1b458)

~~~json
{
  "source": "00b1b458",
  "target": "00b11188",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b45c`](#insn-00b1b45c)

~~~json
{
  "source": "00b1b45c",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b464`](#insn-00b1b464)

~~~json
{
  "source": "00b1b464",
  "target": "00b1b488",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b468`](#insn-00b1b468)

~~~json
{
  "source": "00b1b468",
  "target": "Stack[-0x258]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b46c`](#insn-00b1b46c)

~~~json
{
  "source": "00b1b46c",
  "target": "00b1b498",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b470`](#insn-00b1b470)

~~~json
{
  "source": "00b1b470",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b474`](#insn-00b1b474)

~~~json
{
  "source": "00b1b474",
  "target": "00b1b4a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b478`](#insn-00b1b478)

~~~json
{
  "source": "00b1b478",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b47c`](#insn-00b1b47c)

~~~json
{
  "source": "00b1b47c",
  "target": "00b1b4b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b480`](#insn-00b1b480)

~~~json
{
  "source": "00b1b480",
  "target": "00b1b4c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b484`](#insn-00b1b484)

~~~json
{
  "source": "00b1b484",
  "target": "00b1b51c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b488`](#insn-00b1b488)

~~~json
{
  "source": "00b1b488",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b48c`](#insn-00b1b48c)

~~~json
{
  "source": "00b1b48c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b490`](#insn-00b1b490)

~~~json
{
  "source": "00b1b490",
  "target": "Stack[-0x258]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b494`](#insn-00b1b494)

~~~json
{
  "source": "00b1b494",
  "target": "00b1b470",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b498`](#insn-00b1b498)

~~~json
{
  "source": "00b1b498",
  "target": "Stack[-0x248]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b49c`](#insn-00b1b49c)

~~~json
{
  "source": "00b1b49c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b4a0`](#insn-00b1b4a0)

~~~json
{
  "source": "00b1b4a0",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b4a4`](#insn-00b1b4a4)

~~~json
{
  "source": "00b1b4a4",
  "target": "00b1b478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b4a8`](#insn-00b1b4a8)

~~~json
{
  "source": "00b1b4a8",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b4ac`](#insn-00b1b4ac)

~~~json
{
  "source": "00b1b4ac",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b4b0`](#insn-00b1b4b0)

~~~json
{
  "source": "00b1b4b0",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b4b4`](#insn-00b1b4b4)

~~~json
{
  "source": "00b1b4b4",
  "target": "00b1b480",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b4b8`](#insn-00b1b4b8)

~~~json
{
  "source": "00b1b4b8",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b4bc`](#insn-00b1b4bc)

~~~json
{
  "source": "00b1b4bc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b4c0`](#insn-00b1b4c0)

~~~json
{
  "source": "00b1b4c0",
  "target": "00b1b51c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b4cc`](#insn-00b1b4cc)

~~~json
{
  "source": "00b1b4cc",
  "target": "00b1b4ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b4d0`](#insn-00b1b4d0)

~~~json
{
  "source": "00b1b4d0",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b4d4`](#insn-00b1b4d4)

~~~json
{
  "source": "00b1b4d4",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b4dc`](#insn-00b1b4dc)

~~~json
{
  "source": "00b1b4dc",
  "target": "002a7418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a73f0",
  "offset": 40,
  "size": 57,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f4669726562617365",
  "capture_start": "002a73f0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b1b4e0`](#insn-00b1b4e0)

~~~json
{
  "source": "00b1b4e0",
  "target": "002a7428",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a73f0",
  "offset": 56,
  "size": 57,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f4669726562617365",
  "capture_start": "002a73f0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b1b4e8`](#insn-00b1b4e8)

~~~json
{
  "source": "00b1b4e8",
  "target": "00b1b51c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b4f4`](#insn-00b1b4f4)

~~~json
{
  "source": "00b1b4f4",
  "target": "004882ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b504`](#insn-00b1b504)

~~~json
{
  "source": "00b1b504",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b508`](#insn-00b1b508)

~~~json
{
  "source": "00b1b508",
  "target": "002a7418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a73f0",
  "offset": 40,
  "size": 57,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f4669726562617365",
  "capture_start": "002a73f0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b1b50c`](#insn-00b1b50c)

~~~json
{
  "source": "00b1b50c",
  "target": "00b1b4d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b510`](#insn-00b1b510)

~~~json
{
  "source": "00b1b510",
  "target": "002a7428",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a73f0",
  "offset": 56,
  "size": 57,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f4669726562617365",
  "capture_start": "002a73f0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b1b514`](#insn-00b1b514)

~~~json
{
  "source": "00b1b514",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b518`](#insn-00b1b518)

~~~json
{
  "source": "00b1b518",
  "target": "00b1b4d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b520`](#insn-00b1b520)

~~~json
{
  "source": "00b1b520",
  "target": "00488698",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b530`](#insn-00b1b530)

~~~json
{
  "source": "00b1b530",
  "target": "002a18b7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a18b7",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "4f50335f25402e63737600",
  "capture_start": "002a18b7",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b538`](#insn-00b1b538)

~~~json
{
  "source": "00b1b538",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b540`](#insn-00b1b540)

~~~json
{
  "source": "00b1b540",
  "target": "Stack[-0x1d7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b544`](#insn-00b1b544)

~~~json
{
  "source": "00b1b544",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b548`](#insn-00b1b548)

~~~json
{
  "source": "00b1b548",
  "target": "Stack[-0x1d5]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b54c`](#insn-00b1b54c)

~~~json
{
  "source": "00b1b54c",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b550`](#insn-00b1b550)

~~~json
{
  "source": "00b1b550",
  "target": "Stack[-0x20f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b554`](#insn-00b1b554)

~~~json
{
  "source": "00b1b554",
  "target": "Stack[-0x20b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b560`](#insn-00b1b560)

~~~json
{
  "source": "00b1b560",
  "target": "0048ce94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b570`](#insn-00b1b570)

~~~json
{
  "source": "00b1b570",
  "target": "00492e48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b584`](#insn-00b1b584)

~~~json
{
  "source": "00b1b584",
  "target": "00b11188",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b588`](#insn-00b1b588)

~~~json
{
  "source": "00b1b588",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b590`](#insn-00b1b590)

~~~json
{
  "source": "00b1b590",
  "target": "00b1b5b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b594`](#insn-00b1b594)

~~~json
{
  "source": "00b1b594",
  "target": "Stack[-0x270]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b598`](#insn-00b1b598)

~~~json
{
  "source": "00b1b598",
  "target": "00b1b5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b59c`](#insn-00b1b59c)

~~~json
{
  "source": "00b1b59c",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5a0`](#insn-00b1b5a0)

~~~json
{
  "source": "00b1b5a0",
  "target": "00b1b5d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5a4`](#insn-00b1b5a4)

~~~json
{
  "source": "00b1b5a4",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5a8`](#insn-00b1b5a8)

~~~json
{
  "source": "00b1b5a8",
  "target": "00b1b5e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5ac`](#insn-00b1b5ac)

~~~json
{
  "source": "00b1b5ac",
  "target": "00b1b5f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5b0`](#insn-00b1b5b0)

~~~json
{
  "source": "00b1b5b0",
  "target": "00b1b64c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5b4`](#insn-00b1b5b4)

~~~json
{
  "source": "00b1b5b4",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5b8`](#insn-00b1b5b8)

~~~json
{
  "source": "00b1b5b8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b5bc`](#insn-00b1b5bc)

~~~json
{
  "source": "00b1b5bc",
  "target": "Stack[-0x270]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5c0`](#insn-00b1b5c0)

~~~json
{
  "source": "00b1b5c0",
  "target": "00b1b59c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5c4`](#insn-00b1b5c4)

~~~json
{
  "source": "00b1b5c4",
  "target": "Stack[-0x260]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5c8`](#insn-00b1b5c8)

~~~json
{
  "source": "00b1b5c8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b5cc`](#insn-00b1b5cc)

~~~json
{
  "source": "00b1b5cc",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5d0`](#insn-00b1b5d0)

~~~json
{
  "source": "00b1b5d0",
  "target": "00b1b5a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5d4`](#insn-00b1b5d4)

~~~json
{
  "source": "00b1b5d4",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5d8`](#insn-00b1b5d8)

~~~json
{
  "source": "00b1b5d8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b5dc`](#insn-00b1b5dc)

~~~json
{
  "source": "00b1b5dc",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5e0`](#insn-00b1b5e0)

~~~json
{
  "source": "00b1b5e0",
  "target": "00b1b5ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5e4`](#insn-00b1b5e4)

~~~json
{
  "source": "00b1b5e4",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5e8`](#insn-00b1b5e8)

~~~json
{
  "source": "00b1b5e8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b5ec`](#insn-00b1b5ec)

~~~json
{
  "source": "00b1b5ec",
  "target": "00b1b64c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b5fc`](#insn-00b1b5fc)

~~~json
{
  "source": "00b1b5fc",
  "target": "00b1b61c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b600`](#insn-00b1b600)

~~~json
{
  "source": "00b1b600",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b604`](#insn-00b1b604)

~~~json
{
  "source": "00b1b604",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b60c`](#insn-00b1b60c)

~~~json
{
  "source": "00b1b60c",
  "target": "002a7b50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7b4b",
  "offset": 5,
  "size": 15,
  "datatype": "string",
  "bytes": "4761747961496e69745b455d5f5300",
  "capture_start": "002a7b4b",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b610`](#insn-00b1b610)

~~~json
{
  "source": "00b1b610",
  "target": "002a7b60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7b5a",
  "offset": 6,
  "size": 33,
  "datatype": "string",
  "bytes": "65766f6c7665416e696d6174696f6e5f5468697264466f726d2e6d61616e696d",
  "capture_start": "002a7b5a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b1b618`](#insn-00b1b618)

~~~json
{
  "source": "00b1b618",
  "target": "00b1b64c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b624`](#insn-00b1b624)

~~~json
{
  "source": "00b1b624",
  "target": "004882ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b634`](#insn-00b1b634)

~~~json
{
  "source": "00b1b634",
  "target": "00487aa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b638`](#insn-00b1b638)

~~~json
{
  "source": "00b1b638",
  "target": "002a7b50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7b4b",
  "offset": 5,
  "size": 15,
  "datatype": "string",
  "bytes": "4761747961496e69745b455d5f5300",
  "capture_start": "002a7b4b",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b63c`](#insn-00b1b63c)

~~~json
{
  "source": "00b1b63c",
  "target": "00b1b600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b640`](#insn-00b1b640)

~~~json
{
  "source": "00b1b640",
  "target": "002a7b60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7b5a",
  "offset": 6,
  "size": 33,
  "datatype": "string",
  "bytes": "65766f6c7665416e696d6174696f6e5f5468697264466f726d2e6d61616e696d",
  "capture_start": "002a7b5a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b1b644`](#insn-00b1b644)

~~~json
{
  "source": "00b1b644",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b648`](#insn-00b1b648)

~~~json
{
  "source": "00b1b648",
  "target": "00b1b600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b654`](#insn-00b1b654)

~~~json
{
  "source": "00b1b654",
  "target": "00488698",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b664`](#insn-00b1b664)

~~~json
{
  "source": "00b1b664",
  "target": "00c9ac80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1b668`](#insn-00b1b668)

~~~json
{
  "source": "00b1b668",
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
- 参照命令 [`00b1b66c`](#insn-00b1b66c)

~~~json
{
  "source": "00b1b66c",
  "target": "00c932d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1b674`](#insn-00b1b674)

~~~json
{
  "source": "00b1b674",
  "target": "00c658e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c658e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1b674`](#insn-00b1b674)

~~~json
{
  "source": "00b1b674",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b678`](#insn-00b1b678)

~~~json
{
  "source": "00b1b678",
  "target": "00c910e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c910e0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1b678`](#insn-00b1b678)

~~~json
{
  "source": "00b1b678",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b67c`](#insn-00b1b67c)

~~~json
{
  "source": "00b1b67c",
  "target": "00c910c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c910c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c910c8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1b680`](#insn-00b1b680)

~~~json
{
  "source": "00b1b680",
  "target": "00c932e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1b684`](#insn-00b1b684)

~~~json
{
  "source": "00b1b684",
  "target": "00c91108",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91108",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1b68c`](#insn-00b1b68c)

~~~json
{
  "source": "00b1b68c",
  "target": "00c9ac90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1b690`](#insn-00b1b690)

~~~json
{
  "source": "00b1b690",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b698`](#insn-00b1b698)

~~~json
{
  "source": "00b1b698",
  "target": "00c90cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90cc8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00b1b698`](#insn-00b1b698)

~~~json
{
  "source": "00b1b698",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b69c`](#insn-00b1b69c)

~~~json
{
  "source": "00b1b69c",
  "target": "00b1b6a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b6a0`](#insn-00b1b6a0)

~~~json
{
  "source": "00b1b6a0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b6a4`](#insn-00b1b6a4)

~~~json
{
  "source": "00b1b6a4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b6ac`](#insn-00b1b6ac)

~~~json
{
  "source": "00b1b6ac",
  "target": "00c58070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b6b0`](#insn-00b1b6b0)

~~~json
{
  "source": "00b1b6b0",
  "target": "00c932d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1b6b8`](#insn-00b1b6b8)

~~~json
{
  "source": "00b1b6b8",
  "target": "00c58080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b6c4`](#insn-00b1b6c4)

~~~json
{
  "source": "00b1b6c4",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b6c8`](#insn-00b1b6c8)

~~~json
{
  "source": "00b1b6c8",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b6cc`](#insn-00b1b6cc)

~~~json
{
  "source": "00b1b6cc",
  "target": "00b1b6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b6d0`](#insn-00b1b6d0)

~~~json
{
  "source": "00b1b6d0",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b6d4`](#insn-00b1b6d4)

~~~json
{
  "source": "00b1b6d4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b6d8`](#insn-00b1b6d8)

~~~json
{
  "source": "00b1b6d8",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b6dc`](#insn-00b1b6dc)

~~~json
{
  "source": "00b1b6dc",
  "target": "00b1b6e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b6e0`](#insn-00b1b6e0)

~~~json
{
  "source": "00b1b6e0",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b6e4`](#insn-00b1b6e4)

~~~json
{
  "source": "00b1b6e4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1b6ec`](#insn-00b1b6ec)

~~~json
{
  "source": "00b1b6ec",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b6f4`](#insn-00b1b6f4)

~~~json
{
  "source": "00b1b6f4",
  "target": "00b1b880",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b6fc`](#insn-00b1b6fc)

~~~json
{
  "source": "00b1b6fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b700`](#insn-00b1b700)

~~~json
{
  "source": "00b1b700",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b704`](#insn-00b1b704)

~~~json
{
  "source": "00b1b704",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b708`](#insn-00b1b708)

~~~json
{
  "source": "00b1b708",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b70c`](#insn-00b1b70c)

~~~json
{
  "source": "00b1b70c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1b880`](#insn-00b1b880)

~~~json
{
  "source": "00b1b880",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
