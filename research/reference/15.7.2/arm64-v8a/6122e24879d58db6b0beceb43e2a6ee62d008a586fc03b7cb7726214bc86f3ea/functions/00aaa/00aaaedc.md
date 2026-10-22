# 00aaaedc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aaaedc.md)

## 関数情報

~~~json
{
  "address": "00aaaedc",
  "name": "FUN_00aaaedc",
  "size": 1200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f18e8c4678031eece74ff60703a23d0d87f7e963adbe50e262bfc84c94b6ca76",
  "source_text_sha256": "f18e8c4678031eece74ff60703a23d0d87f7e963adbe50e262bfc84c94b6ca76"
}
~~~
## 呼び出し元

- [005d996c](../005d9/005d996c.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0041e380](../0041e/0041e380.md)
- [007cf950](../007cf/007cf950.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [0081f580](../0081f/0081f580.md)
- [00aaca78](../00aac/00aaca78.md)
- [00aaca8c](../00aac/00aaca8c.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)

## 疑似コード 1/1 / UTF-8 7943 bytes

~~~c

void FUN_00aaaedc(long param_1,int param_2,int param_3,int param_4)

{
  ulong uVar1;
  byte *pbVar2;
  undefined4 uVar3;
  byte bVar4;
  byte bVar5;
  byte bVar6;
  byte bVar7;
  byte bVar8;
  byte bVar9;
  byte bVar10;
  byte bVar11;
  int iVar12;
  int iVar13;
  long lVar14;
  undefined8 *puVar15;
  undefined8 uVar16;
  long lVar17;
  undefined8 *puVar18;
  void *__dest;
  undefined8 *puVar19;
  long *plVar20;
  ulong uVar21;
  undefined8 *puVar22;
  ulong uVar23;
  undefined8 *puVar24;
  void *__src;
  long lVar25;
  long lVar26;
  void *local_80;
  void *local_78;
  undefined8 local_70;
  long local_68;
  
  lVar14 = tpidr_el0;
  local_68 = *(long *)(lVar14 + 0x28);
  if (param_2 == -1) {
    param_2 = FUN_007cf950(0);
    param_3 = FUN_007cfaa0();
    param_4 = FUN_007cfcd8();
  }
  iVar12 = param_4 + param_3 * 10 + param_2 * 1000;
  puVar22 = (undefined8 *)(param_1 + 0x20);
  puVar19 = (undefined8 *)*puVar22;
  puVar18 = puVar22;
  puVar24 = puVar22;
  if ((undefined8 *)*puVar22 != (undefined8 *)0x0) {
    do {
      while (puVar15 = puVar19, puVar24 = puVar15, iVar12 < *(int *)(puVar15 + 4)) {
        puVar19 = (undefined8 *)*puVar15;
        puVar18 = puVar15;
        if ((undefined8 *)*puVar15 == (undefined8 *)0x0) goto LAB_00aaaf98;
      }
      if (iVar12 <= *(int *)(puVar15 + 4)) goto LAB_00aaafec;
      puVar19 = (undefined8 *)puVar15[1];
    } while ((undefined8 *)puVar15[1] != (undefined8 *)0x0);
    puVar18 = puVar15 + 1;
  }
LAB_00aaaf98:
  puVar15 = operator_new(0x40);
  puVar15[6] = 0;
  puVar15[7] = 0;
  puVar15[5] = 0;
  *puVar15 = 0;
  puVar15[1] = 0;
  puVar15[2] = puVar24;
  *puVar18 = puVar15;
  plVar20 = *(long **)(param_1 + 0x18);
  *(int *)(puVar15 + 4) = iVar12;
  puVar19 = puVar15;
  if (*plVar20 != 0) {
    *(long *)(param_1 + 0x18) = *plVar20;
    puVar19 = (undefined8 *)*puVar18;
  }
  FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar19);
  *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aaafec:
  if ((ulong)(((long)(puVar15[6] - puVar15[5]) >> 3) * -0x5555555555555555) < 10) {
    puVar19 = (undefined8 *)*puVar22;
    puVar18 = puVar22;
    puVar24 = puVar22;
    if ((undefined8 *)*puVar22 != (undefined8 *)0x0) {
      do {
        while (puVar15 = puVar19, puVar24 = puVar15, iVar12 < *(int *)(puVar15 + 4)) {
          puVar19 = (undefined8 *)*puVar15;
          puVar18 = puVar15;
          if ((undefined8 *)*puVar15 == (undefined8 *)0x0) goto LAB_00aab084;
        }
        if (iVar12 <= *(int *)(puVar15 + 4)) goto LAB_00aab0d8;
        puVar19 = (undefined8 *)puVar15[1];
      } while ((undefined8 *)puVar15[1] != (undefined8 *)0x0);
      puVar18 = puVar15 + 1;
    }
LAB_00aab084:
    puVar15 = operator_new(0x40);
    puVar15[6] = 0;
    puVar15[7] = 0;
    puVar15[5] = 0;
    *puVar15 = 0;
    puVar15[1] = 0;
    puVar15[2] = puVar24;
    *puVar18 = puVar15;
    plVar20 = *(long **)(param_1 + 0x18);
    *(int *)(puVar15 + 4) = iVar12;
    puVar19 = puVar15;
    if (*plVar20 != 0) {
      *(long *)(param_1 + 0x18) = *plVar20;
      puVar19 = (undefined8 *)*puVar18;
    }
    FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar19);
    *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aab0d8:
    puVar19 = (undefined8 *)puVar15[6];
    local_80 = (void *)0x0;
    local_78 = (void *)0x0;
    local_70 = 0;
    if (puVar19 < (undefined8 *)puVar15[7]) {
      *puVar19 = 0;
      puVar19[1] = 0;
      puVar19[2] = 0;
      puVar15[6] = puVar19 + 3;
    }
    else {
      uVar16 = FUN_00aaca8c(puVar15 + 5,&local_80);
      puVar15[6] = uVar16;
      if (local_80 != (void *)0x0) {
        local_78 = local_80;
        operator_delete(local_80);
      }
    }
    lVar26 = 0;
    while( true ) {
      lVar17 = FUN_0081f580();
      pbVar2 = (byte *)(lVar17 + 0xc744 + lVar26 * 4);
      if (((uint)(*(byte *)(lVar17 + 0xc76e) ^ pbVar2[2]) << 0x10 |
           (uint)(*(byte *)(lVar17 + 0xc76f) ^ pbVar2[3]) << 0x18 |
           (uint)(*(byte *)(lVar17 + 0xc76d) ^ pbVar2[1]) << 8 |
          (uint)(*(byte *)(lVar17 + 0xc76c) ^ *pbVar2)) == 0xffffffff) break;
      lVar17 = FUN_0081f580();
      pbVar2 = (byte *)(lVar17 + 0xc744 + lVar26 * 4);
      bVar4 = *(byte *)(lVar17 + 0xc76c);
      bVar5 = *(byte *)(lVar17 + 0xc76d);
      bVar6 = *pbVar2;
      bVar7 = pbVar2[1];
      bVar8 = pbVar2[2];
      bVar9 = *(byte *)(lVar17 + 0xc76e);
      bVar10 = pbVar2[3];
      bVar11 = *(byte *)(lVar17 + 0xc76f);
      puVar19 = (undefined8 *)*puVar22;
      puVar18 = puVar22;
      while (puVar15 = puVar18, puVar24 = puVar18, puVar19 != (undefined8 *)0x0) {
        while (puVar18 = puVar19, *(int *)(puVar18 + 4) <= iVar12) {
          if (iVar12 <= *(int *)(puVar18 + 4)) goto LAB_00aab280;
          puVar19 = (undefined8 *)puVar18[1];
          if ((undefined8 *)puVar18[1] == (undefined8 *)0x0) {
            puVar24 = puVar18 + 1;
            puVar15 = puVar18;
            goto LAB_00aab218;
          }
        }
        puVar19 = (undefined8 *)*puVar18;
      }
LAB_00aab218:
      puVar18 = operator_new(0x40);
      puVar18[2] = puVar15;
      puVar18[6] = 0;
      puVar18[7] = 0;
      puVar18[5] = 0;
      *puVar18 = 0;
      puVar18[1] = 0;
      *puVar24 = puVar18;
      plVar20 = *(long **)(param_1 + 0x18);
      *(int *)(puVar18 + 4) = iVar12;
      puVar19 = puVar18;
      if (*plVar20 != 0) {
        *(long *)(param_1 + 0x18) = *plVar20;
        puVar19 = (undefined8 *)*puVar24;
      }
      FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar19);
      *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aab280:
      lVar25 = puVar18[6];
      iVar13 = CONCAT13(bVar11 ^ bVar10,
                        CONCAT12(bVar9 ^ bVar8,CONCAT11(bVar5 ^ bVar7,bVar4 ^ bVar6))) + -2;
      lVar17 = FUN_0081f580();
      puVar19 = *(undefined8 **)(lVar25 + -0x10);
      uVar3 = *(undefined4 *)(lVar17 + (long)iVar13 * 4 + 0x49734);
      if (puVar19 < *(undefined8 **)(lVar25 + -8)) {
        puVar18 = puVar19 + 1;
        *puVar19 = CONCAT44(uVar3,iVar13);
      }
      else {
        __src = *(void **)(lVar25 + -0x18);
        lVar17 = (long)puVar19 - (long)__src >> 3;
        uVar1 = lVar17 + 1;
        if (uVar1 >> 0x3d != 0) {
          if (*(long *)(lVar14 + 0x28) == local_68) {
            FUN_00aaca78();
LAB_00aab370:
            if (*(long *)(lVar14 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_0041e380();
            }
          }
          goto LAB_00aab3bc;
        }
        uVar21 = (long)*(undefined8 **)(lVar25 + -8) - (long)__src;
        uVar23 = (long)uVar21 >> 2;
        if (uVar23 <= uVar1) {
          uVar23 = uVar1;
        }
        if (0x7ffffffffffffff7 < uVar21) {
          uVar23 = 0x1fffffffffffffff;
        }
        if (uVar23 == 0) {
          __dest = (void *)0x0;
        }
        else {
          if (uVar23 >> 0x3d != 0) goto LAB_00aab370;
          __dest = operator_new(uVar23 << 3);
        }
        puVar24 = (undefined8 *)((long)__dest + lVar17 * 8);
        puVar18 = puVar24 + 1;
        *puVar24 = CONCAT44(uVar3,iVar13);
        memcpy(__dest,__src,(long)puVar19 - (long)__src);
        *(void **)(lVar25 + -0x18) = __dest;
        *(undefined8 **)(lVar25 + -0x10) = puVar18;
        *(void **)(lVar25 + -8) = (void *)((long)__dest + uVar23 * 8);
        if (__src != (void *)0x0) {
          operator_delete(__src);
        }
      }
      lVar26 = lVar26 + 1;
      *(undefined8 **)(lVar25 + -0x10) = puVar18;
      if (lVar26 == 10) break;
    }
  }
  if (*(long *)(lVar14 + 0x28) == local_68) {
    return;
  }
LAB_00aab3bc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
