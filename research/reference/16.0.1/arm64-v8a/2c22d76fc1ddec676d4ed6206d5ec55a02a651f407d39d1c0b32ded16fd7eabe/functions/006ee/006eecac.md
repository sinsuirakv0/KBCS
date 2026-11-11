# 006eecac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "006eecac",
  "name": "FUN_006eecac",
  "size": 2576,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "39438aea37c29e8c162321dea51e09a2c2b1f25622ee9621082006ae90ef8578",
  "source_text_sha256": "39438aea37c29e8c162321dea51e09a2c2b1f25622ee9621082006ae90ef8578"
}
~~~

## 呼び出し元

- [006f24d4](../006f2/006f24d4.md)

## 呼び出し先

- [00442930](../00442/00442930.md)
- [0046d7b0](../0046d/0046d7b0.md)
- [006dbda8](../006db/006dbda8.md)
- [006e43e8](../006e4/006e43e8.md)
- [006e4ac4](../006e4/006e4ac4.md)
- [006e53d4](../006e5/006e53d4.md)
- [006ecb24](../006ec/006ecb24.md)
- [006ee740](../006ee/006ee740.md)
- [006eea84](../006ee/006eea84.md)
- [0071bed8](../0071b/0071bed8.md)
- [0071d1fc](../0071d/0071d1fc.md)
- [008514f8](../00851/008514f8.md)
- [008783f0](../00878/008783f0.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58090](../00c58/00c58090.md)
- [00c5a830](../00c5a/00c5a830.md)
- [00c5a840](../00c5a/00c5a840.md)

## 関連文字列（未確認候補）

~~~text
"GamattType"
"map::at:  key not found"
"sec2_id"
"sec2_type"
~~~

## 疑似コード / UTF-8 14431 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

undefined4 FUN_006eecac(long param_1)

