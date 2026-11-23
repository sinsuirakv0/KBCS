# 00bbcbcc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbcb04`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbc/00bbcb04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-8d3324f0831d8f66f3bd556af7f8e7a8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbcc10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcc10.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-00ba1c9454457b90313a1e24325147fa)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcbcc",
  "name": "__cxa_demangle",
  "size": 1452,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "837f0bb18cedd6ea1c0c360341ca28442e7b49a70eb6372d422578b273d9e241",
  "source_text_sha256": "837f0bb18cedd6ea1c0c360341ca28442e7b49a70eb6372d422578b273d9e241",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbcbcc",
        "00bbd177"
      ]
    ],
    "bytes_sha256": "248da98d9b001b5238600b49c28eb7bead98b43963bc45cdb1524b35e77a81d6",
    "instruction_count": 363,
    "instruction_bytes": 1452,
    "body_bytes": 1452,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00be1de0](../00be1/00be1de0.md)

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)
- [00bbd2c4](../00bbd/00bbd2c4.md)
- [00bbdd64](../00bbd/00bbdd64.md)
- [00bbde18](../00bbd/00bbde18.md)
- [00bdb140](../00bdb/00bdb140.md)
- [00bdb180](../00bdb/00bdb180.md)
- [00bdb7c0](../00bdb/00bdb7c0.md)
- [00bdd180](../00bdd/00bdd180.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

## 関連文字列（未確認候補）

~~~text
"%s:%d: %s"
"invocation function for block in "
"out/llvm-project/libcxxabi/src/cxa_demangle.cpp"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 14565 bytes

~~~c

void * __cxa_demangle(byte *param_1,void *param_2,ulong *param_3,undefined4 *param_4)

{
  byte bVar1;
  long *plVar2;
  bool bVar3;
  size_t sVar4;
  long *plVar5;
  long *plVar6;
  undefined4 uVar7;
  long lVar8;
  long lVar9;
  byte *pbVar10;
  byte *pbVar11;
  ulong uVar12;
  void *pvVar13;
  void *local_13d8;
  ulong local_13d0;
  size_t local_13c8;
  undefined8 local_13c0;
  undefined4 local_13b8;
  byte *local_13b0;
  byte *local_13a8;
  undefined8 *local_13a0;
  undefined8 *puStack_1398;
  undefined8 **local_1390;
  undefined8 local_1388;
  undefined8 uStack_1380;
  undefined8 local_1378;
  undefined8 uStack_1370;
  undefined8 local_1368;
  undefined8 uStack_1360;
  undefined8 local_1358;
  undefined8 uStack_1350;
  undefined8 local_1348;
  undefined8 uStack_1340;
  undefined8 local_1338;
  undefined8 uStack_1330;
  undefined8 local_1328;
  undefined8 uStack_1320;
  undefined8 local_1318;
  undefined8 uStack_1310;
  undefined8 local_1308;
  undefined8 uStack_1300;
  undefined8 local_12f8;
  undefined8 uStack_12f0;
  undefined8 local_12e8;
  undefined8 uStack_12e0;
  undefined8 local_12d8;
  undefined8 uStack_12d0;
  undefined8 local_12c8;
  undefined8 uStack_12c0;
  undefined8 local_12b8;
  undefined8 uStack_12b0;
  undefined8 local_12a8;
  undefined8 uStack_12a0;
  undefined8 uStack_1298;
  undefined8 uStack_1290;
  undefined8 *local_1288;
  undefined8 *puStack_1280;
  undefined8 **local_1278;
  undefined8 local_1270;
  undefined8 uStack_1268;
  undefined8 uStack_1260;
  undefined8 uStack_1258;
  undefined8 local_1250;
  undefined8 uStack_1248;
  undefined8 uStack_1240;
  undefined8 uStack_1238;
  undefined8 local_1230;
  undefined8 uStack_1228;
  undefined8 uStack_1220;
  undefined8 uStack_1218;
  undefined8 local_1210;
  undefined8 uStack_1208;
  undefined8 uStack_1200;
  undefined8 uStack_11f8;
  undefined8 local_11f0;
  undefined8 uStack_11e8;
  undefined8 uStack_11e0;
  undefined8 uStack_11d8;
  undefined8 local_11d0;
  undefined8 uStack_11c8;
  undefined8 uStack_11c0;
  undefined8 uStack_11b8;
  undefined8 local_11b0;
  undefined8 uStack_11a8;
  undefined8 uStack_11a0;
  undefined8 uStack_1198;
  undefined8 local_1190;
  undefined8 uStack_1188;
  undefined8 uStack_1180;
  undefined8 uStack_1178;
  undefined8 *local_1170;
  undefined8 *local_1168;
  undefined8 **local_1160;
  undefined8 local_1158;
  undefined8 uStack_1150;
  undefined8 uStack_1148;
  undefined8 uStack_1140;
  undefined8 local_1138;
  undefined8 uStack_1130;
  undefined8 uStack_1128;
  undefined8 uStack_1120;
  undefined8 *local_1118;
  undefined8 *local_1110;
  undefined8 **local_1108;
  undefined8 local_1100;
  undefined8 uStack_10f8;
  undefined8 uStack_10f0;
  undefined8 uStack_10e8;
  undefined8 *local_10e0;
  undefined8 *local_10d8;
  undefined2 *local_10d0;
  undefined8 local_10c8;
  undefined8 uStack_10c0;
  undefined8 uStack_10b8;
  undefined8 uStack_10b0;
  undefined2 local_10a8;
  undefined1 local_10a6;
  undefined8 local_10a0;
  undefined8 local_1098;
  undefined4 local_1090;
  long local_1080;
  undefined8 uStack_1078;
  long *local_80;
  
                    /* try { // try from 00bbcbf4 to 00cbcbfb has its CatchHandler @ 00bbd3a0 */
                    /* try { // try from 00bbcc00 to 00cbcc67 has its CatchHandler @ 00bbd398 */
  if ((param_1 == (byte *)0x0) || ((param_2 != (void *)0x0 && (param_3 == (ulong *)0x0)))) {
    if (param_4 == (undefined4 *)0x0) {
      return (void *)0x0;
    }
    *param_4 = 0xfffffffd;
    return (void *)0x0;
  }
  sVar4 = strlen((char *)param_1);
  local_13a8 = param_1 + sVar4;
  local_1390 = &local_1288;
  local_1278 = &local_1170;
  local_1160 = &local_1118;
  local_1108 = &local_10e0;
                    /* try { // try from 00bbcc68 to 00cbcca7 has its CatchHandler @ 00bbb8ec */
  local_10d0 = &local_10a8;
  local_10a8 = 1;
  uStack_12a0 = 0;
  local_12a8 = 0;
  uStack_1290 = 0;
  uStack_1298 = 0;
  uStack_1380 = 0;
  local_1388 = 0;
  uStack_1370 = 0;
  local_1378 = 0;
  uStack_1360 = 0;
  local_1368 = 0;
  uStack_1350 = 0;
  local_1358 = 0;
                    /* try { // try from 00bbcca8 to 00cbcd13 has its CatchHandler @ 00bbd394 */
  uStack_1340 = 0;
  local_1348 = 0;
  uStack_1330 = 0;
  local_1338 = 0;
  uStack_1320 = 0;
  local_1328 = 0;
  uStack_1310 = 0;
  local_1318 = 0;
  uStack_1300 = 0;
  local_1308 = 0;
  uStack_12f0 = 0;
  local_12f8 = 0;
  uStack_12e0 = 0;
  local_12e8 = 0;
  uStack_12d0 = 0;
  local_12d8 = 0;
  uStack_12c0 = 0;
  local_12c8 = 0;
  uStack_12b0 = 0;
  local_12b8 = 0;
  uStack_1268 = 0;
  local_1270 = 0;
  uStack_1258 = 0;
  uStack_1260 = 0;
  uStack_1248 = 0;
  local_1250 = 0;
  uStack_1238 = 0;
  uStack_1240 = 0;
  uStack_1228 = 0;
  local_1230 = 0;
  uStack_1218 = 0;
  uStack_1220 = 0;
  uStack_1208 = 0;
  local_1210 = 0;
  uStack_11f8 = 0;
  uStack_1200 = 0;
  uStack_11e8 = 0;
  local_11f0 = 0;
  uStack_11d8 = 0;
  uStack_11e0 = 0;
  uStack_11c8 = 0;
  local_11d0 = 0;
  uStack_11b8 = 0;
  uStack_11c0 = 0;
  uStack_11a8 = 0;
  local_11b0 = 0;
  uStack_1198 = 0;
  uStack_11a0 = 0;
  uStack_1188 = 0;
  local_1190 = 0;
  uStack_1178 = 0;
  uStack_1180 = 0;
  uStack_1150 = 0;
  local_1158 = 0;
  uStack_1140 = 0;
  uStack_1148 = 0;
  uStack_1130 = 0;
  local_1138 = 0;
  uStack_1120 = 0;
  uStack_1128 = 0;
  uStack_10f8 = 0;
  local_1100 = 0;
  uStack_10e8 = 0;
  uStack_10f0 = 0;
                    /* try { // try from 00bbcd14 to 00cbcd53 has its CatchHandler @ 00bbb8ec */
  uStack_10c0 = 0;
  local_10c8 = 0;
  uStack_10b0 = 0;
  uStack_10b8 = 0;
  local_10a6 = 0;
  local_10a0 = 0xffffffffffffffff;
  local_1090 = 0;
  local_1098 = 0;
  uStack_1078 = 0;
  local_1080 = 0;
  local_13a0 = &local_1388;
  puStack_1398 = &local_1388;
  local_1288 = &local_1270;
  puStack_1280 = &local_1270;
  local_1170 = &local_1158;
  local_1168 = &local_1158;
  local_1118 = &local_1100;
  local_1110 = &local_1100;
  local_10e0 = &local_10c8;
  local_10d8 = &local_10c8;
  local_80 = &local_1080;
  if (sVar4 < 2) {
LAB_00bbcdb0:
    local_13b0 = param_1;
    plVar5 = (long *)FUN_00bbde18(&local_13b0);
    if (local_13a8 == local_13b0) {
LAB_00bbd07c:
      if (plVar5 != (long *)0x0) goto LAB_00bbd080;
    }
LAB_00bbcdc4:
    pvVar13 = (void *)0x0;
    uVar7 = 0xfffffffe;
  }
  else {
    if (*(short *)param_1 != 0x5a5f) {
      if (sVar4 == 2) goto LAB_00bbcdb0;
                    /* try { // try from 00bbcd54 to 00cbcd5b has its CatchHandler @ 00bbd3a0 */
                    /* try { // try from 00bbcd64 to 00cbcdc7 has its CatchHandler @ 00bbd2e4 */
      if (*(short *)param_1 == 0x5f5f && param_1[2] == 0x5a) {
        lVar9 = 3;
        goto LAB_00bbce94;
      }
      if (sVar4 < 4) goto LAB_00bbcdb0;
      if (*(int *)param_1 == 0x5a5f5f5f) {
        lVar9 = 4;
      }
      else {
        if ((sVar4 == 4) || (*(int *)param_1 != 0x5f5f5f5f || param_1[4] != 0x5a))
        goto LAB_00bbcdb0;
        lVar9 = 5;
      }
      local_13b0 = param_1 + lVar9;
      local_13d8 = (void *)FUN_00bbd2c4(&local_13b0);
      plVar5 = (long *)0x0;
      if (local_13d8 != (void *)0x0) {
        if (((ulong)((long)local_13a8 - (long)local_13b0) < 0xd) ||
           (*(long *)local_13b0 != 0x695f6b636f6c625f ||
            *(long *)(local_13b0 + 5) != 0x656b6f766e695f6b)) goto LAB_00bbcdc4;
        pbVar10 = local_13b0 + 0xd;
        if (pbVar10 != local_13a8) {
          bVar1 = *pbVar10;
          if (bVar1 == 0x5f) {
                    /* try { // try from 00bbcfdc to 00cbcfe3 has its CatchHandler @ 00bbd2f4 */
            pbVar10 = local_13b0 + 0xe;
          }
          local_13b0 = pbVar10;
          if (local_13a8 == pbVar10) {
            bVar3 = true;
            pbVar11 = local_13a8;
          }
          else {
                    /* try { // try from 00bbcff8 to 00cbcfff has its CatchHandler @ 00bbd2f0 */
            if (*pbVar10 - 0x3a < 0xfffffff6) {
              bVar3 = true;
              pbVar11 = pbVar10;
            }
            else {
              do {
                    /* try { // try from 00bbd014 to 00cbd01b has its CatchHandler @ 00bbd2ec */
                pbVar11 = local_13b0;
                if (*local_13b0 - 0x3a < 0xfffffff6) break;
                local_13b0 = local_13b0 + 1;
                pbVar11 = local_13a8;
                    /* try { // try from 00bbd030 to 00cbd033 has its CatchHandler @ 00bbd2f4 */
              } while (local_13b0 != local_13a8);
              bVar3 = pbVar11 == pbVar10;
            }
          }
                    /* try { // try from 00bbd048 to 00cbd04b has its CatchHandler @ 00bbd2f0 */
          if ((bVar1 == 0x5f) && (bVar3)) goto LAB_00bbcdc4;
          pbVar10 = local_13b0;
          if (local_13a8 != pbVar11) {
                    /* try { // try from 00bbd060 to 00cbd063 has its CatchHandler @ 00bbd2ec */
            if (*pbVar11 != 0x2e) goto LAB_00bbcdc4;
            local_13b0 = local_13a8;
            pbVar10 = local_13b0;
          }
        }
        local_13b0 = pbVar10;
                    /* try { // try from 00bbd078 to 00cbd07f has its CatchHandler @ 00bbd2c8 */
        plVar5 = (long *)FUN_00bbdd64(&local_13b0,"invocation function for block in ",&local_13d8);
      }
      goto LAB_00bbd07c;
    }
                    /* try { // try from 00bbce88 to 00cbce93 has its CatchHandler @ 00bbd2e8 */
    lVar9 = 2;
LAB_00bbce94:
    local_13b0 = param_1 + lVar9;
    plVar6 = (long *)FUN_00bbd2c4(&local_13b0);
    plVar2 = local_80;
    pbVar10 = local_13b0;
    if (plVar6 == (long *)0x0) goto LAB_00bbcdc4;
    lVar9 = (long)local_13a8 - (long)local_13b0;
    plVar5 = plVar6;
    if (lVar9 != 0) {
      if (*local_13b0 != 0x2e) goto LAB_00bbcdc4;
      lVar8 = local_80[1];
      if (lVar8 - 0xfc0U < 0xfffffffffffff010) {
        plVar5 = malloc(0x1000);
        if (plVar5 == (long *)0x0) {
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bbc0b8 with catch @ 00bbd174 */
          _ZSt9terminatev();
        }
        lVar8 = 0;
        *plVar5 = (long)plVar2;
        plVar5[1] = 0;
        local_80 = plVar5;
      }
      local_80[1] = lVar8 + 0x30;
      plVar5 = (long *)((long)local_80 + lVar8 + 0x10);
      *plVar5 = (long)&PTR_FUN_00c199e8;
      *(long **)((long)local_80 + lVar8 + 0x20) = plVar6;
      *(byte **)((long)local_80 + lVar8 + 0x28) = pbVar10;
      *(undefined1 *)((long)local_80 + lVar8 + 0x18) = 1;
      *(long *)((long)local_80 + lVar8 + 0x30) = lVar9;
      *(ushort *)((long)local_80 + lVar8 + 0x19) =
           *(ushort *)((long)local_80 + lVar8 + 0x19) & 0xf000 | 0x540;
      local_13b0 = local_13a8;
    }
LAB_00bbd080:
    if (param_2 == (void *)0x0) {
      local_13c8 = 0;
    }
    else {
      local_13c8 = *param_3;
    }
                    /* try { // try from 00bbd094 to 00cbd09b has its CatchHandler @ 00bbd2c4 */
    local_13d0 = 0;
    local_13b8 = 1;
                    /* try { // try from 00bbd0b0 to 00cbd0b3 has its CatchHandler @ 00bbd2c8 */
    local_13c0 = 0xffffffffffffffff;
    local_13d8 = param_2;
    if (local_10e0 != local_10d8) {
                    /* catch() { ... } // from try @ 00bbc100 with catch @ 00bbd15c */
                    /* WARNING: Subroutine does not return */
      FUN_00bbb158("%s:%d: %s","out/llvm-project/libcxxabi/src/cxa_demangle.cpp",400,&DAT_00296866);
    }
                    /* try { // try from 00bbd0c8 to 00cbd0cb has its CatchHandler @ 00bbd2c4 */
    (**(code **)(*plVar5 + 0x20))(plVar5,&local_13d8);
                    /* catch() { ... } // from try @ 00bbcba8 with catch @ 00bbd0cc
                       try { // try from 00bbd0cc to 00cbd41f has its CatchHandler @ 00bbb8ec */
                    /* catch() { ... } // from try @ 00bbcb74 with catch @ 00bbd0d0 */
                    /* catch() { ... } // from try @ 00bbc884 with catch @ 00bbd0d4 */
                    /* catch() { ... } // from try @ 00bbc848 with catch @ 00bbd0d8 */
    if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
                    /* catch() { ... } // from try @ 00bbc6e0 with catch @ 00bbd0dc */
                    /* catch() { ... } // from try @ 00bbc6a8 with catch @ 00bbd0e0 */
                    /* catch() { ... } // from try @ 00bbc590 with catch @ 00bbd0e4 */
      (**(code **)(*plVar5 + 0x28))(plVar5,&local_13d8);
    }
    uVar12 = local_13d0 + 1;
                    /* catch() { ... } // from try @ 00bbc580 with catch @ 00bbd0fc */
    if (local_13c8 < uVar12) {
      local_13c8 = local_13c8 * 2;
      uVar12 = local_13d0 + 0x3e1;
                    /* catch() { ... } // from try @ 00bbc558 with catch @ 00bbd10c */
                    /* catch() { ... } // from try @ 00bbc30c with catch @ 00bbd110 */
      if (local_13c8 < uVar12 || local_13c8 - uVar12 == 0) {
        local_13c8 = uVar12;
      }
      local_13d8 = realloc(local_13d8,local_13c8);
      if (local_13d8 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bbc0f4 with catch @ 00bbd170 */
        abort();
      }
                    /* catch() { ... } // from try @ 00bbc2fc with catch @ 00bbd128 */
      uVar12 = local_13d0 + 1;
    }
    *(undefined1 *)((long)local_13d8 + local_13d0) = 0;
    if (param_3 != (ulong *)0x0) {
                    /* catch() { ... } // from try @ 00bbc2f0 with catch @ 00bbd13c */
      *param_3 = uVar12;
    }
                    /* catch() { ... } // from try @ 00bbc2a8 with catch @ 00bbd140 */
                    /* catch() { ... } // from try @ 00bbc110 with catch @ 00bbd144 */
    uVar7 = 0;
    local_13d0 = uVar12;
    pvVar13 = local_13d8;
  }
  plVar5 = local_80;
  if (param_4 != (undefined4 *)0x0) {
    *param_4 = uVar7;
  }
  while (local_80 = plVar5, local_80 != (long *)0x0) {
    while (plVar5 = (long *)*local_80, local_80 != &local_1080) {
      plVar5 = local_80;
      local_80 = (long *)*local_80;
      free(plVar5);
      if (local_80 == (long *)0x0) goto LAB_00bbce04;
    }
  }
LAB_00bbce04:
  local_1080 = 0;
  uStack_1078 = 0;
  local_80 = &local_1080;
  if (local_10e0 != &local_10c8) {
    free(local_10e0);
  }
                    /* try { // try from 00bbce24 to 00cbce27 has its CatchHandler @ 00bbd298 */
  if (local_1118 != &local_1100) {
                    /* try { // try from 00bbce28 to 00cbce87 has its CatchHandler @ 00bbb8ec */
    free(local_1118);
  }
  if (local_1170 != &local_1158) {
    free(local_1170);
  }
  if (local_1288 != &local_1270) {
    free(local_1288);
  }
  if (local_13a0 != &local_1388) {
    free(local_13a0);
  }
  return pvVar13;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbcbcc"></a> `00bbcbcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbcbd0"></a> `00bbcbd0` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bbcbd4"></a> `00bbcbd4` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcbd8"></a> `00bbcbd8` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcbdc"></a> `00bbcbdc` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcbe0"></a> `00bbcbe0` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbcbe4"></a> `00bbcbe4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbcbe8"></a> `00bbcbe8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbcbec"></a> `00bbcbec` | `ff 07 40 d1` | sub sp,sp,#0x1, LSL #12 | `FALL_THROUGH`
<a id="insn-00bbcbf0"></a> `00bbcbf0` | `ff 43 0e d1` | sub sp,sp,#0x390 | `FALL_THROUGH`
<a id="insn-00bbcbf4"></a> `00bbcbf4` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-00bbcbf8"></a> `00bbcbf8` | `a0 00 00 b4` | cbz x0,0x00bbcc0c | `CONDITIONAL_JUMP`
<a id="insn-00bbcbfc"></a> `00bbcbfc` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bbcc00"></a> `00bbcc00` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bbcc04"></a> `00bbcc04` | `e1 00 00 b4` | cbz x1,0x00bbcc20 | `CONDITIONAL_JUMP`
<a id="insn-00bbcc08"></a> `00bbcc08` | `d4 00 00 b5` | cbnz x20,0x00bbcc20 | `CONDITIONAL_JUMP`
<a id="insn-00bbcc0c"></a> `00bbcc0c` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00bbcc10"></a> `00bbcc10` | `73 12 00 b4` | cbz x19,0x00bbce5c | `CONDITIONAL_JUMP`
<a id="insn-00bbcc14"></a> `00bbcc14` | `48 00 80 12` | mov w8,#0xfffffffd | `FALL_THROUGH`
<a id="insn-00bbcc18"></a> `00bbcc18` | `68 02 00 b9` | str w8,[x19] | `FALL_THROUGH`
<a id="insn-00bbcc1c"></a> `00bbcc1c` | `90 00 00 14` | b 0x00bbce5c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcc20"></a> `00bbcc20` | `fc 03 01 91` | add x28,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbcc24"></a> `00bbcc24` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbcc28"></a> `00bbcc28` | `46 79 00 94` | bl 0x00bdb140 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcc2c"></a> `00bbcc2c` | `e9 03 01 91` | add x9,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbcc30"></a> `00bbcc30` | `ca 02 00 8b` | add x10,x22,x0 | `FALL_THROUGH`
<a id="insn-00bbcc34"></a> `00bbcc34` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bbcc38"></a> `00bbcc38` | `f6 2b 04 a9` | stp x22,x10,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbcc3c"></a> `00bbcc3c` | `2a a1 04 91` | add x10,x9,#0x128 | `FALL_THROUGH`
<a id="insn-00bbcc40"></a> `00bbcc40` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bbcc44"></a> `00bbcc44` | `ea 33 00 f9` | str x10,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbcc48"></a> `00bbcc48` | `2a 01 09 91` | add x10,x9,#0x240 | `FALL_THROUGH`
<a id="insn-00bbcc4c"></a> `00bbcc4c` | `36 a1 00 91` | add x22,x9,#0x28 | `FALL_THROUGH`
<a id="insn-00bbcc50"></a> `00bbcc50` | `ea bf 00 f9` | str x10,[sp, #0x178] | `FALL_THROUGH`
<a id="insn-00bbcc54"></a> `00bbcc54` | `2a 61 0a 91` | add x10,x9,#0x298 | `FALL_THROUGH`
<a id="insn-00bbcc58"></a> `00bbcc58` | `37 01 05 91` | add x23,x9,#0x140 | `FALL_THROUGH`
<a id="insn-00bbcc5c"></a> `00bbcc5c` | `ea 4b 01 f9` | str x10,[sp, #0x290] | `FALL_THROUGH`
<a id="insn-00bbcc60"></a> `00bbcc60` | `2a 41 0b 91` | add x10,x9,#0x2d0 | `FALL_THROUGH`
<a id="insn-00bbcc64"></a> `00bbcc64` | `38 61 09 91` | add x24,x9,#0x258 | `FALL_THROUGH`
<a id="insn-00bbcc68"></a> `00bbcc68` | `ea 77 01 f9` | str x10,[sp, #0x2e8] | `FALL_THROUGH`
<a id="insn-00bbcc6c"></a> `00bbcc6c` | `2a 21 0c 91` | add x10,x9,#0x308 | `FALL_THROUGH`
<a id="insn-00bbcc70"></a> `00bbcc70` | `39 c1 0a 91` | add x25,x9,#0x2b0 | `FALL_THROUGH`
<a id="insn-00bbcc74"></a> `00bbcc74` | `ea 93 01 f9` | str x10,[sp, #0x320] | `FALL_THROUGH`
<a id="insn-00bbcc78"></a> `00bbcc78` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcc7c"></a> `00bbcc7c` | `3a a1 0b 91` | add x26,x9,#0x2e8 | `FALL_THROUGH`
<a id="insn-00bbcc80"></a> `00bbcc80` | `ea 93 06 79` | strh w10,[sp, #0x348] | `FALL_THROUGH`
<a id="insn-00bbcc84"></a> `00bbcc84` | `0a 00 80 92` | mov x10,#-0x1 | `FALL_THROUGH`
<a id="insn-00bbcc88"></a> `00bbcc88` | `3b c1 0c 91` | add x27,x9,#0x330 | `FALL_THROUGH`
<a id="insn-00bbcc8c"></a> `00bbcc8c` | `1f 08 00 f1` | cmp x0,#0x2 | `FALL_THROUGH`
<a id="insn-00bbcc90"></a> `00bbcc90` | `f6 5b 05 a9` | stp x22,x22,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbcc94"></a> `00bbcc94` | `c0 02 07 ad` | stp q0,q0,[x22, #0xe0] | `FALL_THROUGH`
<a id="insn-00bbcc98"></a> `00bbcc98` | `e0 83 86 3c` | stur q0,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bbcc9c"></a> `00bbcc9c` | `e0 83 87 3c` | stur q0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00bbcca0"></a> `00bbcca0` | `e0 83 88 3c` | stur q0,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00bbcca4"></a> `00bbcca4` | `80 83 85 3c` | stur q0,[x28, #0x58] | `FALL_THROUGH`
<a id="insn-00bbcca8"></a> `00bbcca8` | `80 83 86 3c` | stur q0,[x28, #0x68] | `FALL_THROUGH`
<a id="insn-00bbccac"></a> `00bbccac` | `80 83 87 3c` | stur q0,[x28, #0x78] | `FALL_THROUGH`
<a id="insn-00bbccb0"></a> `00bbccb0` | `80 83 88 3c` | stur q0,[x28, #0x88] | `FALL_THROUGH`
<a id="insn-00bbccb4"></a> `00bbccb4` | `80 83 89 3c` | stur q0,[x28, #0x98] | `FALL_THROUGH`
<a id="insn-00bbccb8"></a> `00bbccb8` | `80 83 8a 3c` | stur q0,[x28, #0xa8] | `FALL_THROUGH`
<a id="insn-00bbccbc"></a> `00bbccbc` | `80 83 8b 3c` | stur q0,[x28, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbccc0"></a> `00bbccc0` | `80 83 8c 3c` | stur q0,[x28, #0xc8] | `FALL_THROUGH`
<a id="insn-00bbccc4"></a> `00bbccc4` | `80 83 8d 3c` | stur q0,[x28, #0xd8] | `FALL_THROUGH`
<a id="insn-00bbccc8"></a> `00bbccc8` | `80 83 8e 3c` | stur q0,[x28, #0xe8] | `FALL_THROUGH`
<a id="insn-00bbcccc"></a> `00bbcccc` | `80 83 8f 3c` | stur q0,[x28, #0xf8] | `FALL_THROUGH`
<a id="insn-00bbccd0"></a> `00bbccd0` | `f7 df 16 a9` | stp x23,x23,[sp, #0x168] | `FALL_THROUGH`
<a id="insn-00bbccd4"></a> `00bbccd4` | `80 03 0a ad` | stp q0,q0,[x28, #0x140] | `FALL_THROUGH`
<a id="insn-00bbccd8"></a> `00bbccd8` | `80 03 0b ad` | stp q0,q0,[x28, #0x160] | `FALL_THROUGH`
<a id="insn-00bbccdc"></a> `00bbccdc` | `80 03 0c ad` | stp q0,q0,[x28, #0x180] | `FALL_THROUGH`
<a id="insn-00bbcce0"></a> `00bbcce0` | `80 03 0d ad` | stp q0,q0,[x28, #0x1a0] | `FALL_THROUGH`
<a id="insn-00bbcce4"></a> `00bbcce4` | `80 03 0e ad` | stp q0,q0,[x28, #0x1c0] | `FALL_THROUGH`
<a id="insn-00bbcce8"></a> `00bbcce8` | `80 03 0f ad` | stp q0,q0,[x28, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bbccec"></a> `00bbccec` | `80 03 10 ad` | stp q0,q0,[x28, #0x200] | `FALL_THROUGH`
<a id="insn-00bbccf0"></a> `00bbccf0` | `80 03 11 ad` | stp q0,q0,[x28, #0x220] | `FALL_THROUGH`
<a id="insn-00bbccf4"></a> `00bbccf4` | `f8 43 01 f9` | str x24,[sp, #0x280] | `FALL_THROUGH`
<a id="insn-00bbccf8"></a> `00bbccf8` | `f8 47 01 f9` | str x24,[sp, #0x288] | `FALL_THROUGH`
<a id="insn-00bbccfc"></a> `00bbccfc` | `00 03 00 ad` | stp q0,q0,[x24] | `FALL_THROUGH`
<a id="insn-00bbcd00"></a> `00bbcd00` | `00 03 01 ad` | stp q0,q0,[x24, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcd04"></a> `00bbcd04` | `f9 6f 01 f9` | str x25,[sp, #0x2d8] | `FALL_THROUGH`
<a id="insn-00bbcd08"></a> `00bbcd08` | `f9 73 01 f9` | str x25,[sp, #0x2e0] | `FALL_THROUGH`
<a id="insn-00bbcd0c"></a> `00bbcd0c` | `80 83 15 ad` | stp q0,q0,[x28, #0x2b0] | `FALL_THROUGH`
<a id="insn-00bbcd10"></a> `00bbcd10` | `fa 8b 01 f9` | str x26,[sp, #0x310] | `FALL_THROUGH`
<a id="insn-00bbcd14"></a> `00bbcd14` | `fa 8f 01 f9` | str x26,[sp, #0x318] | `FALL_THROUGH`
<a id="insn-00bbcd18"></a> `00bbcd18` | `40 03 00 ad` | stp q0,q0,[x26] | `FALL_THROUGH`
<a id="insn-00bbcd1c"></a> `00bbcd1c` | `ff 2b 0d 39` | strb wzr,[sp, #0x34a] | `FALL_THROUGH`
<a id="insn-00bbcd20"></a> `00bbcd20` | `ea ab 01 f9` | str x10,[sp, #0x350] | `FALL_THROUGH`
<a id="insn-00bbcd24"></a> `00bbcd24` | `ff 63 03 b9` | str wzr,[sp, #0x360] | `FALL_THROUGH`
<a id="insn-00bbcd28"></a> `00bbcd28` | `ff af 01 f9` | str xzr,[sp, #0x358] | `FALL_THROUGH`
<a id="insn-00bbcd2c"></a> `00bbcd2c` | `80 cf 80 3d` | str q0,[x28, #0x330] | `FALL_THROUGH`
<a id="insn-00bbcd30"></a> `00bbcd30` | `fb bb 09 f9` | str x27,[sp, #0x1370] | `FALL_THROUGH`
<a id="insn-00bbcd34"></a> `00bbcd34` | `e3 03 00 54` | b.cc 0x00bbcdb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbcd38"></a> `00bbcd38` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbcd3c"></a> `00bbcd3c` | `ea 4b 8b 52` | mov w10,#0x5a5f | `FALL_THROUGH`
<a id="insn-00bbcd40"></a> `00bbcd40` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00bbcd44"></a> `00bbcd44` | `20 0a 00 54` | b.eq 0x00bbce88 | `CONDITIONAL_JUMP`
<a id="insn-00bbcd48"></a> `00bbcd48` | `1f 08 00 f1` | cmp x0,#0x2 | `FALL_THROUGH`
<a id="insn-00bbcd4c"></a> `00bbcd4c` | `20 03 00 54` | b.eq 0x00bbcdb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbcd50"></a> `00bbcd50` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbcd54"></a> `00bbcd54` | `0a 09 40 39` | ldrb w10,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bbcd58"></a> `00bbcd58` | `eb eb 8b 52` | mov w11,#0x5f5f | `FALL_THROUGH`
<a id="insn-00bbcd5c"></a> `00bbcd5c` | `3f 01 0b 6b` | cmp w9,w11 | `FALL_THROUGH`
<a id="insn-00bbcd60"></a> `00bbcd60` | `49 0b 80 52` | mov w9,#0x5a | `FALL_THROUGH`
<a id="insn-00bbcd64"></a> `00bbcd64` | `40 01 49 7a` | ccmp w10,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-00bbcd68"></a> `00bbcd68` | `40 09 00 54` | b.eq 0x00bbce90 | `CONDITIONAL_JUMP`
<a id="insn-00bbcd6c"></a> `00bbcd6c` | `1f 10 00 f1` | cmp x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bbcd70"></a> `00bbcd70` | `03 02 00 54` | b.cc 0x00bbcdb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbcd74"></a> `00bbcd74` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbcd78"></a> `00bbcd78` | `ea eb 8b 52` | mov w10,#0x5f5f | `FALL_THROUGH`
<a id="insn-00bbcd7c"></a> `00bbcd7c` | `ea 4b ab 72` | movk w10,#0x5a5f, LSL #16 | `FALL_THROUGH`
<a id="insn-00bbcd80"></a> `00bbcd80` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00bbcd84"></a> `00bbcd84` | `40 0e 00 54` | b.eq 0x00bbcf4c | `CONDITIONAL_JUMP`
<a id="insn-00bbcd88"></a> `00bbcd88` | `1f 10 00 f1` | cmp x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bbcd8c"></a> `00bbcd8c` | `20 01 00 54` | b.eq 0x00bbcdb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbcd90"></a> `00bbcd90` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbcd94"></a> `00bbcd94` | `eb eb 8b 52` | mov w11,#0x5f5f | `FALL_THROUGH`
<a id="insn-00bbcd98"></a> `00bbcd98` | `0a 11 40 39` | ldrb w10,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bbcd9c"></a> `00bbcd9c` | `eb eb ab 72` | movk w11,#0x5f5f, LSL #16 | `FALL_THROUGH`
<a id="insn-00bbcda0"></a> `00bbcda0` | `3f 01 0b 6b` | cmp w9,w11 | `FALL_THROUGH`
<a id="insn-00bbcda4"></a> `00bbcda4` | `49 0b 80 52` | mov w9,#0x5a | `FALL_THROUGH`
<a id="insn-00bbcda8"></a> `00bbcda8` | `40 01 49 7a` | ccmp w10,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-00bbcdac"></a> `00bbcdac` | `40 0d 00 54` | b.eq 0x00bbcf54 | `CONDITIONAL_JUMP`
<a id="insn-00bbcdb0"></a> `00bbcdb0` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbcdb4"></a> `00bbcdb4` | `19 04 00 94` | bl 0x00bbde18 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcdb8"></a> `00bbcdb8` | `e9 23 44 a9` | ldp x9,x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbcdbc"></a> `00bbcdbc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbcdc0"></a> `00bbcdc0` | `e0 15 00 54` | b.eq 0x00bbd07c | `CONDITIONAL_JUMP`
<a id="insn-00bbcdc4"></a> `00bbcdc4` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00bbcdc8"></a> `00bbcdc8` | `28 00 80 12` | mov w8,#0xfffffffe | `FALL_THROUGH`
<a id="insn-00bbcdcc"></a> `00bbcdcc` | `53 00 00 b4` | cbz x19,0x00bbcdd4 | `CONDITIONAL_JUMP`
<a id="insn-00bbcdd0"></a> `00bbcdd0` | `68 02 00 b9` | str w8,[x19] | `FALL_THROUGH`
<a id="insn-00bbcdd4"></a> `00bbcdd4` | `e0 bb 49 f9` | ldr x0,[sp, #0x1370] | `FALL_THROUGH`
<a id="insn-00bbcdd8"></a> `00bbcdd8` | `80 00 00 b5` | cbnz x0,0x00bbcde8 | `CONDITIONAL_JUMP`
<a id="insn-00bbcddc"></a> `00bbcddc` | `0a 00 00 14` | b 0x00bbce04 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcde0"></a> `00bbcde0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbcde4"></a> `00bbcde4` | `00 01 00 b4` | cbz x0,0x00bbce04 | `CONDITIONAL_JUMP`
<a id="insn-00bbcde8"></a> `00bbcde8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbcdec"></a> `00bbcdec` | `1f 00 1b eb` | cmp x0,x27 | `FALL_THROUGH`
<a id="insn-00bbcdf0"></a> `00bbcdf0` | `e8 bb 09 f9` | str x8,[sp, #0x1370] | `FALL_THROUGH`
<a id="insn-00bbcdf4"></a> `00bbcdf4` | `60 ff ff 54` | b.eq 0x00bbcde0 | `CONDITIONAL_JUMP`
<a id="insn-00bbcdf8"></a> `00bbcdf8` | `72 7a 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcdfc"></a> `00bbcdfc` | `e0 bb 49 f9` | ldr x0,[sp, #0x1370] | `FALL_THROUGH`
<a id="insn-00bbce00"></a> `00bbce00` | `40 ff ff b5` | cbnz x0,0x00bbcde8 | `CONDITIONAL_JUMP`
<a id="insn-00bbce04"></a> `00bbce04` | `e0 8b 41 f9` | ldr x0,[sp, #0x310] | `FALL_THROUGH`
<a id="insn-00bbce08"></a> `00bbce08` | `7f 7f 00 a9` | stp xzr,xzr,[x27] | `FALL_THROUGH`
<a id="insn-00bbce0c"></a> `00bbce0c` | `fb bb 09 f9` | str x27,[sp, #0x1370] | `FALL_THROUGH`
<a id="insn-00bbce10"></a> `00bbce10` | `1f 00 1a eb` | cmp x0,x26 | `FALL_THROUGH`
<a id="insn-00bbce14"></a> `00bbce14` | `40 00 00 54` | b.eq 0x00bbce1c | `CONDITIONAL_JUMP`
<a id="insn-00bbce18"></a> `00bbce18` | `6a 7a 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce1c"></a> `00bbce1c` | `e0 6f 41 f9` | ldr x0,[sp, #0x2d8] | `FALL_THROUGH`
<a id="insn-00bbce20"></a> `00bbce20` | `1f 00 19 eb` | cmp x0,x25 | `FALL_THROUGH`
<a id="insn-00bbce24"></a> `00bbce24` | `40 00 00 54` | b.eq 0x00bbce2c | `CONDITIONAL_JUMP`
<a id="insn-00bbce28"></a> `00bbce28` | `66 7a 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce2c"></a> `00bbce2c` | `e0 43 41 f9` | ldr x0,[sp, #0x280] | `FALL_THROUGH`
<a id="insn-00bbce30"></a> `00bbce30` | `1f 00 18 eb` | cmp x0,x24 | `FALL_THROUGH`
<a id="insn-00bbce34"></a> `00bbce34` | `40 00 00 54` | b.eq 0x00bbce3c | `CONDITIONAL_JUMP`
<a id="insn-00bbce38"></a> `00bbce38` | `62 7a 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce3c"></a> `00bbce3c` | `e0 b7 40 f9` | ldr x0,[sp, #0x168] | `FALL_THROUGH`
<a id="insn-00bbce40"></a> `00bbce40` | `1f 00 17 eb` | cmp x0,x23 | `FALL_THROUGH`
<a id="insn-00bbce44"></a> `00bbce44` | `40 00 00 54` | b.eq 0x00bbce4c | `CONDITIONAL_JUMP`
<a id="insn-00bbce48"></a> `00bbce48` | `5e 7a 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce4c"></a> `00bbce4c` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbce50"></a> `00bbce50` | `1f 00 16 eb` | cmp x0,x22 | `FALL_THROUGH`
<a id="insn-00bbce54"></a> `00bbce54` | `40 00 00 54` | b.eq 0x00bbce5c | `CONDITIONAL_JUMP`
<a id="insn-00bbce58"></a> `00bbce58` | `5a 7a 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce5c"></a> `00bbce5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbce60"></a> `00bbce60` | `ff 07 40 91` | add sp,sp,#0x1, LSL #12 | `FALL_THROUGH`
<a id="insn-00bbce64"></a> `00bbce64` | `ff 43 0e 91` | add sp,sp,#0x390 | `FALL_THROUGH`
<a id="insn-00bbce68"></a> `00bbce68` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbce6c"></a> `00bbce6c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbce70"></a> `00bbce70` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbce74"></a> `00bbce74` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbce78"></a> `00bbce78` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbce7c"></a> `00bbce7c` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bbce80"></a> `00bbce80` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbce84"></a> `00bbce84` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbce88"></a> `00bbce88` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00bbce8c"></a> `00bbce8c` | `02 00 00 14` | b 0x00bbce94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbce90"></a> `00bbce90` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bbce94"></a> `00bbce94` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbce98"></a> `00bbce98` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbce9c"></a> `00bbce9c` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbcea0"></a> `00bbcea0` | `09 01 00 94` | bl 0x00bbd2c4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcea4"></a> `00bbcea4` | `00 f9 ff b4` | cbz x0,0x00bbcdc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbcea8"></a> `00bbcea8` | `fc 23 44 a9` | ldp x28,x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbceac"></a> `00bbceac` | `0b 01 1c eb` | subs x11,x8,x28 | `FALL_THROUGH`
<a id="insn-00bbceb0"></a> `00bbceb0` | `80 0e 00 54` | b.eq 0x00bbd080 | `CONDITIONAL_JUMP`
<a id="insn-00bbceb4"></a> `00bbceb4` | `88 03 40 39` | ldrb w8,[x28] | `FALL_THROUGH`
<a id="insn-00bbceb8"></a> `00bbceb8` | `1f b9 00 71` | cmp w8,#0x2e | `FALL_THROUGH`
<a id="insn-00bbcebc"></a> `00bbcebc` | `41 f8 ff 54` | b.ne 0x00bbcdc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbcec0"></a> `00bbcec0` | `ea bb 49 f9` | ldr x10,[sp, #0x1370] | `FALL_THROUGH`
<a id="insn-00bbcec4"></a> `00bbcec4` | `48 05 40 f9` | ldr x8,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcec8"></a> `00bbcec8` | `09 01 3f d1` | sub x9,x8,#0xfc0 | `FALL_THROUGH`
<a id="insn-00bbcecc"></a> `00bbcecc` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbced0"></a> `00bbced0` | `88 01 00 54` | b.hi 0x00bbcf00 | `CONDITIONAL_JUMP`
<a id="insn-00bbced4"></a> `00bbced4` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbced8"></a> `00bbced8` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbcedc"></a> `00bbcedc` | `ea 2f 00 a9` | stp x10,x11,[sp] | `FALL_THROUGH`
<a id="insn-00bbcee0"></a> `00bbcee0` | `a8 80 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcee4"></a> `00bbcee4` | `80 14 00 b4` | cbz x0,0x00bbd174 | `CONDITIONAL_JUMP`
<a id="insn-00bbcee8"></a> `00bbcee8` | `e9 2f 40 a9` | ldp x9,x11,[sp] | `FALL_THROUGH`
<a id="insn-00bbceec"></a> `00bbceec` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bbcef0"></a> `00bbcef0` | `e0 bb 09 f9` | str x0,[sp, #0x1370] | `FALL_THROUGH`
<a id="insn-00bbcef4"></a> `00bbcef4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbcef8"></a> `00bbcef8` | `09 7c 00 a9` | stp x9,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbcefc"></a> `00bbcefc` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcf00"></a> `00bbcf00` | `09 c1 00 91` | add x9,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcf04"></a> `00bbcf04` | `48 01 08 8b` | add x8,x10,x8 | `FALL_THROUGH`
<a id="insn-00bbcf08"></a> `00bbcf08` | `49 05 00 f9` | str x9,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcf0c"></a> `00bbcf0c` | `e9 02 00 b0` | adrp x9,0xc19000 | `FALL_THROUGH`
<a id="insn-00bbcf10"></a> `00bbcf10` | `29 a1 27 91` | add x9,x9,#0x9e8 | `FALL_THROUGH`
<a id="insn-00bbcf14"></a> `00bbcf14` | `09 0d 01 f8` | str x9,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbcf18"></a> `00bbcf18` | `09 91 40 78` | ldurh w9,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00bbcf1c"></a> `00bbcf1c` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcf20"></a> `00bbcf20` | `00 71 01 a9` | stp x0,x28,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcf24"></a> `00bbcf24` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbcf28"></a> `00bbcf28` | `0a 21 00 39` | strb w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcf2c"></a> `00bbcf2c` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbcf30"></a> `00bbcf30` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbcf34"></a> `00bbcf34` | `29 01 0a 2a` | orr w9,w9,w10 | `FALL_THROUGH`
<a id="insn-00bbcf38"></a> `00bbcf38` | `0b 11 00 f9` | str x11,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcf3c"></a> `00bbcf3c` | `09 91 00 78` | sturh w9,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00bbcf40"></a> `00bbcf40` | `e9 27 40 f9` | ldr x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbcf44"></a> `00bbcf44` | `e9 23 00 f9` | str x9,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbcf48"></a> `00bbcf48` | `4e 00 00 14` | b 0x00bbd080 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcf4c"></a> `00bbcf4c` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bbcf50"></a> `00bbcf50` | `02 00 00 14` | b 0x00bbcf58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcf54"></a> `00bbcf54` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bbcf58"></a> `00bbcf58` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbcf5c"></a> `00bbcf5c` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbcf60"></a> `00bbcf60` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbcf64"></a> `00bbcf64` | `d8 00 00 94` | bl 0x00bbd2c4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf68"></a> `00bbcf68` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbcf6c"></a> `00bbcf6c` | `80 08 00 b4` | cbz x0,0x00bbd07c | `CONDITIONAL_JUMP`
<a id="insn-00bbcf70"></a> `00bbcf70` | `eb 23 44 a9` | ldp x11,x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbcf74"></a> `00bbcf74` | `09 01 0b cb` | sub x9,x8,x11 | `FALL_THROUGH`
<a id="insn-00bbcf78"></a> `00bbcf78` | `3f 35 00 f1` | cmp x9,#0xd | `FALL_THROUGH`
<a id="insn-00bbcf7c"></a> `00bbcf7c` | `c3 01 00 54` | b.cc 0x00bbcfb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbcf80"></a> `00bbcf80` | `ec 4b 8c d2` | mov x12,#0x625f | `FALL_THROUGH`
<a id="insn-00bbcf84"></a> `00bbcf84` | `69 01 40 f9` | ldr x9,[x11] | `FALL_THROUGH`
<a id="insn-00bbcf88"></a> `00bbcf88` | `6a 51 40 f8` | ldur x10,[x11, #0x5] | `FALL_THROUGH`
<a id="insn-00bbcf8c"></a> `00bbcf8c` | `8c ed ad f2` | movk x12,#0x6f6c, LSL #16 | `FALL_THROUGH`
<a id="insn-00bbcf90"></a> `00bbcf90` | `6c 6c cd f2` | movk x12,#0x6b63, LSL #32 | `FALL_THROUGH`
<a id="insn-00bbcf94"></a> `00bbcf94` | `ec 2b ed f2` | movk x12,#0x695f, LSL #48 | `FALL_THROUGH`
<a id="insn-00bbcf98"></a> `00bbcf98` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00bbcf9c"></a> `00bbcf9c` | `69 ed 8b d2` | mov x9,#0x5f6b | `FALL_THROUGH`
<a id="insn-00bbcfa0"></a> `00bbcfa0` | `29 cd ad f2` | movk x9,#0x6e69, LSL #16 | `FALL_THROUGH`
<a id="insn-00bbcfa4"></a> `00bbcfa4` | `c9 ee cd f2` | movk x9,#0x6f76, LSL #32 | `FALL_THROUGH`
<a id="insn-00bbcfa8"></a> `00bbcfa8` | `69 ad ec f2` | movk x9,#0x656b, LSL #48 | `FALL_THROUGH`
<a id="insn-00bbcfac"></a> `00bbcfac` | `40 01 49 fa` | ccmp x10,x9,#0x0,eq | `FALL_THROUGH`
<a id="insn-00bbcfb0"></a> `00bbcfb0` | `80 00 00 54` | b.eq 0x00bbcfc0 | `CONDITIONAL_JUMP`
<a id="insn-00bbcfb4"></a> `00bbcfb4` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbcfb8"></a> `00bbcfb8` | `40 06 00 b5` | cbnz x0,0x00bbd080 | `CONDITIONAL_JUMP`
<a id="insn-00bbcfbc"></a> `00bbcfbc` | `82 ff ff 17` | b 0x00bbcdc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcfc0"></a> `00bbcfc0` | `69 35 00 91` | add x9,x11,#0xd | `FALL_THROUGH`
<a id="insn-00bbcfc4"></a> `00bbcfc4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbcfc8"></a> `00bbcfc8` | `e9 23 00 f9` | str x9,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbcfcc"></a> `00bbcfcc` | `e0 04 00 54` | b.eq 0x00bbd068 | `CONDITIONAL_JUMP`
<a id="insn-00bbcfd0"></a> `00bbcfd0` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbcfd4"></a> `00bbcfd4` | `5f 7d 01 71` | cmp w10,#0x5f | `FALL_THROUGH`
<a id="insn-00bbcfd8"></a> `00bbcfd8` | `61 00 00 54` | b.ne 0x00bbcfe4 | `CONDITIONAL_JUMP`
<a id="insn-00bbcfdc"></a> `00bbcfdc` | `69 39 00 91` | add x9,x11,#0xe | `FALL_THROUGH`
<a id="insn-00bbcfe0"></a> `00bbcfe0` | `e9 23 00 f9` | str x9,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbcfe4"></a> `00bbcfe4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbcfe8"></a> `00bbcfe8` | `e0 00 00 54` | b.eq 0x00bbd004 | `CONDITIONAL_JUMP`
<a id="insn-00bbcfec"></a> `00bbcfec` | `2b 01 40 39` | ldrb w11,[x9] | `FALL_THROUGH`
<a id="insn-00bbcff0"></a> `00bbcff0` | `6b e9 00 51` | sub w11,w11,#0x3a | `FALL_THROUGH`
<a id="insn-00bbcff4"></a> `00bbcff4` | `7f 29 00 31` | cmn w11,#0xa | `FALL_THROUGH`
<a id="insn-00bbcff8"></a> `00bbcff8` | `c2 00 00 54` | b.cs 0x00bbd010 | `CONDITIONAL_JUMP`
<a id="insn-00bbcffc"></a> `00bbcffc` | `2b 00 80 52` | mov w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd000"></a> `00bbd000` | `11 00 00 14` | b 0x00bbd044 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd004"></a> `00bbd004` | `2b 00 80 52` | mov w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd008"></a> `00bbd008` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00bbd00c"></a> `00bbd00c` | `0e 00 00 14` | b 0x00bbd044 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd010"></a> `00bbd010` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bbd014"></a> `00bbd014` | `6c 01 40 39` | ldrb w12,[x11] | `FALL_THROUGH`
<a id="insn-00bbd018"></a> `00bbd018` | `8c e9 00 51` | sub w12,w12,#0x3a | `FALL_THROUGH`
<a id="insn-00bbd01c"></a> `00bbd01c` | `9f 29 00 31` | cmn w12,#0xa | `FALL_THROUGH`
<a id="insn-00bbd020"></a> `00bbd020` | `c3 00 00 54` | b.cc 0x00bbd038 | `CONDITIONAL_JUMP`
<a id="insn-00bbd024"></a> `00bbd024` | `6b 05 00 91` | add x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd028"></a> `00bbd028` | `7f 01 08 eb` | cmp x11,x8 | `FALL_THROUGH`
<a id="insn-00bbd02c"></a> `00bbd02c` | `eb 23 00 f9` | str x11,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd030"></a> `00bbd030` | `21 ff ff 54` | b.ne 0x00bbd014 | `CONDITIONAL_JUMP`
<a id="insn-00bbd034"></a> `00bbd034` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-00bbd038"></a> `00bbd038` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00bbd03c"></a> `00bbd03c` | `e9 03 0b aa` | mov x9,x11 | `FALL_THROUGH`
<a id="insn-00bbd040"></a> `00bbd040` | `eb 17 9f 1a` | cset w11,eq | `FALL_THROUGH`
<a id="insn-00bbd044"></a> `00bbd044` | `5f 7d 01 71` | cmp w10,#0x5f | `FALL_THROUGH`
<a id="insn-00bbd048"></a> `00bbd048` | `41 00 00 54` | b.ne 0x00bbd050 | `CONDITIONAL_JUMP`
<a id="insn-00bbd04c"></a> `00bbd04c` | `4b fb 07 37` | tbnz w11,#0x0,0x00bbcfb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd050"></a> `00bbd050` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbd054"></a> `00bbd054` | `a0 00 00 54` | b.eq 0x00bbd068 | `CONDITIONAL_JUMP`
<a id="insn-00bbd058"></a> `00bbd058` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bbd05c"></a> `00bbd05c` | `3f b9 00 71` | cmp w9,#0x2e | `FALL_THROUGH`
<a id="insn-00bbd060"></a> `00bbd060` | `a1 fa ff 54` | b.ne 0x00bbcfb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd064"></a> `00bbd064` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd068"></a> `00bbd068` | `61 b7 ff 90` | adrp x1,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bbd06c"></a> `00bbd06c` | `21 88 03 91` | add x1,x1,#0xe2 | `FALL_THROUGH`
<a id="insn-00bbd070"></a> `00bbd070` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd074"></a> `00bbd074` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbd078"></a> `00bbd078` | `3b 03 00 94` | bl 0x00bbdd64 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd07c"></a> `00bbd07c` | `40 ea ff b4` | cbz x0,0x00bbcdc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd080"></a> `00bbd080` | `75 00 00 b4` | cbz x21,0x00bbd08c | `CONDITIONAL_JUMP`
<a id="insn-00bbd084"></a> `00bbd084` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbd088"></a> `00bbd088` | `02 00 00 14` | b 0x00bbd090 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd08c"></a> `00bbd08c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbd090"></a> `00bbd090` | `e0 e7 07 6f` | movi v0.2D,#-0x1 | `FALL_THROUGH`
<a id="insn-00bbd094"></a> `00bbd094` | `e9 8b 41 f9` | ldr x9,[sp, #0x310] | `FALL_THROUGH`
<a id="insn-00bbd098"></a> `00bbd098` | `ea 8f 41 f9` | ldr x10,[sp, #0x318] | `FALL_THROUGH`
<a id="insn-00bbd09c"></a> `00bbd09c` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbd0a0"></a> `00bbd0a0` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd0a4"></a> `00bbd0a4` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbd0a8"></a> `00bbd0a8` | `f5 ff 01 a9` | stp x21,xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd0ac"></a> `00bbd0ac` | `e8 3b 00 b9` | str w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbd0b0"></a> `00bbd0b0` | `e0 1b 00 fd` | str d0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbd0b4"></a> `00bbd0b4` | `e1 04 00 54` | b.ne 0x00bbd150 | `CONDITIONAL_JUMP`
<a id="insn-00bbd0b8"></a> `00bbd0b8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbd0bc"></a> `00bbd0bc` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd0c0"></a> `00bbd0c0` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbd0c4"></a> `00bbd0c4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbd0c8"></a> `00bbd0c8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbd0cc"></a> `00bbd0cc` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bbd0d0"></a> `00bbd0d0` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bbd0d4"></a> `00bbd0d4` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd0d8"></a> `00bbd0d8` | `c0 00 00 54` | b.eq 0x00bbd0f0 | `CONDITIONAL_JUMP`
<a id="insn-00bbd0dc"></a> `00bbd0dc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bbd0e0"></a> `00bbd0e0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bbd0e4"></a> `00bbd0e4` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbd0e8"></a> `00bbd0e8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbd0ec"></a> `00bbd0ec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbd0f0"></a> `00bbd0f0` | `e8 2b 42 a9` | ldp x8,x10,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd0f4"></a> `00bbd0f4` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd0f8"></a> `00bbd0f8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd0fc"></a> `00bbd0fc` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbd100"></a> `00bbd100` | `69 01 00 54` | b.ls 0x00bbd12c | `CONDITIONAL_JUMP`
<a id="insn-00bbd104"></a> `00bbd104` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd108"></a> `00bbd108` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bbd10c"></a> `00bbd10c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbd110"></a> `00bbd110` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bbd114"></a> `00bbd114` | `e1 17 00 f9` | str x1,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbd118"></a> `00bbd118` | `3a 80 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd11c"></a> `00bbd11c` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd120"></a> `00bbd120` | `80 02 00 b4` | cbz x0,0x00bbd170 | `CONDITIONAL_JUMP`
<a id="insn-00bbd124"></a> `00bbd124` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd128"></a> `00bbd128` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd12c"></a> `00bbd12c` | `e9 13 00 f9` | str x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd130"></a> `00bbd130` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bbd134"></a> `00bbd134` | `74 00 00 b4` | cbz x20,0x00bbd140 | `CONDITIONAL_JUMP`
<a id="insn-00bbd138"></a> `00bbd138` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd13c"></a> `00bbd13c` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbd140"></a> `00bbd140` | `f4 0f 40 f9` | ldr x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd144"></a> `00bbd144` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbd148"></a> `00bbd148` | `53 e4 ff b5` | cbnz x19,0x00bbcdd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbd14c"></a> `00bbd14c` | `22 ff ff 17` | b 0x00bbcdd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd150"></a> `00bbd150` | `a0 b6 ff 90` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00bbd154"></a> `00bbd154` | `00 f0 1f 91` | add x0,x0,#0x7fc | `FALL_THROUGH`
<a id="insn-00bbd158"></a> `00bbd158` | `81 b7 ff f0` | adrp x1,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbd15c"></a> `00bbd15c` | `21 34 26 91` | add x1,x1,#0x98d | `FALL_THROUGH`
<a id="insn-00bbd160"></a> `00bbd160` | `c3 b6 ff b0` | adrp x3,0x296000 | `FALL_THROUGH`
<a id="insn-00bbd164"></a> `00bbd164` | `63 98 21 91` | add x3,x3,#0x866 | `FALL_THROUGH`
<a id="insn-00bbd168"></a> `00bbd168` | `02 32 80 52` | mov w2,#0x190 | `FALL_THROUGH`
<a id="insn-00bbd16c"></a> `00bbd16c` | `fb f7 ff 97` | bl 0x00bbb158 | `CALL_TERMINATOR`
<a id="insn-00bbd170"></a> `00bbd170` | `40 84 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bbd174"></a> `00bbd174` | `03 78 00 94` | bl 0x00bdb180 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbcbcc`](#insn-00bbcbcc) 範囲 `[['00bbcbcc', '00bbcbf3']]`
  - `FALL_THROUGH` [`00bbcbf0`](#insn-00bbcbf0) → [`00bbcbf4`](#insn-00bbcbf4)
- ブロック [`00bbcbf4`](#insn-00bbcbf4) 範囲 `[['00bbcbf4', '00bbcbfb']]`
  - `CONDITIONAL_JUMP` [`00bbcbf8`](#insn-00bbcbf8) → [`00bbcc0c`](#insn-00bbcc0c)
  - `FALL_THROUGH` [`00bbcbf8`](#insn-00bbcbf8) → [`00bbcbfc`](#insn-00bbcbfc)
- ブロック [`00bbcbfc`](#insn-00bbcbfc) 範囲 `[['00bbcbfc', '00bbcbff']]`
  - `FALL_THROUGH` [`00bbcbfc`](#insn-00bbcbfc) → [`00bbcc00`](#insn-00bbcc00)
- ブロック [`00bbcc00`](#insn-00bbcc00) 範囲 `[['00bbcc00', '00bbcc07']]`
  - `CONDITIONAL_JUMP` [`00bbcc04`](#insn-00bbcc04) → [`00bbcc20`](#insn-00bbcc20)
  - `FALL_THROUGH` [`00bbcc04`](#insn-00bbcc04) → [`00bbcc08`](#insn-00bbcc08)
- ブロック [`00bbcc08`](#insn-00bbcc08) 範囲 `[['00bbcc08', '00bbcc0b']]`
  - `CONDITIONAL_JUMP` [`00bbcc08`](#insn-00bbcc08) → [`00bbcc20`](#insn-00bbcc20)
  - `FALL_THROUGH` [`00bbcc08`](#insn-00bbcc08) → [`00bbcc0c`](#insn-00bbcc0c)
- ブロック [`00bbcc0c`](#insn-00bbcc0c) 範囲 `[['00bbcc0c', '00bbcc13']]`
  - `CONDITIONAL_JUMP` [`00bbcc10`](#insn-00bbcc10) → [`00bbce5c`](#insn-00bbce5c)
  - `FALL_THROUGH` [`00bbcc10`](#insn-00bbcc10) → [`00bbcc14`](#insn-00bbcc14)
- ブロック [`00bbcc14`](#insn-00bbcc14) 範囲 `[['00bbcc14', '00bbcc1f']]`
  - `UNCONDITIONAL_JUMP` [`00bbcc1c`](#insn-00bbcc1c) → [`00bbce5c`](#insn-00bbce5c)
- ブロック [`00bbcc20`](#insn-00bbcc20) 範囲 `[['00bbcc20', '00bbcc67']]`
  - `FALL_THROUGH` [`00bbcc64`](#insn-00bbcc64) → [`00bbcc68`](#insn-00bbcc68)
- ブロック [`00bbcc68`](#insn-00bbcc68) 範囲 `[['00bbcc68', '00bbcca7']]`
  - `FALL_THROUGH` [`00bbcca4`](#insn-00bbcca4) → [`00bbcca8`](#insn-00bbcca8)
- ブロック [`00bbcca8`](#insn-00bbcca8) 範囲 `[['00bbcca8', '00bbcd13']]`
  - `FALL_THROUGH` [`00bbcd10`](#insn-00bbcd10) → [`00bbcd14`](#insn-00bbcd14)
- ブロック [`00bbcd14`](#insn-00bbcd14) 範囲 `[['00bbcd14', '00bbcd37']]`
  - `CONDITIONAL_JUMP` [`00bbcd34`](#insn-00bbcd34) → [`00bbcdb0`](#insn-00bbcdb0)
  - `FALL_THROUGH` [`00bbcd34`](#insn-00bbcd34) → [`00bbcd38`](#insn-00bbcd38)
- ブロック [`00bbcd38`](#insn-00bbcd38) 範囲 `[['00bbcd38', '00bbcd47']]`
  - `CONDITIONAL_JUMP` [`00bbcd44`](#insn-00bbcd44) → [`00bbce88`](#insn-00bbce88)
  - `FALL_THROUGH` [`00bbcd44`](#insn-00bbcd44) → [`00bbcd48`](#insn-00bbcd48)
- ブロック [`00bbcd48`](#insn-00bbcd48) 範囲 `[['00bbcd48', '00bbcd4f']]`
  - `CONDITIONAL_JUMP` [`00bbcd4c`](#insn-00bbcd4c) → [`00bbcdb0`](#insn-00bbcdb0)
  - `FALL_THROUGH` [`00bbcd4c`](#insn-00bbcd4c) → [`00bbcd50`](#insn-00bbcd50)
- ブロック [`00bbcd50`](#insn-00bbcd50) 範囲 `[['00bbcd50', '00bbcd53']]`
  - `FALL_THROUGH` [`00bbcd50`](#insn-00bbcd50) → [`00bbcd54`](#insn-00bbcd54)
- ブロック [`00bbcd54`](#insn-00bbcd54) 範囲 `[['00bbcd54', '00bbcd63']]`
  - `FALL_THROUGH` [`00bbcd60`](#insn-00bbcd60) → [`00bbcd64`](#insn-00bbcd64)
- ブロック [`00bbcd64`](#insn-00bbcd64) 範囲 `[['00bbcd64', '00bbcd6b']]`
  - `CONDITIONAL_JUMP` [`00bbcd68`](#insn-00bbcd68) → [`00bbce90`](#insn-00bbce90)
  - `FALL_THROUGH` [`00bbcd68`](#insn-00bbcd68) → [`00bbcd6c`](#insn-00bbcd6c)
- ブロック [`00bbcd6c`](#insn-00bbcd6c) 範囲 `[['00bbcd6c', '00bbcd73']]`
  - `CONDITIONAL_JUMP` [`00bbcd70`](#insn-00bbcd70) → [`00bbcdb0`](#insn-00bbcdb0)
  - `FALL_THROUGH` [`00bbcd70`](#insn-00bbcd70) → [`00bbcd74`](#insn-00bbcd74)
- ブロック [`00bbcd74`](#insn-00bbcd74) 範囲 `[['00bbcd74', '00bbcd87']]`
  - `CONDITIONAL_JUMP` [`00bbcd84`](#insn-00bbcd84) → [`00bbcf4c`](#insn-00bbcf4c)
  - `FALL_THROUGH` [`00bbcd84`](#insn-00bbcd84) → [`00bbcd88`](#insn-00bbcd88)
- ブロック [`00bbcd88`](#insn-00bbcd88) 範囲 `[['00bbcd88', '00bbcd8f']]`
  - `CONDITIONAL_JUMP` [`00bbcd8c`](#insn-00bbcd8c) → [`00bbcdb0`](#insn-00bbcdb0)
  - `FALL_THROUGH` [`00bbcd8c`](#insn-00bbcd8c) → [`00bbcd90`](#insn-00bbcd90)
- ブロック [`00bbcd90`](#insn-00bbcd90) 範囲 `[['00bbcd90', '00bbcdaf']]`
  - `CONDITIONAL_JUMP` [`00bbcdac`](#insn-00bbcdac) → [`00bbcf54`](#insn-00bbcf54)
  - `FALL_THROUGH` [`00bbcdac`](#insn-00bbcdac) → [`00bbcdb0`](#insn-00bbcdb0)
- ブロック [`00bbcdb0`](#insn-00bbcdb0) 範囲 `[['00bbcdb0', '00bbcdc3']]`
  - `CONDITIONAL_JUMP` [`00bbcdc0`](#insn-00bbcdc0) → [`00bbd07c`](#insn-00bbd07c)
  - `FALL_THROUGH` [`00bbcdc0`](#insn-00bbcdc0) → [`00bbcdc4`](#insn-00bbcdc4)
- ブロック [`00bbcdc4`](#insn-00bbcdc4) 範囲 `[['00bbcdc4', '00bbcdcf']]`
  - `CONDITIONAL_JUMP` [`00bbcdcc`](#insn-00bbcdcc) → [`00bbcdd4`](#insn-00bbcdd4)
  - `FALL_THROUGH` [`00bbcdcc`](#insn-00bbcdcc) → [`00bbcdd0`](#insn-00bbcdd0)
- ブロック [`00bbcdd0`](#insn-00bbcdd0) 範囲 `[['00bbcdd0', '00bbcdd3']]`
  - `FALL_THROUGH` [`00bbcdd0`](#insn-00bbcdd0) → [`00bbcdd4`](#insn-00bbcdd4)
- ブロック [`00bbcdd4`](#insn-00bbcdd4) 範囲 `[['00bbcdd4', '00bbcddb']]`
  - `CONDITIONAL_JUMP` [`00bbcdd8`](#insn-00bbcdd8) → [`00bbcde8`](#insn-00bbcde8)
  - `FALL_THROUGH` [`00bbcdd8`](#insn-00bbcdd8) → [`00bbcddc`](#insn-00bbcddc)
- ブロック [`00bbcddc`](#insn-00bbcddc) 範囲 `[['00bbcddc', '00bbcddf']]`
  - `UNCONDITIONAL_JUMP` [`00bbcddc`](#insn-00bbcddc) → [`00bbce04`](#insn-00bbce04)
- ブロック [`00bbcde0`](#insn-00bbcde0) 範囲 `[['00bbcde0', '00bbcde7']]`
  - `CONDITIONAL_JUMP` [`00bbcde4`](#insn-00bbcde4) → [`00bbce04`](#insn-00bbce04)
  - `FALL_THROUGH` [`00bbcde4`](#insn-00bbcde4) → [`00bbcde8`](#insn-00bbcde8)
- ブロック [`00bbcde8`](#insn-00bbcde8) 範囲 `[['00bbcde8', '00bbcdf7']]`
  - `CONDITIONAL_JUMP` [`00bbcdf4`](#insn-00bbcdf4) → [`00bbcde0`](#insn-00bbcde0)
  - `FALL_THROUGH` [`00bbcdf4`](#insn-00bbcdf4) → [`00bbcdf8`](#insn-00bbcdf8)
- ブロック [`00bbcdf8`](#insn-00bbcdf8) 範囲 `[['00bbcdf8', '00bbce03']]`
  - `CONDITIONAL_JUMP` [`00bbce00`](#insn-00bbce00) → [`00bbcde8`](#insn-00bbcde8)
  - `FALL_THROUGH` [`00bbce00`](#insn-00bbce00) → [`00bbce04`](#insn-00bbce04)
- ブロック [`00bbce04`](#insn-00bbce04) 範囲 `[['00bbce04', '00bbce17']]`
  - `CONDITIONAL_JUMP` [`00bbce14`](#insn-00bbce14) → [`00bbce1c`](#insn-00bbce1c)
  - `FALL_THROUGH` [`00bbce14`](#insn-00bbce14) → [`00bbce18`](#insn-00bbce18)
- ブロック [`00bbce18`](#insn-00bbce18) 範囲 `[['00bbce18', '00bbce1b']]`
  - `FALL_THROUGH` [`00bbce18`](#insn-00bbce18) → [`00bbce1c`](#insn-00bbce1c)
- ブロック [`00bbce1c`](#insn-00bbce1c) 範囲 `[['00bbce1c', '00bbce23']]`
  - `FALL_THROUGH` [`00bbce20`](#insn-00bbce20) → [`00bbce24`](#insn-00bbce24)
- ブロック [`00bbce24`](#insn-00bbce24) 範囲 `[['00bbce24', '00bbce27']]`
  - `CONDITIONAL_JUMP` [`00bbce24`](#insn-00bbce24) → [`00bbce2c`](#insn-00bbce2c)
  - `FALL_THROUGH` [`00bbce24`](#insn-00bbce24) → [`00bbce28`](#insn-00bbce28)
- ブロック [`00bbce28`](#insn-00bbce28) 範囲 `[['00bbce28', '00bbce2b']]`
  - `FALL_THROUGH` [`00bbce28`](#insn-00bbce28) → [`00bbce2c`](#insn-00bbce2c)
- ブロック [`00bbce2c`](#insn-00bbce2c) 範囲 `[['00bbce2c', '00bbce37']]`
  - `CONDITIONAL_JUMP` [`00bbce34`](#insn-00bbce34) → [`00bbce3c`](#insn-00bbce3c)
  - `FALL_THROUGH` [`00bbce34`](#insn-00bbce34) → [`00bbce38`](#insn-00bbce38)
- ブロック [`00bbce38`](#insn-00bbce38) 範囲 `[['00bbce38', '00bbce3b']]`
  - `FALL_THROUGH` [`00bbce38`](#insn-00bbce38) → [`00bbce3c`](#insn-00bbce3c)
- ブロック [`00bbce3c`](#insn-00bbce3c) 範囲 `[['00bbce3c', '00bbce47']]`
  - `CONDITIONAL_JUMP` [`00bbce44`](#insn-00bbce44) → [`00bbce4c`](#insn-00bbce4c)
  - `FALL_THROUGH` [`00bbce44`](#insn-00bbce44) → [`00bbce48`](#insn-00bbce48)
- ブロック [`00bbce48`](#insn-00bbce48) 範囲 `[['00bbce48', '00bbce4b']]`
  - `FALL_THROUGH` [`00bbce48`](#insn-00bbce48) → [`00bbce4c`](#insn-00bbce4c)
- ブロック [`00bbce4c`](#insn-00bbce4c) 範囲 `[['00bbce4c', '00bbce57']]`
  - `CONDITIONAL_JUMP` [`00bbce54`](#insn-00bbce54) → [`00bbce5c`](#insn-00bbce5c)
  - `FALL_THROUGH` [`00bbce54`](#insn-00bbce54) → [`00bbce58`](#insn-00bbce58)
- ブロック [`00bbce58`](#insn-00bbce58) 範囲 `[['00bbce58', '00bbce5b']]`
  - `FALL_THROUGH` [`00bbce58`](#insn-00bbce58) → [`00bbce5c`](#insn-00bbce5c)
- ブロック [`00bbce5c`](#insn-00bbce5c) 範囲 `[['00bbce5c', '00bbce87']]`
- ブロック [`00bbce88`](#insn-00bbce88) 範囲 `[['00bbce88', '00bbce8f']]`
  - `UNCONDITIONAL_JUMP` [`00bbce8c`](#insn-00bbce8c) → [`00bbce94`](#insn-00bbce94)
- ブロック [`00bbce90`](#insn-00bbce90) 範囲 `[['00bbce90', '00bbce93']]`
  - `FALL_THROUGH` [`00bbce90`](#insn-00bbce90) → [`00bbce94`](#insn-00bbce94)
- ブロック [`00bbce94`](#insn-00bbce94) 範囲 `[['00bbce94', '00bbcea7']]`
  - `CONDITIONAL_JUMP` [`00bbcea4`](#insn-00bbcea4) → [`00bbcdc4`](#insn-00bbcdc4)
  - `FALL_THROUGH` [`00bbcea4`](#insn-00bbcea4) → [`00bbcea8`](#insn-00bbcea8)
- ブロック [`00bbcea8`](#insn-00bbcea8) 範囲 `[['00bbcea8', '00bbceb3']]`
  - `CONDITIONAL_JUMP` [`00bbceb0`](#insn-00bbceb0) → [`00bbd080`](#insn-00bbd080)
  - `FALL_THROUGH` [`00bbceb0`](#insn-00bbceb0) → [`00bbceb4`](#insn-00bbceb4)
- ブロック [`00bbceb4`](#insn-00bbceb4) 範囲 `[['00bbceb4', '00bbcebf']]`
  - `CONDITIONAL_JUMP` [`00bbcebc`](#insn-00bbcebc) → [`00bbcdc4`](#insn-00bbcdc4)
  - `FALL_THROUGH` [`00bbcebc`](#insn-00bbcebc) → [`00bbcec0`](#insn-00bbcec0)
- ブロック [`00bbcec0`](#insn-00bbcec0) 範囲 `[['00bbcec0', '00bbced3']]`
  - `CONDITIONAL_JUMP` [`00bbced0`](#insn-00bbced0) → [`00bbcf00`](#insn-00bbcf00)
  - `FALL_THROUGH` [`00bbced0`](#insn-00bbced0) → [`00bbced4`](#insn-00bbced4)
- ブロック [`00bbced4`](#insn-00bbced4) 範囲 `[['00bbced4', '00bbcee7']]`
  - `CONDITIONAL_JUMP` [`00bbcee4`](#insn-00bbcee4) → [`00bbd174`](#insn-00bbd174)
  - `FALL_THROUGH` [`00bbcee4`](#insn-00bbcee4) → [`00bbcee8`](#insn-00bbcee8)
- ブロック [`00bbcee8`](#insn-00bbcee8) 範囲 `[['00bbcee8', '00bbceff']]`
  - `FALL_THROUGH` [`00bbcefc`](#insn-00bbcefc) → [`00bbcf00`](#insn-00bbcf00)
- ブロック [`00bbcf00`](#insn-00bbcf00) 範囲 `[['00bbcf00', '00bbcf4b']]`
  - `UNCONDITIONAL_JUMP` [`00bbcf48`](#insn-00bbcf48) → [`00bbd080`](#insn-00bbd080)
- ブロック [`00bbcf4c`](#insn-00bbcf4c) 範囲 `[['00bbcf4c', '00bbcf53']]`
  - `UNCONDITIONAL_JUMP` [`00bbcf50`](#insn-00bbcf50) → [`00bbcf58`](#insn-00bbcf58)
- ブロック [`00bbcf54`](#insn-00bbcf54) 範囲 `[['00bbcf54', '00bbcf57']]`
  - `FALL_THROUGH` [`00bbcf54`](#insn-00bbcf54) → [`00bbcf58`](#insn-00bbcf58)
- ブロック [`00bbcf58`](#insn-00bbcf58) 範囲 `[['00bbcf58', '00bbcf6f']]`
  - `CONDITIONAL_JUMP` [`00bbcf6c`](#insn-00bbcf6c) → [`00bbd07c`](#insn-00bbd07c)
  - `FALL_THROUGH` [`00bbcf6c`](#insn-00bbcf6c) → [`00bbcf70`](#insn-00bbcf70)
- ブロック [`00bbcf70`](#insn-00bbcf70) 範囲 `[['00bbcf70', '00bbcf7f']]`
  - `CONDITIONAL_JUMP` [`00bbcf7c`](#insn-00bbcf7c) → [`00bbcfb4`](#insn-00bbcfb4)
  - `FALL_THROUGH` [`00bbcf7c`](#insn-00bbcf7c) → [`00bbcf80`](#insn-00bbcf80)
- ブロック [`00bbcf80`](#insn-00bbcf80) 範囲 `[['00bbcf80', '00bbcfb3']]`
  - `CONDITIONAL_JUMP` [`00bbcfb0`](#insn-00bbcfb0) → [`00bbcfc0`](#insn-00bbcfc0)
  - `FALL_THROUGH` [`00bbcfb0`](#insn-00bbcfb0) → [`00bbcfb4`](#insn-00bbcfb4)
- ブロック [`00bbcfb4`](#insn-00bbcfb4) 範囲 `[['00bbcfb4', '00bbcfbb']]`
  - `CONDITIONAL_JUMP` [`00bbcfb8`](#insn-00bbcfb8) → [`00bbd080`](#insn-00bbd080)
  - `FALL_THROUGH` [`00bbcfb8`](#insn-00bbcfb8) → [`00bbcfbc`](#insn-00bbcfbc)
- ブロック [`00bbcfbc`](#insn-00bbcfbc) 範囲 `[['00bbcfbc', '00bbcfbf']]`
  - `UNCONDITIONAL_JUMP` [`00bbcfbc`](#insn-00bbcfbc) → [`00bbcdc4`](#insn-00bbcdc4)
- ブロック [`00bbcfc0`](#insn-00bbcfc0) 範囲 `[['00bbcfc0', '00bbcfcf']]`
  - `CONDITIONAL_JUMP` [`00bbcfcc`](#insn-00bbcfcc) → [`00bbd068`](#insn-00bbd068)
  - `FALL_THROUGH` [`00bbcfcc`](#insn-00bbcfcc) → [`00bbcfd0`](#insn-00bbcfd0)
- ブロック [`00bbcfd0`](#insn-00bbcfd0) 範囲 `[['00bbcfd0', '00bbcfdb']]`
  - `CONDITIONAL_JUMP` [`00bbcfd8`](#insn-00bbcfd8) → [`00bbcfe4`](#insn-00bbcfe4)
  - `FALL_THROUGH` [`00bbcfd8`](#insn-00bbcfd8) → [`00bbcfdc`](#insn-00bbcfdc)
- ブロック [`00bbcfdc`](#insn-00bbcfdc) 範囲 `[['00bbcfdc', '00bbcfe3']]`
  - `FALL_THROUGH` [`00bbcfe0`](#insn-00bbcfe0) → [`00bbcfe4`](#insn-00bbcfe4)
- ブロック [`00bbcfe4`](#insn-00bbcfe4) 範囲 `[['00bbcfe4', '00bbcfeb']]`
  - `CONDITIONAL_JUMP` [`00bbcfe8`](#insn-00bbcfe8) → [`00bbd004`](#insn-00bbd004)
  - `FALL_THROUGH` [`00bbcfe8`](#insn-00bbcfe8) → [`00bbcfec`](#insn-00bbcfec)
- ブロック [`00bbcfec`](#insn-00bbcfec) 範囲 `[['00bbcfec', '00bbcff7']]`
  - `FALL_THROUGH` [`00bbcff4`](#insn-00bbcff4) → [`00bbcff8`](#insn-00bbcff8)
- ブロック [`00bbcff8`](#insn-00bbcff8) 範囲 `[['00bbcff8', '00bbcffb']]`
  - `CONDITIONAL_JUMP` [`00bbcff8`](#insn-00bbcff8) → [`00bbd010`](#insn-00bbd010)
  - `FALL_THROUGH` [`00bbcff8`](#insn-00bbcff8) → [`00bbcffc`](#insn-00bbcffc)
- ブロック [`00bbcffc`](#insn-00bbcffc) 範囲 `[['00bbcffc', '00bbd003']]`
  - `UNCONDITIONAL_JUMP` [`00bbd000`](#insn-00bbd000) → [`00bbd044`](#insn-00bbd044)
- ブロック [`00bbd004`](#insn-00bbd004) 範囲 `[['00bbd004', '00bbd00f']]`
  - `UNCONDITIONAL_JUMP` [`00bbd00c`](#insn-00bbd00c) → [`00bbd044`](#insn-00bbd044)
- ブロック [`00bbd010`](#insn-00bbd010) 範囲 `[['00bbd010', '00bbd013']]`
  - `FALL_THROUGH` [`00bbd010`](#insn-00bbd010) → [`00bbd014`](#insn-00bbd014)
- ブロック [`00bbd014`](#insn-00bbd014) 範囲 `[['00bbd014', '00bbd023']]`
  - `CONDITIONAL_JUMP` [`00bbd020`](#insn-00bbd020) → [`00bbd038`](#insn-00bbd038)
  - `FALL_THROUGH` [`00bbd020`](#insn-00bbd020) → [`00bbd024`](#insn-00bbd024)
- ブロック [`00bbd024`](#insn-00bbd024) 範囲 `[['00bbd024', '00bbd02f']]`
  - `FALL_THROUGH` [`00bbd02c`](#insn-00bbd02c) → [`00bbd030`](#insn-00bbd030)
- ブロック [`00bbd030`](#insn-00bbd030) 範囲 `[['00bbd030', '00bbd033']]`
  - `CONDITIONAL_JUMP` [`00bbd030`](#insn-00bbd030) → [`00bbd014`](#insn-00bbd014)
  - `FALL_THROUGH` [`00bbd030`](#insn-00bbd030) → [`00bbd034`](#insn-00bbd034)
- ブロック [`00bbd034`](#insn-00bbd034) 範囲 `[['00bbd034', '00bbd037']]`
  - `FALL_THROUGH` [`00bbd034`](#insn-00bbd034) → [`00bbd038`](#insn-00bbd038)
- ブロック [`00bbd038`](#insn-00bbd038) 範囲 `[['00bbd038', '00bbd043']]`
  - `FALL_THROUGH` [`00bbd040`](#insn-00bbd040) → [`00bbd044`](#insn-00bbd044)
- ブロック [`00bbd044`](#insn-00bbd044) 範囲 `[['00bbd044', '00bbd047']]`
  - `FALL_THROUGH` [`00bbd044`](#insn-00bbd044) → [`00bbd048`](#insn-00bbd048)
- ブロック [`00bbd048`](#insn-00bbd048) 範囲 `[['00bbd048', '00bbd04b']]`
  - `CONDITIONAL_JUMP` [`00bbd048`](#insn-00bbd048) → [`00bbd050`](#insn-00bbd050)
  - `FALL_THROUGH` [`00bbd048`](#insn-00bbd048) → [`00bbd04c`](#insn-00bbd04c)
- ブロック [`00bbd04c`](#insn-00bbd04c) 範囲 `[['00bbd04c', '00bbd04f']]`
  - `CONDITIONAL_JUMP` [`00bbd04c`](#insn-00bbd04c) → [`00bbcfb4`](#insn-00bbcfb4)
  - `FALL_THROUGH` [`00bbd04c`](#insn-00bbd04c) → [`00bbd050`](#insn-00bbd050)
- ブロック [`00bbd050`](#insn-00bbd050) 範囲 `[['00bbd050', '00bbd057']]`
  - `CONDITIONAL_JUMP` [`00bbd054`](#insn-00bbd054) → [`00bbd068`](#insn-00bbd068)
  - `FALL_THROUGH` [`00bbd054`](#insn-00bbd054) → [`00bbd058`](#insn-00bbd058)
- ブロック [`00bbd058`](#insn-00bbd058) 範囲 `[['00bbd058', '00bbd05f']]`
  - `FALL_THROUGH` [`00bbd05c`](#insn-00bbd05c) → [`00bbd060`](#insn-00bbd060)
- ブロック [`00bbd060`](#insn-00bbd060) 範囲 `[['00bbd060', '00bbd063']]`
  - `CONDITIONAL_JUMP` [`00bbd060`](#insn-00bbd060) → [`00bbcfb4`](#insn-00bbcfb4)
  - `FALL_THROUGH` [`00bbd060`](#insn-00bbd060) → [`00bbd064`](#insn-00bbd064)
- ブロック [`00bbd064`](#insn-00bbd064) 範囲 `[['00bbd064', '00bbd067']]`
  - `FALL_THROUGH` [`00bbd064`](#insn-00bbd064) → [`00bbd068`](#insn-00bbd068)
- ブロック [`00bbd068`](#insn-00bbd068) 範囲 `[['00bbd068', '00bbd077']]`
  - `FALL_THROUGH` [`00bbd074`](#insn-00bbd074) → [`00bbd078`](#insn-00bbd078)
- ブロック [`00bbd078`](#insn-00bbd078) 範囲 `[['00bbd078', '00bbd07b']]`
  - `FALL_THROUGH` [`00bbd078`](#insn-00bbd078) → [`00bbd07c`](#insn-00bbd07c)
- ブロック [`00bbd07c`](#insn-00bbd07c) 範囲 `[['00bbd07c', '00bbd07f']]`
  - `CONDITIONAL_JUMP` [`00bbd07c`](#insn-00bbd07c) → [`00bbcdc4`](#insn-00bbcdc4)
  - `FALL_THROUGH` [`00bbd07c`](#insn-00bbd07c) → [`00bbd080`](#insn-00bbd080)
- ブロック [`00bbd080`](#insn-00bbd080) 範囲 `[['00bbd080', '00bbd083']]`
  - `CONDITIONAL_JUMP` [`00bbd080`](#insn-00bbd080) → [`00bbd08c`](#insn-00bbd08c)
  - `FALL_THROUGH` [`00bbd080`](#insn-00bbd080) → [`00bbd084`](#insn-00bbd084)
- ブロック [`00bbd084`](#insn-00bbd084) 範囲 `[['00bbd084', '00bbd08b']]`
  - `UNCONDITIONAL_JUMP` [`00bbd088`](#insn-00bbd088) → [`00bbd090`](#insn-00bbd090)
- ブロック [`00bbd08c`](#insn-00bbd08c) 範囲 `[['00bbd08c', '00bbd08f']]`
  - `FALL_THROUGH` [`00bbd08c`](#insn-00bbd08c) → [`00bbd090`](#insn-00bbd090)
- ブロック [`00bbd090`](#insn-00bbd090) 範囲 `[['00bbd090', '00bbd093']]`
  - `FALL_THROUGH` [`00bbd090`](#insn-00bbd090) → [`00bbd094`](#insn-00bbd094)
- ブロック [`00bbd094`](#insn-00bbd094) 範囲 `[['00bbd094', '00bbd0af']]`
  - `FALL_THROUGH` [`00bbd0ac`](#insn-00bbd0ac) → [`00bbd0b0`](#insn-00bbd0b0)
- ブロック [`00bbd0b0`](#insn-00bbd0b0) 範囲 `[['00bbd0b0', '00bbd0b7']]`
  - `CONDITIONAL_JUMP` [`00bbd0b4`](#insn-00bbd0b4) → [`00bbd150`](#insn-00bbd150)
  - `FALL_THROUGH` [`00bbd0b4`](#insn-00bbd0b4) → [`00bbd0b8`](#insn-00bbd0b8)
- ブロック [`00bbd0b8`](#insn-00bbd0b8) 範囲 `[['00bbd0b8', '00bbd0c7']]`
  - `FALL_THROUGH` [`00bbd0c4`](#insn-00bbd0c4) → [`00bbd0c8`](#insn-00bbd0c8)
- ブロック [`00bbd0c8`](#insn-00bbd0c8) 範囲 `[['00bbd0c8', '00bbd0cb']]`
  - `FALL_THROUGH` [`00bbd0c8`](#insn-00bbd0c8) → [`00bbd0cc`](#insn-00bbd0cc)
- ブロック [`00bbd0cc`](#insn-00bbd0cc) 範囲 `[['00bbd0cc', '00bbd0cf']]`
  - `FALL_THROUGH` [`00bbd0cc`](#insn-00bbd0cc) → [`00bbd0d0`](#insn-00bbd0d0)
- ブロック [`00bbd0d0`](#insn-00bbd0d0) 範囲 `[['00bbd0d0', '00bbd0d3']]`
  - `FALL_THROUGH` [`00bbd0d0`](#insn-00bbd0d0) → [`00bbd0d4`](#insn-00bbd0d4)
- ブロック [`00bbd0d4`](#insn-00bbd0d4) 範囲 `[['00bbd0d4', '00bbd0d7']]`
  - `FALL_THROUGH` [`00bbd0d4`](#insn-00bbd0d4) → [`00bbd0d8`](#insn-00bbd0d8)
- ブロック [`00bbd0d8`](#insn-00bbd0d8) 範囲 `[['00bbd0d8', '00bbd0db']]`
  - `CONDITIONAL_JUMP` [`00bbd0d8`](#insn-00bbd0d8) → [`00bbd0f0`](#insn-00bbd0f0)
  - `FALL_THROUGH` [`00bbd0d8`](#insn-00bbd0d8) → [`00bbd0dc`](#insn-00bbd0dc)
- ブロック [`00bbd0dc`](#insn-00bbd0dc) 範囲 `[['00bbd0dc', '00bbd0df']]`
  - `FALL_THROUGH` [`00bbd0dc`](#insn-00bbd0dc) → [`00bbd0e0`](#insn-00bbd0e0)
- ブロック [`00bbd0e0`](#insn-00bbd0e0) 範囲 `[['00bbd0e0', '00bbd0e3']]`
  - `FALL_THROUGH` [`00bbd0e0`](#insn-00bbd0e0) → [`00bbd0e4`](#insn-00bbd0e4)
- ブロック [`00bbd0e4`](#insn-00bbd0e4) 範囲 `[['00bbd0e4', '00bbd0ef']]`
  - `FALL_THROUGH` [`00bbd0ec`](#insn-00bbd0ec) → [`00bbd0f0`](#insn-00bbd0f0)
- ブロック [`00bbd0f0`](#insn-00bbd0f0) 範囲 `[['00bbd0f0', '00bbd0fb']]`
  - `FALL_THROUGH` [`00bbd0f8`](#insn-00bbd0f8) → [`00bbd0fc`](#insn-00bbd0fc)
- ブロック [`00bbd0fc`](#insn-00bbd0fc) 範囲 `[['00bbd0fc', '00bbd103']]`
  - `CONDITIONAL_JUMP` [`00bbd100`](#insn-00bbd100) → [`00bbd12c`](#insn-00bbd12c)
  - `FALL_THROUGH` [`00bbd100`](#insn-00bbd100) → [`00bbd104`](#insn-00bbd104)
- ブロック [`00bbd104`](#insn-00bbd104) 範囲 `[['00bbd104', '00bbd10b']]`
  - `FALL_THROUGH` [`00bbd108`](#insn-00bbd108) → [`00bbd10c`](#insn-00bbd10c)
- ブロック [`00bbd10c`](#insn-00bbd10c) 範囲 `[['00bbd10c', '00bbd10f']]`
  - `FALL_THROUGH` [`00bbd10c`](#insn-00bbd10c) → [`00bbd110`](#insn-00bbd110)
- ブロック [`00bbd110`](#insn-00bbd110) 範囲 `[['00bbd110', '00bbd123']]`
  - `CONDITIONAL_JUMP` [`00bbd120`](#insn-00bbd120) → [`00bbd170`](#insn-00bbd170)
  - `FALL_THROUGH` [`00bbd120`](#insn-00bbd120) → [`00bbd124`](#insn-00bbd124)
- ブロック [`00bbd124`](#insn-00bbd124) 範囲 `[['00bbd124', '00bbd127']]`
  - `FALL_THROUGH` [`00bbd124`](#insn-00bbd124) → [`00bbd128`](#insn-00bbd128)
- ブロック [`00bbd128`](#insn-00bbd128) 範囲 `[['00bbd128', '00bbd12b']]`
  - `FALL_THROUGH` [`00bbd128`](#insn-00bbd128) → [`00bbd12c`](#insn-00bbd12c)
- ブロック [`00bbd12c`](#insn-00bbd12c) 範囲 `[['00bbd12c', '00bbd137']]`
  - `CONDITIONAL_JUMP` [`00bbd134`](#insn-00bbd134) → [`00bbd140`](#insn-00bbd140)
  - `FALL_THROUGH` [`00bbd134`](#insn-00bbd134) → [`00bbd138`](#insn-00bbd138)
- ブロック [`00bbd138`](#insn-00bbd138) 範囲 `[['00bbd138', '00bbd13b']]`
  - `FALL_THROUGH` [`00bbd138`](#insn-00bbd138) → [`00bbd13c`](#insn-00bbd13c)
- ブロック [`00bbd13c`](#insn-00bbd13c) 範囲 `[['00bbd13c', '00bbd13f']]`
  - `FALL_THROUGH` [`00bbd13c`](#insn-00bbd13c) → [`00bbd140`](#insn-00bbd140)
- ブロック [`00bbd140`](#insn-00bbd140) 範囲 `[['00bbd140', '00bbd143']]`
  - `FALL_THROUGH` [`00bbd140`](#insn-00bbd140) → [`00bbd144`](#insn-00bbd144)
- ブロック [`00bbd144`](#insn-00bbd144) 範囲 `[['00bbd144', '00bbd14b']]`
  - `CONDITIONAL_JUMP` [`00bbd148`](#insn-00bbd148) → [`00bbcdd0`](#insn-00bbcdd0)
  - `FALL_THROUGH` [`00bbd148`](#insn-00bbd148) → [`00bbd14c`](#insn-00bbd14c)
- ブロック [`00bbd14c`](#insn-00bbd14c) 範囲 `[['00bbd14c', '00bbd14f']]`
  - `UNCONDITIONAL_JUMP` [`00bbd14c`](#insn-00bbd14c) → [`00bbcdd4`](#insn-00bbcdd4)
- ブロック [`00bbd150`](#insn-00bbd150) 範囲 `[['00bbd150', '00bbd15b']]`
  - `FALL_THROUGH` [`00bbd158`](#insn-00bbd158) → [`00bbd15c`](#insn-00bbd15c)
- ブロック [`00bbd15c`](#insn-00bbd15c) 範囲 `[['00bbd15c', '00bbd16f']]`
- ブロック [`00bbd170`](#insn-00bbd170) 範囲 `[['00bbd170', '00bbd173']]`
- ブロック [`00bbd174`](#insn-00bbd174) 範囲 `[['00bbd174', '00bbd177']]`

## 命令位置別の参照

- [`00bbcbd0`](#insn-00bbcbd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbd4`](#insn-00bbcbd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbd8`](#insn-00bbcbd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbdc`](#insn-00bbcbdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbe0`](#insn-00bbcbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbe4`](#insn-00bbcbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbf8`](#insn-00bbcbf8) → [`00bbcc0c`](#insn-00bbcc0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc04`](#insn-00bbcc04) → [`00bbcc20`](#insn-00bbcc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc08`](#insn-00bbcc08) → [`00bbcc20`](#insn-00bbcc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc10`](#insn-00bbcc10) → [`00bbce5c`](#insn-00bbce5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc1c`](#insn-00bbcc1c) → [`00bbce5c`](#insn-00bbce5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc28`](#insn-00bbcc28) → [`00bdb140`](../00bdb/00bdb140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb140` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc38`](#insn-00bbcc38) → `Stack[-0x13b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc44`](#insn-00bbcc44) → `Stack[-0x1390]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc50`](#insn-00bbcc50) → `Stack[-0x1278]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc5c`](#insn-00bbcc5c) → `Stack[-0x1160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc68`](#insn-00bbcc68) → `Stack[-0x1108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc74`](#insn-00bbcc74) → `Stack[-0x10d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc80`](#insn-00bbcc80) → `Stack[-0x10a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc90`](#insn-00bbcc90) → `Stack[-0x13a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc94`](#insn-00bbcc94) → `Stack[-0x12a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc98`](#insn-00bbcc98) → `Stack[-0x1388]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc9c`](#insn-00bbcc9c) → `Stack[-0x1378]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcca0`](#insn-00bbcca0) → `Stack[-0x1368]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcca4`](#insn-00bbcca4) → `Stack[-0x1358]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcca8`](#insn-00bbcca8) → `Stack[-0x1348]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccac`](#insn-00bbccac) → `Stack[-0x1338]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccb0`](#insn-00bbccb0) → `Stack[-0x1328]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccb4`](#insn-00bbccb4) → `Stack[-0x1318]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccb8`](#insn-00bbccb8) → `Stack[-0x1308]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccbc`](#insn-00bbccbc) → `Stack[-0x12f8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccc0`](#insn-00bbccc0) → `Stack[-0x12e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccc4`](#insn-00bbccc4) → `Stack[-0x12d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccc8`](#insn-00bbccc8) → `Stack[-0x12c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcccc`](#insn-00bbcccc) → `Stack[-0x12b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccd0`](#insn-00bbccd0) → `Stack[-0x1288]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccd4`](#insn-00bbccd4) → `Stack[-0x1270]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccd8`](#insn-00bbccd8) → `Stack[-0x1250]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccdc`](#insn-00bbccdc) → `Stack[-0x1230]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcce0`](#insn-00bbcce0) → `Stack[-0x1210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcce4`](#insn-00bbcce4) → `Stack[-0x11f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcce8`](#insn-00bbcce8) → `Stack[-0x11d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccec`](#insn-00bbccec) → `Stack[-0x11b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccf0`](#insn-00bbccf0) → `Stack[-0x1190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccf4`](#insn-00bbccf4) → `Stack[-0x1170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccf8`](#insn-00bbccf8) → `Stack[-0x1168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccfc`](#insn-00bbccfc) → `Stack[-0x1158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd00`](#insn-00bbcd00) → `Stack[-0x1138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd04`](#insn-00bbcd04) → `Stack[-0x1118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd08`](#insn-00bbcd08) → `Stack[-0x1110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd0c`](#insn-00bbcd0c) → `Stack[-0x1100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd10`](#insn-00bbcd10) → `Stack[-0x10e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd14`](#insn-00bbcd14) → `Stack[-0x10d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd18`](#insn-00bbcd18) → `Stack[-0x10c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd1c`](#insn-00bbcd1c) → `Stack[-0x10a6]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd20`](#insn-00bbcd20) → `Stack[-0x10a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd24`](#insn-00bbcd24) → `Stack[-0x1090]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd28`](#insn-00bbcd28) → `Stack[-0x1098]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd2c`](#insn-00bbcd2c) → `Stack[-0x1080]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd30`](#insn-00bbcd30) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd34`](#insn-00bbcd34) → [`00bbcdb0`](#insn-00bbcdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd44`](#insn-00bbcd44) → [`00bbce88`](#insn-00bbce88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd4c`](#insn-00bbcd4c) → [`00bbcdb0`](#insn-00bbcdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd68`](#insn-00bbcd68) → [`00bbce90`](#insn-00bbce90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd70`](#insn-00bbcd70) → [`00bbcdb0`](#insn-00bbcdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd84`](#insn-00bbcd84) → [`00bbcf4c`](#insn-00bbcf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd8c`](#insn-00bbcd8c) → [`00bbcdb0`](#insn-00bbcdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdac`](#insn-00bbcdac) → [`00bbcf54`](#insn-00bbcf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdb4`](#insn-00bbcdb4) → [`00bbde18`](../00bbd/00bbde18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde18` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdb8`](#insn-00bbcdb8) → `Stack[-0x13b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdc0`](#insn-00bbcdc0) → [`00bbd07c`](#insn-00bbd07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdcc`](#insn-00bbcdcc) → [`00bbcdd4`](#insn-00bbcdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdd4`](#insn-00bbcdd4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdd8`](#insn-00bbcdd8) → [`00bbcde8`](#insn-00bbcde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcddc`](#insn-00bbcddc) → [`00bbce04`](#insn-00bbce04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcde4`](#insn-00bbcde4) → [`00bbce04`](#insn-00bbce04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcde8`](#insn-00bbcde8) → `Stack[-0x1080]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdf0`](#insn-00bbcdf0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdf4`](#insn-00bbcdf4) → [`00bbcde0`](#insn-00bbcde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdf8`](#insn-00bbcdf8) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdfc`](#insn-00bbcdfc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce00`](#insn-00bbce00) → [`00bbcde8`](#insn-00bbcde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce04`](#insn-00bbce04) → `Stack[-0x10e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce08`](#insn-00bbce08) → `Stack[-0x1080]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce0c`](#insn-00bbce0c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce14`](#insn-00bbce14) → [`00bbce1c`](#insn-00bbce1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce18`](#insn-00bbce18) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce1c`](#insn-00bbce1c) → `Stack[-0x1118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce24`](#insn-00bbce24) → [`00bbce2c`](#insn-00bbce2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce28`](#insn-00bbce28) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce2c`](#insn-00bbce2c) → `Stack[-0x1170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce34`](#insn-00bbce34) → [`00bbce3c`](#insn-00bbce3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce38`](#insn-00bbce38) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce3c`](#insn-00bbce3c) → `Stack[-0x1288]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce44`](#insn-00bbce44) → [`00bbce4c`](#insn-00bbce4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce48`](#insn-00bbce48) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce4c`](#insn-00bbce4c) → `Stack[-0x13a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce54`](#insn-00bbce54) → [`00bbce5c`](#insn-00bbce5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce58`](#insn-00bbce58) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce68`](#insn-00bbce68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce6c`](#insn-00bbce6c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce70`](#insn-00bbce70) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce74`](#insn-00bbce74) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce78`](#insn-00bbce78) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce7c`](#insn-00bbce7c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce8c`](#insn-00bbce8c) → [`00bbce94`](#insn-00bbce94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce98`](#insn-00bbce98) → `Stack[-0x13b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcea0`](#insn-00bbcea0) → [`00bbd2c4`](../00bbd/00bbd2c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbd2c4` · 推定シンボル `None` · 推定型 `None`
- [`00bbcea4`](#insn-00bbcea4) → [`00bbcdc4`](#insn-00bbcdc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcea8`](#insn-00bbcea8) → `Stack[-0x13b0]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbceb0`](#insn-00bbceb0) → [`00bbd080`](#insn-00bbd080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcebc`](#insn-00bbcebc) → [`00bbcdc4`](#insn-00bbcdc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcec0`](#insn-00bbcec0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcec4`](#insn-00bbcec4) → `Stack[-0x1078]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbced0`](#insn-00bbced0) → [`00bbcf00`](#insn-00bbcf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbced4`](#insn-00bbced4) → `Stack[-0x13e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcedc`](#insn-00bbcedc) → `Stack[-0x13f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcee0`](#insn-00bbcee0) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bbcee4`](#insn-00bbcee4) → [`00bbd174`](#insn-00bbd174) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcee8`](#insn-00bbcee8) → `Stack[-0x13f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcef0`](#insn-00bbcef0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcefc`](#insn-00bbcefc) → `Stack[-0x13e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf08`](#insn-00bbcf08) → `Stack[-0x1078]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf14`](#insn-00bbcf14) → `00c199e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbcf40`](#insn-00bbcf40) → `Stack[-0x13a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf44`](#insn-00bbcf44) → `Stack[-0x13b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf48`](#insn-00bbcf48) → [`00bbd080`](#insn-00bbd080) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf50`](#insn-00bbcf50) → [`00bbcf58`](#insn-00bbcf58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf5c`](#insn-00bbcf5c) → `Stack[-0x13b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf64`](#insn-00bbcf64) → [`00bbd2c4`](../00bbd/00bbd2c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbd2c4` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf68`](#insn-00bbcf68) → `Stack[-0x13d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf6c`](#insn-00bbcf6c) → [`00bbd07c`](#insn-00bbd07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf70`](#insn-00bbcf70) → `Stack[-0x13b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf7c`](#insn-00bbcf7c) → [`00bbcfb4`](#insn-00bbcfb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfb0`](#insn-00bbcfb0) → [`00bbcfc0`](#insn-00bbcfc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfb8`](#insn-00bbcfb8) → [`00bbd080`](#insn-00bbd080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfbc`](#insn-00bbcfbc) → [`00bbcdc4`](#insn-00bbcdc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfc8`](#insn-00bbcfc8) → `Stack[-0x13b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfcc`](#insn-00bbcfcc) → [`00bbd068`](#insn-00bbd068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfd8`](#insn-00bbcfd8) → [`00bbcfe4`](#insn-00bbcfe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfe0`](#insn-00bbcfe0) → `Stack[-0x13b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfe8`](#insn-00bbcfe8) → [`00bbd004`](#insn-00bbd004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcff8`](#insn-00bbcff8) → [`00bbd010`](#insn-00bbd010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd000`](#insn-00bbd000) → [`00bbd044`](#insn-00bbd044) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd00c`](#insn-00bbd00c) → [`00bbd044`](#insn-00bbd044) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd020`](#insn-00bbd020) → [`00bbd038`](#insn-00bbd038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd02c`](#insn-00bbd02c) → `Stack[-0x13b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd030`](#insn-00bbd030) → [`00bbd014`](#insn-00bbd014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd048`](#insn-00bbd048) → [`00bbd050`](#insn-00bbd050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd04c`](#insn-00bbd04c) → [`00bbcfb4`](#insn-00bbcfb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd054`](#insn-00bbd054) → [`00bbd068`](#insn-00bbd068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd060`](#insn-00bbd060) → [`00bbcfb4`](#insn-00bbcfb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd064`](#insn-00bbd064) → `Stack[-0x13b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd06c`](#insn-00bbd06c) → `002a90e2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbd078`](#insn-00bbd078) → [`00bbdd64`](../00bbd/00bbdd64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd64` · 推定シンボル `None` · 推定型 `None`
- [`00bbd07c`](#insn-00bbd07c) → [`00bbcdc4`](#insn-00bbcdc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd080`](#insn-00bbd080) → [`00bbd08c`](#insn-00bbd08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd088`](#insn-00bbd088) → [`00bbd090`](#insn-00bbd090) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd094`](#insn-00bbd094) → `Stack[-0x10e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd098`](#insn-00bbd098) → `Stack[-0x10d8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd09c`](#insn-00bbd09c) → `Stack[-0x13c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0a8`](#insn-00bbd0a8) → `Stack[-0x13d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0ac`](#insn-00bbd0ac) → `Stack[-0x13b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0b0`](#insn-00bbd0b0) → `Stack[-0x13c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0b4`](#insn-00bbd0b4) → [`00bbd150`](#insn-00bbd150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0d8`](#insn-00bbd0d8) → [`00bbd0f0`](#insn-00bbd0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0f0`](#insn-00bbd0f0) → `Stack[-0x13d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0f4`](#insn-00bbd0f4) → `Stack[-0x13d8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd100`](#insn-00bbd100) → [`00bbd12c`](#insn-00bbd12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd114`](#insn-00bbd114) → `Stack[-0x13c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd118`](#insn-00bbd118) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bbd11c`](#insn-00bbd11c) → `Stack[-0x13d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd120`](#insn-00bbd120) → [`00bbd170`](#insn-00bbd170) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd124`](#insn-00bbd124) → `Stack[-0x13d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd12c`](#insn-00bbd12c) → `Stack[-0x13d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd134`](#insn-00bbd134) → [`00bbd140`](#insn-00bbd140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd138`](#insn-00bbd138) → `Stack[-0x13d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd140`](#insn-00bbd140) → `Stack[-0x13d8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd148`](#insn-00bbd148) → [`00bbcdd0`](#insn-00bbcdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd14c`](#insn-00bbd14c) → [`00bbcdd4`](#insn-00bbcdd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd154`](#insn-00bbd154) → `002917fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbd15c`](#insn-00bbd15c) → `002b098d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbd164`](#insn-00bbd164) → `00296866`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbd16c`](#insn-00bbd16c) → [`00bbb158`](../00bbb/00bbb158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb158` · 推定シンボル `None` · 推定型 `None`
- [`00bbd170`](#insn-00bbd170) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bbd174`](#insn-00bbd174) → [`00bdb180`](../00bdb/00bdb180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb180` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbcbd0`](#insn-00bbcbd0)

~~~json
{
  "source": "00bbcbd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbd4`](#insn-00bbcbd4)

~~~json
{
  "source": "00bbcbd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbd8`](#insn-00bbcbd8)

~~~json
{
  "source": "00bbcbd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbdc`](#insn-00bbcbdc)

~~~json
{
  "source": "00bbcbdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbe0`](#insn-00bbcbe0)

~~~json
{
  "source": "00bbcbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbe4`](#insn-00bbcbe4)

~~~json
{
  "source": "00bbcbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbf8`](#insn-00bbcbf8)

~~~json
{
  "source": "00bbcbf8",
  "target": "00bbcc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc04`](#insn-00bbcc04)

~~~json
{
  "source": "00bbcc04",
  "target": "00bbcc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc08`](#insn-00bbcc08)

~~~json
{
  "source": "00bbcc08",
  "target": "00bbcc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc10`](#insn-00bbcc10)

~~~json
{
  "source": "00bbcc10",
  "target": "00bbce5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc1c`](#insn-00bbcc1c)

~~~json
{
  "source": "00bbcc1c",
  "target": "00bbce5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc28`](#insn-00bbcc28)

~~~json
{
  "source": "00bbcc28",
  "target": "00bdb140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcc38`](#insn-00bbcc38)

~~~json
{
  "source": "00bbcc38",
  "target": "Stack[-0x13b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc44`](#insn-00bbcc44)

~~~json
{
  "source": "00bbcc44",
  "target": "Stack[-0x1390]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc50`](#insn-00bbcc50)

~~~json
{
  "source": "00bbcc50",
  "target": "Stack[-0x1278]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc5c`](#insn-00bbcc5c)

~~~json
{
  "source": "00bbcc5c",
  "target": "Stack[-0x1160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc68`](#insn-00bbcc68)

~~~json
{
  "source": "00bbcc68",
  "target": "Stack[-0x1108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc74`](#insn-00bbcc74)

~~~json
{
  "source": "00bbcc74",
  "target": "Stack[-0x10d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc80`](#insn-00bbcc80)

~~~json
{
  "source": "00bbcc80",
  "target": "Stack[-0x10a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc90`](#insn-00bbcc90)

~~~json
{
  "source": "00bbcc90",
  "target": "Stack[-0x13a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc94`](#insn-00bbcc94)

~~~json
{
  "source": "00bbcc94",
  "target": "Stack[-0x12a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc98`](#insn-00bbcc98)

~~~json
{
  "source": "00bbcc98",
  "target": "Stack[-0x1388]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc9c`](#insn-00bbcc9c)

~~~json
{
  "source": "00bbcc9c",
  "target": "Stack[-0x1378]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcca0`](#insn-00bbcca0)

~~~json
{
  "source": "00bbcca0",
  "target": "Stack[-0x1368]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcca4`](#insn-00bbcca4)

~~~json
{
  "source": "00bbcca4",
  "target": "Stack[-0x1358]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcca8`](#insn-00bbcca8)

~~~json
{
  "source": "00bbcca8",
  "target": "Stack[-0x1348]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccac`](#insn-00bbccac)

~~~json
{
  "source": "00bbccac",
  "target": "Stack[-0x1338]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccb0`](#insn-00bbccb0)

~~~json
{
  "source": "00bbccb0",
  "target": "Stack[-0x1328]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccb4`](#insn-00bbccb4)

~~~json
{
  "source": "00bbccb4",
  "target": "Stack[-0x1318]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccb8`](#insn-00bbccb8)

~~~json
{
  "source": "00bbccb8",
  "target": "Stack[-0x1308]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccbc`](#insn-00bbccbc)

~~~json
{
  "source": "00bbccbc",
  "target": "Stack[-0x12f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccc0`](#insn-00bbccc0)

~~~json
{
  "source": "00bbccc0",
  "target": "Stack[-0x12e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccc4`](#insn-00bbccc4)

~~~json
{
  "source": "00bbccc4",
  "target": "Stack[-0x12d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccc8`](#insn-00bbccc8)

~~~json
{
  "source": "00bbccc8",
  "target": "Stack[-0x12c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcccc`](#insn-00bbcccc)

~~~json
{
  "source": "00bbcccc",
  "target": "Stack[-0x12b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccd0`](#insn-00bbccd0)

~~~json
{
  "source": "00bbccd0",
  "target": "Stack[-0x1288]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccd4`](#insn-00bbccd4)

~~~json
{
  "source": "00bbccd4",
  "target": "Stack[-0x1270]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccd8`](#insn-00bbccd8)

~~~json
{
  "source": "00bbccd8",
  "target": "Stack[-0x1250]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccdc`](#insn-00bbccdc)

~~~json
{
  "source": "00bbccdc",
  "target": "Stack[-0x1230]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcce0`](#insn-00bbcce0)

~~~json
{
  "source": "00bbcce0",
  "target": "Stack[-0x1210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcce4`](#insn-00bbcce4)

~~~json
{
  "source": "00bbcce4",
  "target": "Stack[-0x11f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcce8`](#insn-00bbcce8)

~~~json
{
  "source": "00bbcce8",
  "target": "Stack[-0x11d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccec`](#insn-00bbccec)

~~~json
{
  "source": "00bbccec",
  "target": "Stack[-0x11b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccf0`](#insn-00bbccf0)

~~~json
{
  "source": "00bbccf0",
  "target": "Stack[-0x1190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccf4`](#insn-00bbccf4)

~~~json
{
  "source": "00bbccf4",
  "target": "Stack[-0x1170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccf8`](#insn-00bbccf8)

~~~json
{
  "source": "00bbccf8",
  "target": "Stack[-0x1168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccfc`](#insn-00bbccfc)

~~~json
{
  "source": "00bbccfc",
  "target": "Stack[-0x1158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd00`](#insn-00bbcd00)

~~~json
{
  "source": "00bbcd00",
  "target": "Stack[-0x1138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd04`](#insn-00bbcd04)

~~~json
{
  "source": "00bbcd04",
  "target": "Stack[-0x1118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd08`](#insn-00bbcd08)

~~~json
{
  "source": "00bbcd08",
  "target": "Stack[-0x1110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd0c`](#insn-00bbcd0c)

~~~json
{
  "source": "00bbcd0c",
  "target": "Stack[-0x1100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd10`](#insn-00bbcd10)

~~~json
{
  "source": "00bbcd10",
  "target": "Stack[-0x10e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd14`](#insn-00bbcd14)

~~~json
{
  "source": "00bbcd14",
  "target": "Stack[-0x10d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd18`](#insn-00bbcd18)

~~~json
{
  "source": "00bbcd18",
  "target": "Stack[-0x10c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd1c`](#insn-00bbcd1c)

~~~json
{
  "source": "00bbcd1c",
  "target": "Stack[-0x10a6]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd20`](#insn-00bbcd20)

~~~json
{
  "source": "00bbcd20",
  "target": "Stack[-0x10a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd24`](#insn-00bbcd24)

~~~json
{
  "source": "00bbcd24",
  "target": "Stack[-0x1090]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd28`](#insn-00bbcd28)

~~~json
{
  "source": "00bbcd28",
  "target": "Stack[-0x1098]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd2c`](#insn-00bbcd2c)

~~~json
{
  "source": "00bbcd2c",
  "target": "Stack[-0x1080]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd30`](#insn-00bbcd30)

~~~json
{
  "source": "00bbcd30",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd34`](#insn-00bbcd34)

~~~json
{
  "source": "00bbcd34",
  "target": "00bbcdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd44`](#insn-00bbcd44)

~~~json
{
  "source": "00bbcd44",
  "target": "00bbce88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd4c`](#insn-00bbcd4c)

~~~json
{
  "source": "00bbcd4c",
  "target": "00bbcdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd68`](#insn-00bbcd68)

~~~json
{
  "source": "00bbcd68",
  "target": "00bbce90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd70`](#insn-00bbcd70)

~~~json
{
  "source": "00bbcd70",
  "target": "00bbcdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd84`](#insn-00bbcd84)

~~~json
{
  "source": "00bbcd84",
  "target": "00bbcf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd8c`](#insn-00bbcd8c)

~~~json
{
  "source": "00bbcd8c",
  "target": "00bbcdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdac`](#insn-00bbcdac)

~~~json
{
  "source": "00bbcdac",
  "target": "00bbcf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdb4`](#insn-00bbcdb4)

~~~json
{
  "source": "00bbcdb4",
  "target": "00bbde18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcdb8`](#insn-00bbcdb8)

~~~json
{
  "source": "00bbcdb8",
  "target": "Stack[-0x13b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdc0`](#insn-00bbcdc0)

~~~json
{
  "source": "00bbcdc0",
  "target": "00bbd07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdcc`](#insn-00bbcdcc)

~~~json
{
  "source": "00bbcdcc",
  "target": "00bbcdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdd4`](#insn-00bbcdd4)

~~~json
{
  "source": "00bbcdd4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdd8`](#insn-00bbcdd8)

~~~json
{
  "source": "00bbcdd8",
  "target": "00bbcde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcddc`](#insn-00bbcddc)

~~~json
{
  "source": "00bbcddc",
  "target": "00bbce04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcde4`](#insn-00bbcde4)

~~~json
{
  "source": "00bbcde4",
  "target": "00bbce04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcde8`](#insn-00bbcde8)

~~~json
{
  "source": "00bbcde8",
  "target": "Stack[-0x1080]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdf0`](#insn-00bbcdf0)

~~~json
{
  "source": "00bbcdf0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdf4`](#insn-00bbcdf4)

~~~json
{
  "source": "00bbcdf4",
  "target": "00bbcde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdf8`](#insn-00bbcdf8)

~~~json
{
  "source": "00bbcdf8",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcdfc`](#insn-00bbcdfc)

~~~json
{
  "source": "00bbcdfc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce00`](#insn-00bbce00)

~~~json
{
  "source": "00bbce00",
  "target": "00bbcde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce04`](#insn-00bbce04)

~~~json
{
  "source": "00bbce04",
  "target": "Stack[-0x10e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce08`](#insn-00bbce08)

~~~json
{
  "source": "00bbce08",
  "target": "Stack[-0x1080]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce0c`](#insn-00bbce0c)

~~~json
{
  "source": "00bbce0c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce14`](#insn-00bbce14)

~~~json
{
  "source": "00bbce14",
  "target": "00bbce1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce18`](#insn-00bbce18)

~~~json
{
  "source": "00bbce18",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce1c`](#insn-00bbce1c)

~~~json
{
  "source": "00bbce1c",
  "target": "Stack[-0x1118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce24`](#insn-00bbce24)

~~~json
{
  "source": "00bbce24",
  "target": "00bbce2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce28`](#insn-00bbce28)

~~~json
{
  "source": "00bbce28",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce2c`](#insn-00bbce2c)

~~~json
{
  "source": "00bbce2c",
  "target": "Stack[-0x1170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce34`](#insn-00bbce34)

~~~json
{
  "source": "00bbce34",
  "target": "00bbce3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce38`](#insn-00bbce38)

~~~json
{
  "source": "00bbce38",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce3c`](#insn-00bbce3c)

~~~json
{
  "source": "00bbce3c",
  "target": "Stack[-0x1288]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce44`](#insn-00bbce44)

~~~json
{
  "source": "00bbce44",
  "target": "00bbce4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce48`](#insn-00bbce48)

~~~json
{
  "source": "00bbce48",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce4c`](#insn-00bbce4c)

~~~json
{
  "source": "00bbce4c",
  "target": "Stack[-0x13a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce54`](#insn-00bbce54)

~~~json
{
  "source": "00bbce54",
  "target": "00bbce5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce58`](#insn-00bbce58)

~~~json
{
  "source": "00bbce58",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce68`](#insn-00bbce68)

~~~json
{
  "source": "00bbce68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce6c`](#insn-00bbce6c)

~~~json
{
  "source": "00bbce6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce70`](#insn-00bbce70)

~~~json
{
  "source": "00bbce70",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce74`](#insn-00bbce74)

~~~json
{
  "source": "00bbce74",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce78`](#insn-00bbce78)

~~~json
{
  "source": "00bbce78",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce7c`](#insn-00bbce7c)

~~~json
{
  "source": "00bbce7c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce8c`](#insn-00bbce8c)

~~~json
{
  "source": "00bbce8c",
  "target": "00bbce94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce98`](#insn-00bbce98)

~~~json
{
  "source": "00bbce98",
  "target": "Stack[-0x13b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcea0`](#insn-00bbcea0)

~~~json
{
  "source": "00bbcea0",
  "target": "00bbd2c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcea4`](#insn-00bbcea4)

~~~json
{
  "source": "00bbcea4",
  "target": "00bbcdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcea8`](#insn-00bbcea8)

~~~json
{
  "source": "00bbcea8",
  "target": "Stack[-0x13b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbceb0`](#insn-00bbceb0)

~~~json
{
  "source": "00bbceb0",
  "target": "00bbd080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcebc`](#insn-00bbcebc)

~~~json
{
  "source": "00bbcebc",
  "target": "00bbcdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcec0`](#insn-00bbcec0)

~~~json
{
  "source": "00bbcec0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcec4`](#insn-00bbcec4)

~~~json
{
  "source": "00bbcec4",
  "target": "Stack[-0x1078]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbced0`](#insn-00bbced0)

~~~json
{
  "source": "00bbced0",
  "target": "00bbcf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbced4`](#insn-00bbced4)

~~~json
{
  "source": "00bbced4",
  "target": "Stack[-0x13e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcedc`](#insn-00bbcedc)

~~~json
{
  "source": "00bbcedc",
  "target": "Stack[-0x13f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcee0`](#insn-00bbcee0)

~~~json
{
  "source": "00bbcee0",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcee4`](#insn-00bbcee4)

~~~json
{
  "source": "00bbcee4",
  "target": "00bbd174",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcee8`](#insn-00bbcee8)

~~~json
{
  "source": "00bbcee8",
  "target": "Stack[-0x13f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcef0`](#insn-00bbcef0)

~~~json
{
  "source": "00bbcef0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcefc`](#insn-00bbcefc)

~~~json
{
  "source": "00bbcefc",
  "target": "Stack[-0x13e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf08`](#insn-00bbcf08)

~~~json
{
  "source": "00bbcf08",
  "target": "Stack[-0x1078]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf14`](#insn-00bbcf14)

~~~json
{
  "source": "00bbcf14",
  "target": "00c199e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c199e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbcf40`](#insn-00bbcf40)

~~~json
{
  "source": "00bbcf40",
  "target": "Stack[-0x13a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf44`](#insn-00bbcf44)

~~~json
{
  "source": "00bbcf44",
  "target": "Stack[-0x13b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf48`](#insn-00bbcf48)

~~~json
{
  "source": "00bbcf48",
  "target": "00bbd080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf50`](#insn-00bbcf50)

~~~json
{
  "source": "00bbcf50",
  "target": "00bbcf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf5c`](#insn-00bbcf5c)

~~~json
{
  "source": "00bbcf5c",
  "target": "Stack[-0x13b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf64`](#insn-00bbcf64)

~~~json
{
  "source": "00bbcf64",
  "target": "00bbd2c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf68`](#insn-00bbcf68)

~~~json
{
  "source": "00bbcf68",
  "target": "Stack[-0x13d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf6c`](#insn-00bbcf6c)

~~~json
{
  "source": "00bbcf6c",
  "target": "00bbd07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf70`](#insn-00bbcf70)

~~~json
{
  "source": "00bbcf70",
  "target": "Stack[-0x13b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf7c`](#insn-00bbcf7c)

~~~json
{
  "source": "00bbcf7c",
  "target": "00bbcfb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfb0`](#insn-00bbcfb0)

~~~json
{
  "source": "00bbcfb0",
  "target": "00bbcfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfb8`](#insn-00bbcfb8)

~~~json
{
  "source": "00bbcfb8",
  "target": "00bbd080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfbc`](#insn-00bbcfbc)

~~~json
{
  "source": "00bbcfbc",
  "target": "00bbcdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfc8`](#insn-00bbcfc8)

~~~json
{
  "source": "00bbcfc8",
  "target": "Stack[-0x13b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfcc`](#insn-00bbcfcc)

~~~json
{
  "source": "00bbcfcc",
  "target": "00bbd068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfd8`](#insn-00bbcfd8)

~~~json
{
  "source": "00bbcfd8",
  "target": "00bbcfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfe0`](#insn-00bbcfe0)

~~~json
{
  "source": "00bbcfe0",
  "target": "Stack[-0x13b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfe8`](#insn-00bbcfe8)

~~~json
{
  "source": "00bbcfe8",
  "target": "00bbd004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcff8`](#insn-00bbcff8)

~~~json
{
  "source": "00bbcff8",
  "target": "00bbd010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd000`](#insn-00bbd000)

~~~json
{
  "source": "00bbd000",
  "target": "00bbd044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd00c`](#insn-00bbd00c)

~~~json
{
  "source": "00bbd00c",
  "target": "00bbd044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd020`](#insn-00bbd020)

~~~json
{
  "source": "00bbd020",
  "target": "00bbd038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd02c`](#insn-00bbd02c)

~~~json
{
  "source": "00bbd02c",
  "target": "Stack[-0x13b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd030`](#insn-00bbd030)

~~~json
{
  "source": "00bbd030",
  "target": "00bbd014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd048`](#insn-00bbd048)

~~~json
{
  "source": "00bbd048",
  "target": "00bbd050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd04c`](#insn-00bbd04c)

~~~json
{
  "source": "00bbd04c",
  "target": "00bbcfb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd054`](#insn-00bbd054)

~~~json
{
  "source": "00bbd054",
  "target": "00bbd068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd060`](#insn-00bbd060)

~~~json
{
  "source": "00bbd060",
  "target": "00bbcfb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd064`](#insn-00bbd064)

~~~json
{
  "source": "00bbd064",
  "target": "Stack[-0x13b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd06c`](#insn-00bbd06c)

~~~json
{
  "source": "00bbd06c",
  "target": "002a90e2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a90e2",
  "offset": 0,
  "size": 34,
  "datatype": "string",
  "bytes": "696e766f636174696f6e2066756e6374696f6e20666f7220626c6f636b20696e",
  "capture_start": "002a90e2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbd078`](#insn-00bbd078)

~~~json
{
  "source": "00bbd078",
  "target": "00bbdd64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd07c`](#insn-00bbd07c)

~~~json
{
  "source": "00bbd07c",
  "target": "00bbcdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd080`](#insn-00bbd080)

~~~json
{
  "source": "00bbd080",
  "target": "00bbd08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd088`](#insn-00bbd088)

~~~json
{
  "source": "00bbd088",
  "target": "00bbd090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd094`](#insn-00bbd094)

~~~json
{
  "source": "00bbd094",
  "target": "Stack[-0x10e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd098`](#insn-00bbd098)

~~~json
{
  "source": "00bbd098",
  "target": "Stack[-0x10d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd09c`](#insn-00bbd09c)

~~~json
{
  "source": "00bbd09c",
  "target": "Stack[-0x13c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd0a8`](#insn-00bbd0a8)

~~~json
{
  "source": "00bbd0a8",
  "target": "Stack[-0x13d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd0ac`](#insn-00bbd0ac)

~~~json
{
  "source": "00bbd0ac",
  "target": "Stack[-0x13b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd0b0`](#insn-00bbd0b0)

~~~json
{
  "source": "00bbd0b0",
  "target": "Stack[-0x13c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd0b4`](#insn-00bbd0b4)

~~~json
{
  "source": "00bbd0b4",
  "target": "00bbd150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd0d8`](#insn-00bbd0d8)

~~~json
{
  "source": "00bbd0d8",
  "target": "00bbd0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd0f0`](#insn-00bbd0f0)

~~~json
{
  "source": "00bbd0f0",
  "target": "Stack[-0x13d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd0f4`](#insn-00bbd0f4)

~~~json
{
  "source": "00bbd0f4",
  "target": "Stack[-0x13d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd100`](#insn-00bbd100)

~~~json
{
  "source": "00bbd100",
  "target": "00bbd12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd114`](#insn-00bbd114)

~~~json
{
  "source": "00bbd114",
  "target": "Stack[-0x13c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd118`](#insn-00bbd118)

~~~json
{
  "source": "00bbd118",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd11c`](#insn-00bbd11c)

~~~json
{
  "source": "00bbd11c",
  "target": "Stack[-0x13d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd120`](#insn-00bbd120)

~~~json
{
  "source": "00bbd120",
  "target": "00bbd170",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd124`](#insn-00bbd124)

~~~json
{
  "source": "00bbd124",
  "target": "Stack[-0x13d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd12c`](#insn-00bbd12c)

~~~json
{
  "source": "00bbd12c",
  "target": "Stack[-0x13d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd134`](#insn-00bbd134)

~~~json
{
  "source": "00bbd134",
  "target": "00bbd140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd138`](#insn-00bbd138)

~~~json
{
  "source": "00bbd138",
  "target": "Stack[-0x13d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd140`](#insn-00bbd140)

~~~json
{
  "source": "00bbd140",
  "target": "Stack[-0x13d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd148`](#insn-00bbd148)

~~~json
{
  "source": "00bbd148",
  "target": "00bbcdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd14c`](#insn-00bbd14c)

~~~json
{
  "source": "00bbd14c",
  "target": "00bbcdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd154`](#insn-00bbd154)

~~~json
{
  "source": "00bbd154",
  "target": "002917fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002917fc",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "25733a25643a20257300",
  "capture_start": "002917fc",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbd15c`](#insn-00bbd15c)

~~~json
{
  "source": "00bbd15c",
  "target": "002b098d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b098d",
  "offset": 0,
  "size": 48,
  "datatype": "string",
  "bytes": "6f75742f6c6c766d2d70726f6a6563742f6c69626378786162692f7372632f63",
  "capture_start": "002b098d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbd164`](#insn-00bbd164)

~~~json
{
  "source": "00bbd164",
  "target": "00296866",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296866",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "00296866",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbd16c`](#insn-00bbd16c)

~~~json
{
  "source": "00bbd16c",
  "target": "00bbb158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd170`](#insn-00bbd170)

~~~json
{
  "source": "00bbd170",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd174`](#insn-00bbd174)

~~~json
{
  "source": "00bbd174",
  "target": "00bdb180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
