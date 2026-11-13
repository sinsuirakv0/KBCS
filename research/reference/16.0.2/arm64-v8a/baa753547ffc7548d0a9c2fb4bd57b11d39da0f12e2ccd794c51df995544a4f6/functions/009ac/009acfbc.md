# 009acfbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "009acfbc",
  "name": "FUN_009acfbc",
  "size": 1284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "958c25bc65b1be87ed8b26e49158c4c58632388420545f9d11638bfdfe1415fb",
  "source_text_sha256": "958c25bc65b1be87ed8b26e49158c4c58632388420545f9d11638bfdfe1415fb"
}
~~~

## 呼び出し元

- [0075ebd8](../0075e/0075ebd8.md)

## 呼び出し先

- [00440f00](../00440/00440f00.md)
- [006b8c9c](../006b8/006b8c9c.md)
- [0080666c](../00806/0080666c.md)
- [009b0c3c](../009b0/009b0c3c.md)
- [009b0d98](../009b0/009b0d98.md)
- [009b0dac](../009b0/009b0dac.md)
- [009b1e30](../009b1/009b1e30.md)
- [009b41a8](../009b4/009b41a8.md)
- [009b5ce8](../009b5/009b5ce8.md)
- [009b5cf8](../009b5/009b5cf8.md)
- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c53ffc](../00c53/00c53ffc.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)

## 疑似コード / UTF-8 8994 bytes

~~~c

