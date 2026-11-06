# 00b8faec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00b8faec",
  "name": "FUN_00b8faec",
  "size": 992,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "add2024fa89e33f4eb2804ee8bce8633fa615af76c6b5ff8cce7adb3f7545168",
  "source_text_sha256": "add2024fa89e33f4eb2804ee8bce8633fa615af76c6b5ff8cce7adb3f7545168"
}
~~~

## 呼び出し元

- [00b8fae4](../00b8f/00b8fae4.md)

## 呼び出し先

- [00bb9940](../00bb9/00bb9940.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdefc0](../00bde/00bdefc0.md)
- [00be1540](../00be1/00be1540.md)
- [00be15a0](../00be1/00be15a0.md)
- [00be15b0](../00be1/00be15b0.md)

## 疑似コード / UTF-8 6879 bytes

~~~c

long * FUN_00b8faec(undefined8 param_1,long *param_2,long *param_3,long param_4,uint *param_5,
                   undefined8 *param_6)

{
  uint uVar1;
  ulong uVar2;
  long *plVar3;
  bool bVar4;
  int iVar5;
  ulong uVar6;
  undefined8 uVar7;
  void *pvVar8;
  ulong uVar9;
  undefined4 uVar10;
  void *pvVar11;
  undefined4 local_1bc;
  undefined4 *local_1b8;
  undefined4 auStack_1b0 [40];
  void *local_110;
  undefined8 local_108;
  ulong local_100;
  void *local_f8;
  byte local_f0 [8];
  ulong local_e8;
  void *local_e0;
  undefined1 auStack_d4 [104];
  undefined4 local_6c [3];
  
  uVar1 = *(uint *)(param_4 + 8) & 0x4a;
  if (uVar1 == 0) {
    uVar10 = 0;
  }
  else if (uVar1 == 0x40) {
    uVar10 = 8;
  }
  else if (uVar1 == 8) {
    uVar10 = 0x10;
  }
  else {
    uVar10 = 10;
  }
  _ZNSt6__ndk19__num_getIwE17__stage2_int_prepERNS_8ios_baseEPwRw
            (local_f0,param_4,auStack_d4,local_6c);
  local_108 = 0;
  local_100 = 0;
  local_f8 = (void *)0x0;
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc(&local_108,0x16,0);
  local_1b8 = auStack_1b0;
  pvVar11 = (void *)((ulong)&local_108 | 1);
  local_1bc = 0;
  pvVar8 = local_f8;
  if ((local_108 & 1) == 0) {
    pvVar8 = (void *)((long)&local_108 + 1);
  }
  local_110 = pvVar8;
LAB_00b8fbcc:
  if (param_2 == (long *)0x0) {
    bVar4 = true;
    if (param_3 != (long *)0x0) goto LAB_00b8fc14;
LAB_00b8fbec:
    if (bVar4 != false) goto LAB_00b8fd90;
  }
  else {
    if ((int *)param_2[3] == (int *)param_2[4]) {
      iVar5 = (**(code **)(*param_2 + 0x48))(param_2);
    }
    else {
      iVar5 = *(int *)param_2[3];
    }
    bVar4 = iVar5 == -1;
    plVar3 = (long *)0x0;
    if (!bVar4) {
      plVar3 = param_2;
    }
    param_2 = plVar3;
    if (param_3 == (long *)0x0) goto LAB_00b8fbec;
LAB_00b8fc14:
    if ((int *)param_3[3] == (int *)param_3[4]) {
                    /* try { // try from 00b8fc34 to 00c8fc3b has its CatchHandler @ 00b8feb8 */
      iVar5 = (**(code **)(*param_3 + 0x48))(param_3);
    }
    else {
      iVar5 = *(int *)param_3[3];
    }
    plVar3 = (long *)0x0;
    if (iVar5 != -1) {
      plVar3 = param_3;
    }
    param_3 = plVar3;
                    /* try { // try from 00b8fc48 to 00c8fc93 has its CatchHandler @ 00b8fec0 */
    if (bVar4 == (iVar5 == -1)) goto LAB_00b8fd90;
  }
  uVar6 = local_108 >> 1 & 0x7f;
  if ((local_108 & 1) != 0) {
    uVar6 = local_100;
  }
  if (local_110 == (void *)((long)pvVar8 + uVar6)) {
    if ((long)uVar6 < 1) {
      uVar9 = uVar6 * 2;
      pvVar8 = local_f8;
      uVar2 = uVar9;
      if ((local_108 & 1) == 0) {
        local_108 = CONCAT71(local_108._1_7_,(char)((int)uVar9 << 1));
        pvVar8 = pvVar11;
        uVar2 = local_100;
                    /* try { // try from 00b8fca0 to 00c8fcbb has its CatchHandler @ 00b8fea0 */
      }
      local_100 = uVar2;
      *(undefined1 *)((long)pvVar8 + uVar9) = 0;
    }
    else {
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
                (&local_108,uVar6,0);
    }
                    /* try { // try from 00b8fcbc to 00c8fd4b has its CatchHandler @ 00b8f8f8 */
    uVar2 = 0x16;
    if ((local_108 & 1) != 0) {
      uVar2 = (local_108 & 0xfffffffffffffffe) - 1;
    }
    uVar9 = local_108 >> 1 & 0x7f;
    if ((local_108 & 1) != 0) {
      uVar9 = local_100;
    }
    if (uVar2 < uVar9 || uVar2 - uVar9 == 0) {
      pvVar8 = local_f8;
      uVar9 = uVar2;
      if ((local_108 & 1) == 0) {
        local_108 = CONCAT71(local_108._1_7_,(char)((int)uVar2 << 1));
        pvVar8 = pvVar11;
        uVar9 = local_100;
      }
      local_100 = uVar9;
      *(undefined1 *)((long)pvVar8 + uVar2) = 0;
    }
    else {
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
                (&local_108,uVar2 - uVar9,0);
    }
    pvVar8 = pvVar11;
    if ((local_108 & 1) != 0) {
      pvVar8 = local_f8;
    }
    local_110 = (void *)((long)pvVar8 + uVar6);
  }
  if ((uint *)param_2[3] == (uint *)param_2[4]) {
    uVar6 = (**(code **)(*param_2 + 0x48))(param_2);
  }
  else {
    uVar6 = (ulong)*(uint *)param_2[3];
  }
                    /* try { // try from 00b8fd4c to 00c8fd4f has its CatchHandler @ 00b8feb8 */
  iVar5 = _ZNSt6__ndk19__num_getIwE17__stage2_int_loopEwiPcRS2_RjwRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSD_Pw
                    (uVar6,uVar10,pvVar8,&local_110,&local_1bc,local_6c[0],local_f0,auStack_1b0,
                     &local_1b8,auStack_d4);
  if (iVar5 != 0) goto LAB_00b8fd90;
                    /* try { // try from 00b8fd78 to 00c8fda7 has its CatchHandler @ 00b8fed0 */
  if (param_2[3] == param_2[4]) {
    (**(code **)(*param_2 + 0x50))(param_2);
  }
  else {
    param_2[3] = param_2[3] + 4;
  }
  goto LAB_00b8fbcc;
LAB_00b8fd90:
  uVar6 = (ulong)(local_f0[0] >> 1);
  if ((local_f0[0] & 1) != 0) {
    uVar6 = local_e8;
  }
                    /* try { // try from 00b8fda8 to 00c8fffb has its CatchHandler @ 00b8f8f8 */
  if ((uVar6 != 0) && ((long)local_1b8 - (long)auStack_1b0 < 0xa0)) {
    *local_1b8 = local_1bc;
    local_1b8 = local_1b8 + 1;
  }
  uVar7 = FUN_00bb9940(pvVar8,local_110,param_5,uVar10);
  *param_6 = uVar7;
  _ZNSt6__ndk116__check_groupingERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjS8_Rj
            (local_f0,auStack_1b0,local_1b8,param_5);
  if (param_2 == (long *)0x0) {
    bVar4 = true;
    if (param_3 != (long *)0x0) goto LAB_00b8fe44;
LAB_00b8fe1c:
    if (!bVar4) goto LAB_00b8fe84;
  }
  else {
    if ((int *)param_2[3] == (int *)param_2[4]) {
      iVar5 = (**(code **)(*param_2 + 0x48))(param_2);
    }
    else {
      iVar5 = *(int *)param_2[3];
    }
    bVar4 = iVar5 == -1;
    plVar3 = (long *)0x0;
    if (!bVar4) {
      plVar3 = param_2;
    }
    param_2 = plVar3;
    if (param_3 == (long *)0x0) goto LAB_00b8fe1c;
LAB_00b8fe44:
    if ((int *)param_3[3] == (int *)param_3[4]) {
      iVar5 = (**(code **)(*param_3 + 0x48))(param_3);
    }
    else {
      iVar5 = *(int *)param_3[3];
    }
    if (bVar4 != (iVar5 == -1)) goto LAB_00b8fe84;
  }
  *param_5 = *param_5 | 2;
LAB_00b8fe84:
                    /* catch() { ... } // from try @ 00b8fa4c with catch @ 00b8fe88 */
  if ((local_108 & 1) != 0) {
                    /* catch() { ... } // from try @ 00b8f9f0 with catch @ 00b8fe90 */
    _ZdlPv(local_f8);
  }
  if ((local_f0[0] & 1) != 0) {
                    /* catch() { ... } // from try @ 00b8fca0 with catch @ 00b8fea0 */
    _ZdlPv(local_e0);
  }
                    /* catch() { ... } // from try @ 00b8fc34 with catch @ 00b8feb8
                       catch() { ... } // from try @ 00b8fd4c with catch @ 00b8feb8 */
                    /* catch() { ... } // from try @ 00b8fc48 with catch @ 00b8fec0 */
                    /* catch() { ... } // from try @ 00b8fa14 with catch @ 00b8fec8 */
  return param_2;
}

~~~