{
  void *__s;
  int iVar1;
  long lVar2;
  bool bVar3;
  int iVar4;
  uint uVar5;
  int iVar6;
  long lVar7;
  undefined8 uVar8;
  void *__ptr;
  long lVar9;
  undefined8 uVar10;
  ulong uVar11;
  long *plVar12;
  int *piVar13;
  int *piVar14;
  ulong uVar15;
  undefined4 uVar16;
  int iVar17;
  int iVar18;
  int iVar19;
  float fVar20;
  undefined4 local_c8 [2];
  char *local_c0;
  char *local_b0;
  undefined4 uStack_a8;
  undefined4 uStack_a4;
  undefined8 local_a0;
  char *local_90;
  undefined4 local_88 [2];
  undefined8 local_80;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  lVar7 = FUN_008514f8();
  iVar4 = *(int *)((long)&DWORD_004362fc + lVar7);
  lVar7 = FUN_008514f8();
  if (iVar4 == 5) {
    *(undefined4 *)((long)&DWORD_004362fc + lVar7) = 6;
  }
  else if (*(int *)((long)&DWORD_004362fc + lVar7) == 3) {
    lVar7 = FUN_008514f8();
    *(undefined4 *)((long)&DWORD_004362fc + lVar7) = 4;
  }
  *(undefined4 *)(param_1 + 0x738) = 0;
  *(undefined4 *)(param_1 + 0x1fa0) = 0;
  lVar7 = FUN_008514f8();
  __s = (void *)(param_1 + 0x3914);
  BYTE_ARRAY_00436ad5[lVar7 + 0x1f] = 0;
  *(undefined4 *)(param_1 + 0x3910) = 0;
  memset(__s,0xff,0x800);
  *(undefined8 *)(param_1 + 0x4134) = 0;
  *(undefined8 *)(param_1 + 0x411c) = 0;
  *(undefined8 *)(param_1 + 0x4114) = 0;
  *(undefined8 *)(param_1 + 0x412c) = 0;
  *(undefined8 *)(param_1 + 0x4124) = 0;
  uVar8 = FUN_0046d7b0(10000);
  iVar4 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),0);
  uVar16 = 1;
  if (iVar4 <= (int)uVar8) {
    iVar4 = *(int *)(param_1 + 0x1f9c);
    lVar7 = FUN_008514f8();
    uVar16 = 1;
    if (iVar4 < *(int *)((long)&fde_00436d88 + lVar7) + -1) {
      uVar16 = 2;
    }
  }
  *(undefined4 *)(param_1 + 0x3910) = uVar16;
  uVar16 = *(undefined4 *)(&DAT_00ca3ed0 + (long)*(int *)(param_1 + 0x1f8c) * 4);
  *(undefined8 *)(param_1 + 0x57d8) = *(undefined8 *)(param_1 + 0x57d0);
  FUN_006dbda8(&local_b0,param_1 + 0x5790,*(undefined4 *)(param_1 + 0x1f88),uVar16);
  __ptr = *(void **)(param_1 + 0x57d0);
  if (__ptr != (void *)0x0) {
    *(void **)(param_1 + 0x57d8) = __ptr;
    _ZdlPv(__ptr);
    *(undefined8 *)(param_1 + 0x57d0) = 0;
    *(undefined8 *)(param_1 + 0x57d8) = 0;
    *(undefined8 *)(param_1 + 0x57e0) = 0;
  }
  *(ulong *)(param_1 + 0x57d8) = CONCAT44(uStack_a4,uStack_a8);
  *(char **)(param_1 + 0x57d0) = local_b0;
  *(undefined8 *)(param_1 + 0x57e0) = local_a0;
  if (*(int *)(param_1 + 0x1f94) < 1) {
LAB_006ef1c8:
    uVar8 = FUN_006e4ac4();
    uVar16 = *(undefined4 *)(param_1 + 0x1f88);
    *(int *)((long)__s + (long)*(int *)(param_1 + 0x1f94) * 8 + -8) = (int)uVar8;
    uVar8 = FUN_006e4ac4(uVar8,uVar16,10);
    uVar10 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),0xb);
    iVar4 = FUN_006e4ac4(uVar10,*(undefined4 *)(param_1 + 0x1f88),10);
    iVar4 = FUN_0046d7b0(((int)uVar10 - iVar4) + 1);
    lVar7 = (long)*(int *)(param_1 + 0x1f94) + -1;
    *(int *)((long)__s + lVar7 * 8 + 4) = iVar4 + (int)uVar8;
    iVar4 = *(int *)(param_1 + 0x56f0);
    if ((iVar4 != -1) && (*(int *)((long)__s + lVar7 * 8) != 0x16)) {
      for (plVar12 = *(long **)(param_1 + 0x56c8); plVar12 != (long *)0x0;
          plVar12 = (long *)plVar12[1]) {
        while (iVar4 < (int)plVar12[4]) {
                    /* try { // try from 006ef5ac to 007efbd7 has its CatchHandler @ 006ef5ac
                       catch() { ... } // from try @ 006ef5ac with catch @ 006ef5ac
                       catch() { ... } // from try @ 006efbe4 with catch @ 006ef5ac */
          plVar12 = (long *)*plVar12;
          if (plVar12 == (long *)0x0) goto LAB_006ef5d0;
        }
        if (iVar4 <= (int)plVar12[4]) goto LAB_006ef268;
      }
LAB_006ef5d0:
      if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
        FUN_00442930("map::at:  key not found");
      }
      goto LAB_006ef740;
    }
    lVar7 = FUN_008514f8();
    if (*(int *)((long)&DWORD_004362fc + lVar7) != 4) {
      FUN_008514f8();
    }
