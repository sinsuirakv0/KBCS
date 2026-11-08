# 00bbcbcc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

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
  "source_text_sha256": "837f0bb18cedd6ea1c0c360341ca28442e7b49a70eb6372d422578b273d9e241"
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
