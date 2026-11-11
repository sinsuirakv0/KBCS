# 00c1afec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00c1afec",
  "name": "FUN_00c1afec",
  "size": 800,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3cbd0d3b3dd63b8a10086e1dd2a708c951d9d269ca740eeff67babd77df8523f",
  "source_text_sha256": "3cbd0d3b3dd63b8a10086e1dd2a708c951d9d269ca740eeff67babd77df8523f"
}
~~~

## 呼び出し元

- [00c1acc0](../00c1a/00c1acc0.md)

## 呼び出し先

- [006d76a0](../006d7/006d76a0.md)
- [00c53f5c](../00c53/00c53f5c.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57f40](../00c57/00c57f40.md)
- [00c58000](../00c58/00c58000.md)
- [00c5a8a0](../00c5a/00c5a8a0.md)
- [00c5dff0](../00c5d/00c5dff0.md)

## 疑似コード / UTF-8 5681 bytes

~~~c

ulong * FUN_00c1afec(ulong *param_1,undefined4 *param_2,undefined4 *param_3)

{
  size_t __n;
  ulong uVar1;
  ulong uVar2;
  long lVar3;
  ulong uVar4;
  undefined8 *puVar5;
  bool bVar6;
  undefined8 uVar7;
  uint uVar8;
  undefined4 *puVar9;
  undefined4 *puVar10;
  ulong uVar11;
  undefined8 *puVar12;
  undefined8 *puVar13;
  ulong uVar14;
  void *pvVar15;
  byte bVar16;
  ulong uVar17;
  ulong uVar18;
  undefined4 *puVar19;
  long lVar20;
  undefined8 uVar21;
  undefined8 uVar22;
  ulong local_78;
  ulong local_70;
  void *local_68;
  
  uVar4 = *param_1;
  uVar14 = param_1[1];
                    /* try { // try from 00c1b020 to 00d1b02b has its CatchHandler @ 00c1b738 */
  bVar6 = ((byte)*param_1 & 1) != 0;
  lVar20 = (uVar4 & 0xfffffffffffffffe) - 1;
  uVar2 = (ulong)(byte)((byte)*param_1 >> 1);
                    /* try { // try from 00c1b02c to 00d1b0d7 has its CatchHandler @ 00c1b79c */
  if (bVar6) {
    uVar2 = uVar14;
  }
  lVar3 = 4;
  if (bVar6) {
    lVar3 = lVar20;
  }
  uVar11 = (long)param_3 - (long)param_2;
  if (uVar11 == 0) {
    return param_1;
  }
  puVar19 = (undefined4 *)param_1[2];
  uVar8 = (uint)uVar4;
  puVar10 = (undefined4 *)((long)param_1 + 4);
  uVar18 = uVar4 >> 1 & 0x7f;
  uVar17 = (long)uVar11 >> 2;
  uVar1 = uVar18;
  puVar9 = puVar10;
  if ((uVar4 & 1) != 0) {
    uVar1 = uVar14;
    puVar9 = puVar19;
  }
  if ((puVar9 <= param_2) && (param_2 < puVar9 + uVar1 + 1)) {
    if (0x3ffffffffffffff7 < uVar17) {
      uVar7 = FUN_006d76a0(&local_78);
      if ((local_78 & 1) != 0) {
        _ZdlPv(local_68);
      }
                    /* WARNING: Subroutine does not return */
      FUN_00c53f5c(uVar7);
    }
    if (uVar17 < 5) {
      pvVar15 = (void *)((ulong)&local_78 | 4);
      local_78 = CONCAT71(local_78._1_7_,(char)(uVar11 >> 1)) & 0xfffffffffffffffe;
    }
    else {
                    /* try { // try from 00c1b134 to 00d1b13f has its CatchHandler @ 00c1b734 */
                    /* try { // try from 00c1b140 to 00d1b14f has its CatchHandler @ 00c1b720 */
      uVar2 = (uVar17 & 0x3ffffffffffffffe) + 2;
      if ((uVar17 | 1) != 5) {
        uVar2 = uVar17 | 1;
      }
                    /* try { // try from 00c1b150 to 00d1b163 has its CatchHandler @ 00c1b708 */
      pvVar15 = (void *)_Znwm((uVar2 + 1) * 4);
      local_78 = uVar2 + 1 | 1;
      local_70 = uVar17;
      local_68 = pvVar15;
    }
    __n = (uVar11 - 4 & 0xfffffffffffffffc) + 4;
    memcpy(pvVar15,param_2,__n);
    *(undefined4 *)((long)pvVar15 + __n) = 0;
    bVar16 = (byte)local_78 & 1;
    uVar2 = (ulong)((byte)local_78 >> 1);
    pvVar15 = (void *)((ulong)&local_78 | 4);
    if ((local_78 & 1) != 0) {
      uVar2 = local_70;
      pvVar15 = local_68;
    }
    lVar3 = 4;
    if ((uVar4 & 1) != 0) {
      lVar3 = lVar20;
    }
                    /* try { // try from 00c1b1c4 to 00d1b1cf has its CatchHandler @ 00c1b7bc */
    if ((uVar4 & 1) != 0) {
      uVar18 = uVar14;
    }
                    /* try { // try from 00c1b1d0 to 00d1b1df has its CatchHandler @ 00c1b7c0 */
    if (lVar3 - uVar18 < uVar2) {
      _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE21__grow_by_and_replaceEmmmmmmPKw
                (param_1,lVar3,(uVar2 - lVar3) + uVar18,uVar18,uVar18,0);
                    /* try { // try from 00c1b1f4 to 00d1b1fb has its CatchHandler @ 00c1b7a0 */
      bVar16 = (byte)local_78 & 1;
    }
    else if (uVar2 != 0) {
      if ((uVar4 & 1) != 0) {
        puVar10 = puVar19;
      }
      memmove(puVar10 + uVar18,pvVar15,uVar2 << 2);
      uVar18 = uVar18 + uVar2;
      if ((*param_1 & 1) == 0) {
        *(char *)param_1 = (char)((int)uVar18 << 1);
                    /* try { // try from 00c1b230 to 00d1b23b has its CatchHandler @ 00c1b704 */
      }
      else {
        param_1[1] = uVar18;
      }
      puVar10[uVar18] = 0;
    }
    if (bVar16 == 0) {
      return param_1;
    }
    _ZdlPv(local_68);
    return param_1;
  }
  if (lVar3 - uVar2 < uVar17) {
    _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9__grow_byEmmmmmm
              (param_1,lVar3,(uVar2 + uVar17) - lVar3,uVar2,uVar2,0,0);
    puVar19 = (undefined4 *)param_1[2];
    param_1[1] = uVar2;
    uVar8 = (uint)(byte)*param_1;
  }
                    /* try { // try from 00c1b0fc to 00d1b103 has its CatchHandler @ 00c1b7a0 */
  if ((uVar8 & 1) != 0) {
    puVar10 = puVar19;
  }
  puVar9 = puVar10 + uVar2;
  if ((0x1b < uVar11 - 4) && (0x1f < (long)puVar10 + (uVar2 * 4 - (long)param_2))) {
    puVar12 = (undefined8 *)(puVar10 + uVar2 + 4);
                    /* try { // try from 00c1b23c to 00d1b24b has its CatchHandler @ 00c1b6f0 */
    uVar4 = (uVar11 - 4 >> 2) + 1;
    uVar11 = uVar4 & 0x7ffffffffffffff8;
                    /* try { // try from 00c1b24c to 00d1b25f has its CatchHandler @ 00c1b6d8 */
    puVar9 = puVar9 + uVar11;
    puVar13 = (undefined8 *)(param_2 + 4);
    uVar14 = uVar11;
    do {
      puVar5 = puVar13 + -1;
      uVar7 = puVar13[-2];
      uVar22 = puVar13[1];
      uVar21 = *puVar13;
      uVar14 = uVar14 - 8;
      puVar13 = puVar13 + 4;
      puVar12[-1] = *puVar5;
      puVar12[-2] = uVar7;
      puVar12[1] = uVar22;
      *puVar12 = uVar21;
      puVar12 = puVar12 + 4;
    } while (uVar14 != 0);
    param_2 = param_2 + uVar11;
    if (uVar4 == uVar11) goto LAB_00c1b288;
  }
  do {
    puVar19 = param_2 + 1;
    puVar10 = puVar9 + 1;
    *puVar9 = *param_2;
    puVar9 = puVar10;
    param_2 = puVar19;
  } while (puVar19 != param_3);
LAB_00c1b288:
  *puVar9 = 0;
  if ((*param_1 & 1) == 0) {
    *(char *)param_1 = (char)((int)(uVar2 + uVar17) << 1);
  }
  else {
    param_1[1] = uVar2 + uVar17;
  }
  return param_1;
}

~~~
