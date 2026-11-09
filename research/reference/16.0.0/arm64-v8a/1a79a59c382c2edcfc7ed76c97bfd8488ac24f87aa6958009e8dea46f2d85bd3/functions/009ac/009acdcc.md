# 009acdcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "009acdcc",
  "name": "FUN_009acdcc",
  "size": 1284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23a007eee0ea7b9c4eb42853c6722f4063d95b1423b313faa001a7ab37622243",
  "source_text_sha256": "23a007eee0ea7b9c4eb42853c6722f4063d95b1423b313faa001a7ab37622243"
}
~~~

## 呼び出し元

- [0075eb40](../0075e/0075eb40.md)

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [006b8c04](../006b8/006b8c04.md)
- [008065d4](../00806/008065d4.md)
- [009b0a4c](../009b0/009b0a4c.md)
- [009b0ba8](../009b0/009b0ba8.md)
- [009b0bbc](../009b0/009b0bbc.md)
- [009b1c40](../009b1/009b1c40.md)
- [009b3fb8](../009b3/009b3fb8.md)
- [009b5af8](../009b5/009b5af8.md)
- [009b5b08](../009b5/009b5b08.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c53b3c](../00c53/00c53b3c.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57c00](../00c57/00c57c00.md)

## 疑似コード / UTF-8 8816 bytes

~~~c

void FUN_009acdcc(undefined8 *param_1)