LAB_006ef268:
    uVar16 = *(undefined4 *)((long)__s + (long)*(int *)(param_1 + 0x1f94) * 8 + -8);
    iVar4 = FUN_0071bed8(uVar16);
    uVar8 = FUN_0071d1fc(uVar16,*(int *)((long)__s + (long)*(int *)(param_1 + 0x1f94) * 8 + -4) +
                                iVar4,0);
    iVar4 = *(int *)(param_1 + 0x1f94);
    uVar11 = (ulong)iVar4;
    if (*(int *)((long)__s + uVar11 * 8 + -8) != 0x16) {
      uVar16 = 0;
      goto joined_r0x006ef1c0;
    }
    local_b0 = "sec2_type";
    uStack_a8 = 0;
    local_a0 = 0;
    local_c8[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_c8,4);
    local_c0 = "GamattType";
    _ZN8firebase7VariantaSEOS0_(&uStack_a8,local_c8);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_c8,0);
    local_90 = "sec2_id";
    local_88[0] = 0;
    local_80 = 0;
    local_c8[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_c8,1);
    local_c0 = (char *)0x1;
    _ZN8firebase7VariantaSEOS0_(local_88,local_c8);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_c8,0);
    lVar7 = FUN_008514f8();
                    /* try { // try from 006ef348 to 007ef353 has its CatchHandler @ 006ef580 */
                    /* try { // try from 006ef354 to 007ef5ab has its CatchHandler @ 006ee5d0 */
    FUN_008783f0(*(undefined8 *)(lVar7 + 0x22b0),0x98c17d,
                 *(undefined4 *)((long)__s + (long)*(int *)(param_1 + 0x1f94) * 8 + -4),0,&local_b0,
                 2);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_88,0);
    uVar8 = _ZN8firebase7Variant5ClearENS0_4TypeE(&uStack_a8,0);
    uVar11 = (ulong)*(uint *)(param_1 + 0x1f94);
    uVar16 = 0;
    if (0 < (int)*(uint *)(param_1 + 0x1f94)) goto LAB_006ef4bc;
