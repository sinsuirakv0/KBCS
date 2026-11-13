# 00aa0fec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aa0fec",
  "name": "FUN_00aa0fec",
  "size": 944,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "80c426338596e1a878d66d5bcdc41229a940cef461b2a678626597a51f97a15d",
  "source_text_sha256": "80c426338596e1a878d66d5bcdc41229a940cef461b2a678626597a51f97a15d"
}
~~~

## 呼び出し元

- [00a9f6cc](../00a9f/00a9f6cc.md)

## 呼び出し先

- [00470880](../00470/00470880.md)
- [00615f20](../00615/00615f20.md)
- [00674764](../00674/00674764.md)
- [00675b80](../00675/00675b80.md)
- [008003d0](../00800/008003d0.md)
- [00800684](../00800/00800684.md)
- [00851550](../00851/00851550.md)
- [00a65e5c](../00a65/00a65e5c.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)

## 疑似コード / UTF-8 7281 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00aa0fec(undefined8 *param_1,long param_2)

{
  void *pvVar1;
  size_t sVar2;
  long lVar3;
  void *__ptr;
  void *pvVar4;
  long *plVar5;
  bool bVar6;
  undefined4 uVar7;
  undefined4 uVar8;
  int iVar9;
  long lVar10;
  void *__dest;
  void *pvVar11;
  void *pvVar12;
  undefined8 *puVar13;
  long *plVar14;
  long *plVar15;
  void *local_a0;
  void *local_98;
  long local_90;
  undefined4 local_88;
  undefined4 uStack_84;
  void *local_80;
  void *local_78;
  void *local_70;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  lVar10 = FUN_00851550();
  uVar7 = FUN_00675b80(lVar10 + 0x1438);
  FUN_00674764(&local_88,lVar10 + 0x1438,uVar7);
  pvVar4 = local_80;
  __ptr = (void *)CONCAT44(uStack_84,local_88);
  if (__ptr != (void *)0x0) {
    local_80 = __ptr;
    _ZdlPv(__ptr);
  }
  plVar14 = *(long **)(param_2 + 0x18);
  do {
    if (plVar14 == (long *)(param_2 + 0x20)) {
      if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00a9d0fc with catch @ 00aa1328 */
                    /* catch() { ... } // from try @ 00a9cde8 with catch @ 00aa1340 */
        return;
      }
LAB_00aa1458:
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    pvVar11 = (void *)plVar14[5];
    pvVar12 = (void *)plVar14[6];
    local_88 = (undefined4)plVar14[4];
    local_78 = (void *)0x0;
    local_70 = (void *)0x0;
    sVar2 = (long)pvVar12 - (long)pvVar11;
    local_80 = (void *)0x0;
    if (sVar2 == 0) {
      pvVar11 = (void *)0x0;
      __dest = (void *)0x0;
      if (_DAT_00000020 != 5) goto LAB_00aa12d4;
LAB_00aa1130:
      uVar7 = FUN_008003d0(*(int *)((long)pvVar11 + 0x54) / 100);
      uVar8 = FUN_00800684(*(int *)((long)pvVar11 + 0x54) / 100);
      iVar9 = FUN_00a65e5c(uVar7,uVar8,*(int *)((long)pvVar11 + 0x54) % 100,0,0);
      _ZdlPv(pvVar11);
      pvVar11 = local_80;
      if (iVar9 == 0) {
        local_a0 = (void *)0x0;
        local_98 = (void *)0x0;
        local_90 = 0;
        sVar2 = (long)local_78 - (long)local_80;
        if (sVar2 == 0) {
          pvVar12 = (void *)0x0;
        }
        else {
          if ((long)sVar2 < 0) {
                    /* catch() { ... } // from try @ 00a9cd1c with catch @ 00aa1360 */
                    /* catch() { ... } // from try @ 00a9fc44 with catch @ 00aa1364 */
                    /* catch() { ... } // from try @ 00a9d37c with catch @ 00aa1368 */
                    /* catch() { ... } // from try @ 00aa01e0 with catch @ 00aa136c */
                    /* catch() { ... } // from try @ 00aa0024 with catch @ 00aa1370 */
            if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00aa0fbc with catch @ 00aa1374 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00aa0ab0 with catch @ 00aa1378 */
              FUN_00470880(&local_a0);
            }
            goto LAB_00aa1458;
          }
          pvVar12 = (void *)_Znwm(sVar2);
          local_90 = (long)pvVar12 + sVar2;
          local_a0 = pvVar12;
          memcpy(pvVar12,pvVar11,sVar2);
        }
                    /* try { // try from 00aa11f0 to 00ba1303 has its CatchHandler @ 00aa13a0 */
        uVar7 = FUN_008003d0(*(int *)((long)pvVar12 + 0x50) / 100);
        uVar8 = FUN_00800684(*(int *)((long)pvVar12 + 0x50) / 100);
        iVar9 = FUN_00a65e5c(uVar7,uVar8,*(int *)((long)pvVar12 + 0x50) % 100,0,0);
        local_98 = pvVar12;
        _ZdlPv(pvVar12);
        pvVar11 = local_80;
        if ((__ptr != pvVar4) && (iVar9 != 0)) {
          puVar13 = (undefined8 *)param_1[1];
          if (puVar13 < (undefined8 *)param_1[2]) {
            *puVar13 = 0;
            puVar13[1] = 0;
            puVar13[2] = 0;
            sVar2 = (long)local_78 - (long)local_80;
            if (sVar2 != 0) {
              if ((long)sVar2 < 0) {
                    /* catch() { ... } // from try @ 00a9d460 with catch @ 00aa137c */
                    /* catch() { ... } // from try @ 00a9cedc with catch @ 00aa1380 */
                    /* catch() { ... } // from try @ 00aa0d84 with catch @ 00aa138c */
                if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00a9ea34 with catch @ 00aa1390 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00aa095c with catch @ 00aa1394
                       catch() { ... } // from try @ 00aa0b14 with catch @ 00aa1394 */
                  FUN_00470880(puVar13);
                }
                goto LAB_00aa1458;
              }
              pvVar12 = (void *)_Znwm(sVar2);
              *puVar13 = pvVar12;
              puVar13[1] = pvVar12;
              puVar13[2] = (long)pvVar12 + sVar2;
              memcpy(pvVar12,pvVar11,sVar2);
              puVar13[1] = (long)pvVar12 + sVar2;
            }
            puVar13 = puVar13 + 3;
          }
          else {
            puVar13 = (undefined8 *)FUN_00615f20(param_1,&local_80);
          }
          param_1[1] = puVar13;
        }
      }
      __dest = local_80;
      if (local_80 != (void *)0x0) goto LAB_00aa12d4;
    }
    else {
      if ((long)sVar2 < 0) {
                    /* catch() { ... } // from try @ 00a9d134 with catch @ 00aa1344 */
                    /* catch() { ... } // from try @ 00a9d0cc with catch @ 00aa1348 */
                    /* catch() { ... } // from try @ 00a9cdb8 with catch @ 00aa134c */
                    /* catch() { ... } // from try @ 00a9da34 with catch @ 00aa1350 */
                    /* catch() { ... } // from try @ 00a9d278 with catch @ 00aa1354 */
        if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00a9d3b4 with catch @ 00aa1358 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00a9d5b4 with catch @ 00aa135c */
          FUN_00470880(&local_80);
        }
        goto LAB_00aa1458;
      }
      __dest = (void *)_Znwm(sVar2);
      pvVar1 = (void *)((long)__dest + sVar2);
      local_80 = __dest;
      local_78 = __dest;
      local_70 = pvVar1;
      memcpy(__dest,pvVar11,sVar2);
      if (*(int *)((long)__dest + 0x20) == 5) {
        local_78 = pvVar1;
        if (pvVar12 == pvVar11) {
          pvVar11 = (void *)0x0;
        }
        else {
          pvVar11 = (void *)_Znwm(sVar2);
          memcpy(pvVar11,__dest,sVar2);
        }
        goto LAB_00aa1130;
      }
LAB_00aa12d4:
      local_78 = __dest;
      _ZdlPv(__dest);
    }
    plVar5 = (long *)plVar14[1];
    plVar15 = plVar14;
    if ((long *)plVar14[1] == (long *)0x0) {
      do {
        plVar14 = (long *)plVar15[2];
        bVar6 = (long *)*plVar14 != plVar15;
        plVar15 = plVar14;
                    /* try { // try from 00aa1304 to 00ba13cf has its CatchHandler @ 00a9bac4 */
      } while (bVar6);
    }
    else {
      do {
        plVar14 = plVar5;
        plVar5 = (long *)*plVar14;
      } while ((long *)*plVar14 != (long *)0x0);
    }
  } while( true );
}

~~~
