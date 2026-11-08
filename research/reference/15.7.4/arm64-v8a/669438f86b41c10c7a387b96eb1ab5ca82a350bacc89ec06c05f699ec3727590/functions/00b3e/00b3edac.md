# 00b3edac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00b3edac",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__append_forward_unsafeIPKcEERS5_T_SA_",
  "size": 656,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e96d183da6d5f793922e0cb8c7d66e30bb5de494cf5b717c75abb3be9f466837",
  "source_text_sha256": "e96d183da6d5f793922e0cb8c7d66e30bb5de494cf5b717c75abb3be9f466837"
}
~~~

## 呼び出し元

- [00bdfcf0](../00bdf/00bdfcf0.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb130](../00bdb/00bdb130.md)
- [00bdda90](../00bdd/00bdda90.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 疑似コード / UTF-8 5124 bytes

~~~c

ulong * _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__append_forward_unsafeIPKcEERS5_T_SA_
                  (ulong *param_1,undefined1 *param_2,undefined1 *param_3)

{
  byte bVar1;
  uint uVar2;
  long lVar3;
  undefined8 *puVar4;
  ulong uVar5;
  undefined1 *puVar6;
  long lVar7;
  ulong uVar8;
  undefined1 *puVar9;
  ulong uVar10;
  undefined8 *puVar11;
  undefined8 *puVar12;
  undefined1 *puVar13;
  ulong uVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  undefined8 uVar17;
  ulong local_60;
  ulong local_58;
  undefined1 *local_50;
  long local_48;
  
  lVar3 = tpidr_el0;
  local_48 = *(long *)(lVar3 + 0x28);
  bVar1 = (byte)*param_1;
  if ((bVar1 & 1) == 0) {
    uVar14 = (ulong)(bVar1 >> 1);
    lVar7 = 0x16;
    uVar8 = (ulong)bVar1;
  }
  else {
    uVar8 = *param_1;
    uVar14 = param_1[1];
    lVar7 = (uVar8 & 0xfffffffffffffffe) - 1;
  }
  uVar5 = (long)param_3 - (long)param_2;
  if (uVar5 == 0) goto LAB_00b3f008;
  if ((bVar1 & 1) == 0) {
    puVar9 = (undefined1 *)((long)param_1 + 1);
    uVar10 = (ulong)(bVar1 >> 1);
  }
  else {
    uVar10 = param_1[1];
    puVar9 = (undefined1 *)param_1[2];
  }
  if ((puVar9 <= param_2) && (param_2 < puVar9 + uVar10)) {
    local_58 = 0;
    local_50 = (undefined1 *)0x0;
    local_60 = 0;
    if (0xffffffffffffffef < uVar5) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    if (uVar5 < 0x17) {
      uVar2 = (int)uVar5 << 1;
      uVar8 = (ulong)uVar2;
      local_60 = (ulong)(byte)uVar2;
      puVar9 = (undefined1 *)((ulong)&local_60 | 1);
    }
    else {
      uVar8 = uVar5 + 0x10 & 0xfffffffffffffff0;
      puVar9 = (undefined1 *)_Znwm(uVar8);
      uVar8 = uVar8 | 1;
      local_60 = uVar8;
      local_50 = puVar9;
      local_58 = uVar5;
    }
    if (param_2 != param_3) {
      puVar6 = puVar9;
      if (0x1f < uVar5) {
        uVar10 = uVar5 & 0xffffffffffffffe0;
        puVar12 = (undefined8 *)(puVar9 + 0x10);
        puVar9 = puVar9 + uVar10;
        puVar11 = (undefined8 *)(param_2 + 0x10);
        uVar14 = uVar10;
        do {
          puVar4 = puVar11 + -1;
          uVar15 = puVar11[-2];
          uVar17 = puVar11[1];
          uVar16 = *puVar11;
          uVar14 = uVar14 - 0x20;
          puVar11 = puVar11 + 4;
          puVar12[-1] = *puVar4;
          puVar12[-2] = uVar15;
          puVar12[1] = uVar17;
          *puVar12 = uVar16;
          puVar12 = puVar12 + 4;
        } while (uVar14 != 0);
        puVar6 = puVar9;
        param_2 = param_2 + uVar10;
        if (uVar5 == uVar10) goto LAB_00b3efd0;
      }
      do {
        puVar13 = param_2 + 1;
        puVar9 = puVar6 + 1;
        *puVar6 = *param_2;
        puVar6 = puVar9;
        param_2 = puVar13;
      } while (param_3 != puVar13);
    }
LAB_00b3efd0:
    *puVar9 = 0;
    uVar14 = (ulong)((uint)uVar8 >> 1 & 0x7f);
    puVar9 = (undefined1 *)((ulong)&local_60 | 1);
    if ((uVar8 & 1) != 0) {
      uVar14 = local_58;
      puVar9 = local_50;
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
              (param_1,puVar9,uVar14);
    if ((local_60 & 1) != 0) {
      _ZdlPv(local_50);
    }
    goto LAB_00b3f008;
  }
  if (lVar7 - uVar14 < uVar5) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
              (param_1,lVar7,(uVar14 + uVar5) - lVar7,uVar14,uVar14,0,0);
                    /* try { // try from 00b3eeac to 00c3efd7 has its CatchHandler @ 00b40c88 */
    uVar8 = (ulong)(byte)*param_1;
  }
  if ((uVar8 & 1) == 0) {
    uVar8 = (long)param_1 + 1;
  }
  else {
    uVar8 = param_1[2];
  }
  puVar9 = (undefined1 *)(uVar8 + uVar14);
  if (param_2 != param_3) {
    puVar6 = puVar9;
    if ((0x1f < uVar5) &&
       ((param_3 <= puVar9 || (param_3 + uVar8 + (uVar14 - (long)param_2) <= param_2)))) {
      uVar10 = uVar5 & 0xffffffffffffffe0;
      puVar12 = (undefined8 *)(param_2 + 0x10);
      puVar9 = puVar9 + uVar10;
      puVar11 = (undefined8 *)(uVar14 + uVar8 + 0x10);
      uVar8 = uVar10;
      do {
        puVar4 = puVar12 + -1;
        uVar15 = puVar12[-2];
        uVar17 = puVar12[1];
        uVar16 = *puVar12;
        puVar12 = puVar12 + 4;
        uVar8 = uVar8 - 0x20;
        puVar11[-1] = *puVar4;
        puVar11[-2] = uVar15;
        puVar11[1] = uVar17;
        *puVar11 = uVar16;
        puVar11 = puVar11 + 4;
      } while (uVar8 != 0);
      puVar6 = puVar9;
      param_2 = param_2 + uVar10;
      if (uVar5 == uVar10) goto LAB_00b3ef3c;
    }
    do {
      puVar13 = param_2 + 1;
      puVar9 = puVar6 + 1;
      *puVar6 = *param_2;
      puVar6 = puVar9;
      param_2 = puVar13;
    } while (param_3 != puVar13);
  }
LAB_00b3ef3c:
  *puVar9 = 0;
  if ((*param_1 & 1) == 0) {
    *(char *)param_1 = (char)((int)(uVar14 + uVar5) << 1);
  }
  else {
    param_1[1] = uVar14 + uVar5;
  }
LAB_00b3f008:
                    /* try { // try from 00b3f010 to 00c3f02b has its CatchHandler @ 00b40ccc */
  if (*(long *)(lVar3 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return param_1;
}

~~~