LAB_006ef39c:
    iVar4 = 0;
    iVar6 = 0;
    iVar18 = 0;
    iVar19 = 0;
    iVar17 = 0;
  }
  else {
    lVar7 = 0;
    bVar3 = false;
    do {
      uVar8 = FUN_0046d7b0(10000);
      iVar4 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),7);
      uVar5 = FUN_006e43e8();
      FUN_008514f8();
      if (uVar5 < 0x47) {
        lVar9 = FUN_008514f8();
        iVar6 = *(int *)(BYTE_ARRAY_0043addd + lVar9 + (ulong)uVar5 * 4 + 0x17);
      }
      else {
        iVar6 = 0;
      }
      if ((int)uVar8 < iVar6 + iVar4) {
        uVar8 = FUN_006eea84(param_1);
        if ((int)uVar8 == -1) goto LAB_006ef178;
        iVar4 = (int)uVar8 * 6;
        uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),iVar4 + 9);
        piVar14 = (int *)((long)__s + lVar7 * 8);
        uVar16 = *(undefined4 *)(param_1 + 0x1f88);
        *piVar14 = (int)uVar8;
        uVar8 = FUN_006e4ac4(uVar8,uVar16,iVar4 + 10);
        uVar10 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),iVar4 + 0xb);
        iVar6 = FUN_006e4ac4(uVar10,*(undefined4 *)(param_1 + 0x1f88),iVar4 + 10);
        uVar10 = FUN_0046d7b0(((int)uVar10 - iVar6) + 1);
        uVar16 = *(undefined4 *)(param_1 + 0x1f88);
        piVar14[1] = (int)uVar10 + (int)uVar8;
        uVar8 = FUN_006e4ac4(uVar10,uVar16,iVar4 + 0xd);
        if ((int)uVar8 == 0) {
LAB_006eef90:
          iVar4 = piVar14[1];
          iVar6 = *(int *)(param_1 + 0x56f0);
          if ((iVar6 == -1) || (iVar18 = *piVar14, iVar18 == 0x16)) {
            lVar9 = FUN_008514f8();
            if ((*(int *)((long)&DWORD_004362fc + lVar9) != 4) &&
               (lVar9 = FUN_008514f8(), *(int *)((long)&DWORD_004362fc + lVar9) != 6)) {
              iVar18 = *piVar14;
              goto LAB_006ef04c;
            }
            iVar18 = *piVar14;
            if (iVar18 != 0x16) {
              fVar20 = *(float *)(param_1 + 0x1d68);
              goto LAB_006ef03c;
            }
LAB_006ef088:
            iVar6 = FUN_0071bed8(iVar18);
            FUN_0071d1fc(iVar18,iVar6 + iVar4,0);
            if (*piVar14 == 0x16) {
              uStack_a8 = 0;
              local_b0 = "sec2_type";
              local_a0 = 0;
              local_c8[0] = 0;
              _ZN8firebase7Variant5ClearENS0_4TypeE(local_c8,4);
              local_c0 = "GamattType";
              _ZN8firebase7VariantaSEOS0_(&uStack_a8,local_c8);
              _ZN8firebase7Variant5ClearENS0_4TypeE(local_c8,0);
              local_88[0] = 0;
              local_90 = "sec2_id";
              local_80 = 0;
              local_c8[0] = 0;
              _ZN8firebase7Variant5ClearENS0_4TypeE(local_c8,1);
              local_c0 = (char *)0x1;
              _ZN8firebase7VariantaSEOS0_(local_88,local_c8);
              _ZN8firebase7Variant5ClearENS0_4TypeE(local_c8,0);
              lVar9 = FUN_008514f8();
              FUN_008783f0(*(undefined8 *)(lVar9 + 0x22b0),0x98c17d,iVar4,0,&local_b0,2);
              _ZN8firebase7Variant5ClearENS0_4TypeE(local_88,0);
              _ZN8firebase7Variant5ClearENS0_4TypeE(&uStack_a8,0);
            }
          }
          else {
            plVar12 = *(long **)(param_1 + 0x56c8);
            while( true ) {
              while( true ) {
                if (plVar12 == (long *)0x0) goto LAB_006ef5d0;
                if (*(int *)(plVar12 + 4) <= iVar6) break;
                plVar12 = (long *)*plVar12;
              }
              if (iVar6 <= *(int *)(plVar12 + 4)) break;
              plVar12 = (long *)plVar12[1];
            }
            fVar20 = *(float *)(plVar12 + 0x12);
LAB_006ef03c:
            iVar4 = (int)(fVar20 * (float)iVar4);
LAB_006ef04c:
            if (8 < iVar18 - 10U) goto LAB_006ef088;
            iVar6 = FUN_0071bed8(6);
            FUN_0071d1fc(6,iVar6 + *(int *)(&DAT_00ca3ec0 + (long)*piVar14 * 4) * iVar4,0);
          }
          bVar3 = true;
          goto LAB_006ef178;
        }
        uVar11 = (ulong)*(uint *)(param_1 + 0x1f94);
        if ((int)*(uint *)(param_1 + 0x1f94) < 1) {
          iVar6 = 0;
        }
        else {
          iVar6 = 0;
          piVar13 = (int *)(param_1 + 0x3918);
          do {
            if (piVar13[-1] == *piVar14) {
              iVar6 = *piVar13 + iVar6;
            }
            uVar11 = uVar11 - 1;
            piVar13 = piVar13 + 2;
          } while (uVar11 != 0);
        }
        uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),iVar4 + 0xd);
        if (iVar6 <= (int)uVar8) goto LAB_006eef90;
        uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),iVar4 + 0xd);
        iVar4 = (piVar14[1] - iVar6) + (int)uVar8;
        piVar14[1] = iVar4;
        if (0 < iVar4) goto LAB_006eef90;
        *piVar14 = -1;
      }
      else {
LAB_006ef178:
        uVar8 = FUN_0046d7b0(*(int *)(&DAT_00ca3ed0 + (long)*(int *)(param_1 + 0x1f8c) * 4) * 0x3c);
        *(int *)(param_1 + 0x413c + lVar7 * 4) = (int)uVar8 + 1;
      }
      iVar4 = *(int *)(param_1 + 0x1f94);
      uVar11 = (ulong)iVar4;
      lVar7 = lVar7 + 1;
    } while (lVar7 < (long)uVar11);
    if (!bVar3) goto LAB_006ef1c8;
    uVar16 = 1;
joined_r0x006ef1c0:
    if (iVar4 < 1) goto LAB_006ef39c;