void FUN_009acfbc(undefined8 *param_1)

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
  
                    /* catch() { ... } // from try @ 009ace88 with catch @ 009acfbc */
  lVar4 = tpidr_el0;
  local_68 = *(long *)(lVar4 + 0x28);
  puVar1 = (undefined8 *)*param_1;
  puVar3 = (undefined8 *)param_1[1];
  local_90 = (ulong *)0x0;
  local_88 = (ulong *)0x0;
  local_80 = (ulong *)0x0;
  puVar11 = local_90;
  for (; local_90 = puVar11, puVar1 != puVar3; puVar1 = puVar1 + 2) {
    plVar14 = (long *)*puVar1;
    plVar18 = (long *)puVar1[1];
    local_a8 = plVar14;
    local_a0 = plVar18;
    puVar5 = puVar11;
    puVar6 = local_88;
    if (plVar18 != (long *)0x0) {
      FUN_00c53d70(1,plVar18 + 1);
      puVar11 = local_90;
      puVar5 = local_90;
      puVar6 = local_88;
    }
    for (; puVar7 = local_88, __src = local_90, local_90 = puVar5, puVar11 != local_88;
        puVar11 = puVar11 + 1) {
      uVar10 = *puVar11;
      local_88 = puVar6;
      iVar8 = FUN_009b41a8(plVar14);
      puVar5 = local_88;
      if ((int)uVar10 == iVar8) goto joined_r0x009ad0a0;
      puVar5 = local_90;
      puVar6 = local_88;
      local_88 = puVar7;
      local_90 = __src;
    }
    local_88 = puVar6;
    iVar8 = FUN_009b5cf8(plVar14);
    puVar5 = local_88;
    if (iVar8 != 0) {
      uVar10 = FUN_009b41a8(plVar14);
      lVar16 = FUN_009b5ce8(plVar14);
      uVar10 = uVar10 & 0xffffffff | lVar16 << 0x20;
      if (puVar7 < local_80) {
        *puVar7 = uVar10;
        puVar5 = puVar7 + 1;
      }
      else {
        lVar16 = (long)puVar7 - (long)__src >> 3;
        uVar13 = lVar16 + 1;
        if (uVar13 >> 0x3d != 0) {
                    /* try { // try from 009ad43c to 00aad443 has its CatchHandler @ 009ad5c8 */
          if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* try { // try from 009ad444 to 00aad47f has its CatchHandler @ 009ad5f0 */
            FUN_006b8c9c(&local_90);
LAB_009ad44c:
            if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_00440f00();
            }
          }
          goto LAB_009ad4f4;
        }
                    /* catch() { ... } // from try @ 009ad11c with catch @ 009ad0e4 */
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
          if (uVar17 >> 0x3d != 0) goto LAB_009ad44c;
                    /* try { // try from 009ad114 to 00aad11b has its CatchHandler @ 009ad168 */
          puVar11 = (ulong *)_Znwm(uVar17 << 3);
                    /* try { // try from 009ad11c to 00aad1b7 has its CatchHandler @ 009ad0e4 */
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
joined_r0x009ad0a0:
    local_88 = puVar5;
    if ((plVar18 != (long *)0x0) &&
       (lVar16 = FUN_00c53da0(0xffffffffffffffff,plVar18 + 1), lVar16 == 0)) {
      (**(code **)(*plVar18 + 0x10))(plVar18);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
    }
    puVar11 = local_90;
  }
                    /* catch() { ... } // from try @ 009ad114 with catch @ 009ad168 */
  lVar16 = 0;
  if (local_88 != puVar11) {
    lVar16 = LZCOUNT((long)local_88 - (long)puVar11 >> 3) * -2 + 0x7e;
  }
  FUN_009b0dac(local_88,local_88,puVar11,puVar11,lVar16,1);
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
        uVar15 = FUN_009b0d98(&local_a8);
        FUN_009b1e30(&local_78);
        if (local_90 != (ulong *)0x0) {
          local_88 = local_90;
          _ZdlPv(local_90);
        }
                    /* try { // try from 009ad4e0 to 00aad6e3 has its CatchHandler @ 009ad368 */
        if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_00c53ffc(uVar15);
        }
      }
      goto LAB_009ad4f4;
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
        FUN_00c53d70(1,lVar16 + 8);
      }
      plVar14 = plVar14 + 2;
      plVar12 = plVar12 + 2;
    } while (plVar14 != plVar18);
    plVar14 = (long *)*param_1;
    local_a0 = plVar12;
    for (plVar18 = (long *)param_1[1]; plVar18 != plVar14; plVar18 = plVar18 + -2) {
      plVar12 = (long *)plVar18[-1];
      if ((plVar12 != (long *)0x0) &&
         (lVar16 = FUN_00c53da0(0xffffffffffffffff,plVar12 + 1), lVar16 == 0)) {
        (**(code **)(*plVar12 + 0x10))(plVar12);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
      }
                    /* catch() { ... } // from try @ 009ad264 with catch @ 009ad220 */
      puVar11 = local_90;
    }
  }
  puVar5 = local_88;
                    /* try { // try from 009ad264 to 00aad2ff has its CatchHandler @ 009ad220 */
  param_1[1] = plVar14;
  plVar14 = local_a8;
  plVar18 = local_a0;
  for (; local_a8 = plVar14, local_a0 = plVar18, puVar11 != puVar5; puVar11 = puVar11 + 1) {
    if (plVar14 != plVar18) {
      uVar10 = *puVar11;
      do {
        pplVar2 = (long **)*plVar14;
        local_70 = (long *)plVar14[1];
        local_78 = pplVar2;
        if (local_70 != (long *)0x0) {
          FUN_00c53d70(1,local_70 + 1);
        }
        iVar8 = FUN_009b41a8(pplVar2);
        if ((int)uVar10 == iVar8) {
          uVar9 = FUN_009b5ce8(local_78);
          uVar13 = FUN_0080666c(4,uVar9);
          if ((uVar13 & 1) != 0) {
            plVar14 = (long *)param_1[1];
            if (plVar14 < (long *)param_1[2]) {
              *plVar14 = (long)local_78;
              plVar14[1] = (long)local_70;
              if (local_70 != (long *)0x0) {
                FUN_00c53d70(1,local_70 + 1);
              }
              plVar14 = plVar14 + 2;
            }
            else {
                    /* try { // try from 009ad368 to 00aad3ef has its CatchHandler @ 009ad368
                       catch() { ... } // from try @ 009ad368 with catch @ 009ad368
                       catch() { ... } // from try @ 009ad4e0 with catch @ 009ad368 */
              plVar14 = (long *)FUN_009b0c3c(param_1,&local_78);
            }
            plVar18 = local_70;
            param_1[1] = plVar14;
            if ((local_70 != (long *)0x0) &&
               (lVar16 = FUN_00c53da0(0xffffffffffffffff,local_70 + 1), lVar16 == 0)) {
              (**(code **)(*plVar18 + 0x10))(plVar18);
              _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
            }
            break;
          }
        }
        plVar12 = local_70;
        if ((local_70 != (long *)0x0) &&
           (lVar16 = FUN_00c53da0(0xffffffffffffffff,local_70 + 1), lVar16 == 0)) {
          (**(code **)(*plVar12 + 0x10))(plVar12);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
        }
        plVar14 = plVar14 + 2;
                    /* catch() { ... } // from try @ 009ad25c with catch @ 009ad2b0 */
      } while (plVar14 != plVar18);
    }
    plVar14 = local_a8;
    plVar18 = local_a0;
  }
  if (plVar14 != (long *)0x0) {
    for (; plVar18 != plVar14; plVar18 = plVar18 + -2) {
      plVar12 = (long *)plVar18[-1];
      if ((plVar12 != (long *)0x0) &&
         (lVar16 = FUN_00c53da0(0xffffffffffffffff,plVar12 + 1), lVar16 == 0)) {
        (**(code **)(*plVar12 + 0x10))(plVar12);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
      }
    }
    local_a0 = plVar14;
    _ZdlPv(local_a8);
  }
                    /* try { // try from 009ad3f0 to 00aad3fb has its CatchHandler @ 009ad5e0 */
  if (local_90 != (ulong *)0x0) {
    _ZdlPv(local_90);
  }
  if (*(long *)(lVar4 + 0x28) == local_68) {
    return;
  }
LAB_009ad4f4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