{
  undefined8 *puVar1;
  long **pplVar2;
  undefined8 *puVar3;
  long lVar4;
  ulong *puVar5;
  ulong *puVar6;
  ulong *__src;
  ulong *puVar7;
  int iVar8;
  undefined4 uVar9;
  ulong uVar10;
  ulong *puVar11;
  long *plVar12;
  ulong uVar13;
  long *plVar14;
  undefined8 uVar15;
  long lVar16;
  ulong uVar17;
  long *plVar18;
  long *local_a8;
  long *local_a0;
  long local_98;
  ulong *local_90;
  ulong *local_88;
  ulong *local_80;
  long **local_78;
  long *local_70;
  long local_68;
  
                    /* try { // try from 009acdec to 00aacdf7 has its CatchHandler @ 009acf20 */
  lVar4 = tpidr_el0;
  local_68 = *(long *)(lVar4 + 0x28);
  puVar1 = (undefined8 *)*param_1;
  puVar3 = (undefined8 *)param_1[1];
  local_90 = (ulong *)0x0;
  local_88 = (ulong *)0x0;
  local_80 = (ulong *)0x0;
  puVar11 = local_90;
                    /* try { // try from 009ace10 to 00aace2b has its CatchHandler @ 009ace9c */
  for (; local_90 = puVar11, puVar1 != puVar3; puVar1 = puVar1 + 2) {
                    /* try { // try from 009ace2c to 00aacf2f has its CatchHandler @ 009acd10 */
    plVar14 = (long *)*puVar1;
    plVar18 = (long *)puVar1[1];
    local_a8 = plVar14;
    local_a0 = plVar18;
    puVar5 = puVar11;
    puVar6 = local_88;
    if (plVar18 != (long *)0x0) {
      FUN_00c538b0(1,plVar18 + 1);
      puVar11 = local_90;
      puVar5 = local_90;
      puVar6 = local_88;
    }
    for (; puVar7 = local_88, __src = local_90, local_90 = puVar5, puVar11 != local_88;
        puVar11 = puVar11 + 1) {
      uVar10 = *puVar11;
      local_88 = puVar6;
      iVar8 = FUN_009b3fb8(plVar14);
      puVar5 = local_88;
      if ((int)uVar10 == iVar8) goto joined_r0x009aceb0;
      puVar5 = local_90;
      puVar6 = local_88;
      local_88 = puVar7;
      local_90 = __src;
    }
    local_88 = puVar6;
    iVar8 = FUN_009b5b08(plVar14);
    puVar5 = local_88;
    if (iVar8 != 0) {
      uVar10 = FUN_009b3fb8(plVar14);
      lVar16 = FUN_009b5af8(plVar14);
                    /* catch() { ... } // from try @ 009ace10 with catch @ 009ace9c */
      uVar10 = uVar10 & 0xffffffff | lVar16 << 0x20;
      if (puVar7 < local_80) {
        *puVar7 = uVar10;
        puVar5 = puVar7 + 1;
      }
      else {
        lVar16 = (long)puVar7 - (long)__src >> 3;
        uVar13 = lVar16 + 1;
        if (uVar13 >> 0x3d != 0) {
          if (*(long *)(lVar4 + 0x28) == local_68) {
            FUN_006b8c04(&local_90);
LAB_009ad25c:
            if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_00440e80();
            }
          }
          goto LAB_009ad304;
        }
        uVar17 = (long)local_80 - (long)__src >> 2;
        if (uVar17 <= uVar13) {
          uVar17 = uVar13;
        }
        if (0x7ffffffffffffff7 < (ulong)((long)local_80 - (long)__src)) {
          uVar17 = 0x1fffffffffffffff;
        }
        if (uVar17 == 0) {
          puVar11 = (ulong *)0x0;
        }
        else {
          if (uVar17 >> 0x3d != 0) goto LAB_009ad25c;
                    /* catch() { ... } // from try @ 009acdec with catch @ 009acf20 */
          puVar11 = (ulong *)_Znwm(uVar17 << 3);
        }
        puVar5 = puVar11 + lVar16;
        *puVar5 = uVar10;
        memcpy(puVar11,__src,(long)puVar7 - (long)__src);
        local_90 = puVar11;
        puVar5 = puVar5 + 1;
        local_80 = puVar11 + uVar17;
        if (__src != (ulong *)0x0) {
          _ZdlPv(__src);
        }
      }
    }
joined_r0x009aceb0:
    local_88 = puVar5;
    if ((plVar18 != (long *)0x0) &&
       (lVar16 = FUN_00c538e0(0xffffffffffffffff,plVar18 + 1), lVar16 == 0)) {
      (**(code **)(*plVar18 + 0x10))(plVar18);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
    }
    puVar11 = local_90;
  }
  lVar16 = 0;
  if (local_88 != puVar11) {
    lVar16 = LZCOUNT((long)local_88 - (long)puVar11 >> 3) * -2 + 0x7e;
  }
  FUN_009b0bbc(local_88,local_88,puVar11,puVar11,lVar16,1);
  plVar14 = (long *)*param_1;
  plVar18 = (long *)param_1[1];
  local_78 = &local_a8;
  local_a8 = (long *)0x0;
  local_a0 = (long *)0x0;
  local_98 = 0;
  lVar16 = (long)plVar18 - (long)plVar14;
  local_70 = (long *)((ulong)local_70 & 0xffffffffffffff00);
  if (lVar16 != 0) {
    if (lVar16 < 0) {
      if (*(long *)(lVar4 + 0x28) == local_68) {
        uVar15 = FUN_009b0ba8(&local_a8);
        FUN_009b1c40(&local_78);
        if (local_90 != (ulong *)0x0) {
          local_88 = local_90;
          _ZdlPv(local_90);
        }
        if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_00c53b3c(uVar15);
        }
      }
      goto LAB_009ad304;
    }
    plVar12 = (long *)_Znwm(lVar16);
    local_98 = (long)plVar12 + lVar16;
    local_a8 = plVar12;
    local_a0 = plVar12;
    do {
      *plVar12 = *plVar14;
      lVar16 = plVar14[1];
      plVar12[1] = lVar16;
      if (lVar16 != 0) {
        FUN_00c538b0(1,lVar16 + 8);
      }
      plVar14 = plVar14 + 2;
      plVar12 = plVar12 + 2;
    } while (plVar14 != plVar18);
    plVar14 = (long *)*param_1;
    local_a0 = plVar12;
    for (plVar18 = (long *)param_1[1]; plVar18 != plVar14; plVar18 = plVar18 + -2) {
      plVar12 = (long *)plVar18[-1];
                    /* catch() { ... } // from try @ 009ad080 with catch @ 009ad048 */
      if ((plVar12 != (long *)0x0) &&
         (lVar16 = FUN_00c538e0(0xffffffffffffffff,plVar12 + 1), lVar16 == 0)) {
        (**(code **)(*plVar12 + 0x10))(plVar12);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
      }
      puVar11 = local_90;
    }
  }
  puVar5 = local_88;
  param_1[1] = plVar14;
  plVar14 = local_a8;
  plVar18 = local_a0;
                    /* try { // try from 009ad078 to 00aad07f has its CatchHandler @ 009ad0cc */
  for (; local_a8 = plVar14, local_a0 = plVar18, puVar11 != puVar5; puVar11 = puVar11 + 1) {
    if (plVar14 != plVar18) {
      uVar10 = *puVar11;
      do {
        pplVar2 = (long **)*plVar14;
        local_70 = (long *)plVar14[1];
                    /* catch() { ... } // from try @ 009ad078 with catch @ 009ad0cc */
        local_78 = pplVar2;
        if (local_70 != (long *)0x0) {
          FUN_00c538b0(1,local_70 + 1);
        }
        iVar8 = FUN_009b3fb8(pplVar2);
        if ((int)uVar10 == iVar8) {
          uVar9 = FUN_009b5af8(local_78);
          uVar13 = FUN_008065d4(4,uVar9);
          if ((uVar13 & 1) != 0) {
            plVar14 = (long *)param_1[1];
            if (plVar14 < (long *)param_1[2]) {
              *plVar14 = (long)local_78;
              plVar14[1] = (long)local_70;
              if (local_70 != (long *)0x0) {
                FUN_00c538b0(1,local_70 + 1);
              }
              plVar14 = plVar14 + 2;
            }
            else {
              plVar14 = (long *)FUN_009b0a4c(param_1,&local_78);
            }
            plVar18 = local_70;
            param_1[1] = plVar14;
                    /* catch() { ... } // from try @ 009ad1c8 with catch @ 009ad184 */
            if ((local_70 != (long *)0x0) &&
               (lVar16 = FUN_00c538e0(0xffffffffffffffff,local_70 + 1), lVar16 == 0)) {
              (**(code **)(*plVar18 + 0x10))(plVar18);
              _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
            }
            break;
          }
        }
        plVar12 = local_70;
        if ((local_70 != (long *)0x0) &&
           (lVar16 = FUN_00c538e0(0xffffffffffffffff,local_70 + 1), lVar16 == 0)) {
          (**(code **)(*plVar12 + 0x10))(plVar12);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
        }
        plVar14 = plVar14 + 2;
      } while (plVar14 != plVar18);
    }
    plVar14 = local_a8;
    plVar18 = local_a0;
  }
                    /* try { // try from 009ad080 to 00aad11b has its CatchHandler @ 009ad048 */
  if (plVar14 != (long *)0x0) {
    for (; plVar18 != plVar14; plVar18 = plVar18 + -2) {
                    /* try { // try from 009ad1c0 to 00aad1c7 has its CatchHandler @ 009ad214 */
      plVar12 = (long *)plVar18[-1];
                    /* try { // try from 009ad1c8 to 00aad263 has its CatchHandler @ 009ad184 */
      if ((plVar12 != (long *)0x0) &&
         (lVar16 = FUN_00c538e0(0xffffffffffffffff,plVar12 + 1), lVar16 == 0)) {
        (**(code **)(*plVar12 + 0x10))(plVar12);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
      }
    }
    local_a0 = plVar14;
    _ZdlPv(local_a8);
  }
  if (local_90 != (ulong *)0x0) {
    _ZdlPv(local_90);
  }
                    /* catch() { ... } // from try @ 009ad1c0 with catch @ 009ad214 */
  if (*(long *)(lVar4 + 0x28) == local_68) {
    return;
  }
LAB_009ad304:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