LAB_006ef4bc:
    iVar4 = 0;
    iVar6 = 0;
    iVar18 = 0;
    iVar19 = 0;
    iVar17 = 0;
    lVar7 = 0;
    piVar14 = (int *)(param_1 + 0x3918);
    do {
      iVar1 = piVar14[-1];
      if (iVar1 != -1) {
        uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),9);
        if (iVar1 == (int)uVar8) {
          iVar4 = iVar4 + *piVar14;
        }
        iVar1 = piVar14[-1];
        uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),0xf);
        if (iVar1 == (int)uVar8) {
          iVar6 = iVar6 + *piVar14;
        }
        iVar1 = piVar14[-1];
        uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),0x15);
        if (iVar1 == (int)uVar8) {
          iVar18 = iVar18 + *piVar14;
        }
        iVar1 = piVar14[-1];
        uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),0x1b);
        if (iVar1 == (int)uVar8) {
          iVar19 = iVar19 + *piVar14;
        }
                    /* catch() { ... } // from try @ 006ef348 with catch @ 006ef580 */
        iVar1 = piVar14[-1];
        uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),0x21);
        if (iVar1 == (int)uVar8) {
          iVar17 = iVar17 + *piVar14;
        }
        uVar11 = (ulong)*(uint *)(param_1 + 0x1f94);
      }
      lVar7 = lVar7 + 1;
      piVar14 = piVar14 + 2;
    } while (lVar7 < (int)uVar11);
  }
  uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),9);
  *(int *)(param_1 + 0x4114) = (int)uVar8;
  *(int *)(param_1 + 0x4118) = iVar4;
  uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),0xf);
  *(int *)(param_1 + 0x411c) = (int)uVar8;
  *(int *)(param_1 + 0x4120) = iVar6;
  uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),0x15);
  *(int *)(param_1 + 0x4124) = (int)uVar8;
  *(int *)(param_1 + 0x4128) = iVar18;
  uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),0x1b);
  *(int *)(param_1 + 0x412c) = (int)uVar8;
  *(int *)(param_1 + 0x4130) = iVar19;
  uVar8 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),0x21);
  uVar11 = 0;
  *(int *)(param_1 + 0x4134) = (int)uVar8;
  *(int *)(param_1 + 0x4138) = iVar17;
  do {
    uVar15 = 0xff;
    piVar14 = (int *)(param_1 + 0x4538);
    do {
      iVar4 = *piVar14;
      if ((iVar4 != 0) && (iVar6 = piVar14[-1], iVar4 < iVar6)) {
        piVar14[-1] = iVar4;
        *piVar14 = iVar6;
      }
      uVar15 = uVar15 - 1;
      piVar14 = piVar14 + -1;
    } while (uVar11 < uVar15);
    uVar11 = uVar11 + 1;
  } while (uVar11 != 0xff);
  iVar4 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),4);
  if (*(int *)(param_1 + 0x3910) == 2) {
    iVar4 = (iVar4 * 0x96) / 100;
  }
  if (iVar4 != 0) {
    if (*(int *)(param_1 + 0x1f8c) == 2) {
      iVar6 = 0x226;
    }
    else {
      if (*(int *)(param_1 + 0x1f8c) != 1) goto LAB_006ef610;
      iVar6 = 0x113;
    }
    iVar4 = (iVar4 * iVar6) / 100;
  }
LAB_006ef610:
  FUN_006ecb24(param_1,iVar4);
  FUN_006e53d4(param_1);
  if (0 < *(int *)(&DAT_00ca3edc + (long)*(int *)(param_1 + 0x1f8c) * 4)) {
    iVar4 = 0;
    do {
      uVar8 = FUN_0046d7b0(10000);
      iVar6 = FUN_006e4ac4(uVar8,*(undefined4 *)(param_1 + 0x1f88),1);
      if (((int)uVar8 < iVar6) && (uVar11 = FUN_006ee740(param_1), (uVar11 & 1) != 0)) break;
      iVar4 = iVar4 + 1;
    } while (iVar4 < *(int *)(&DAT_00ca3edc + (long)*(int *)(param_1 + 0x1f8c) * 4));
  }
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return uVar16;
  }
LAB_006ef740:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
