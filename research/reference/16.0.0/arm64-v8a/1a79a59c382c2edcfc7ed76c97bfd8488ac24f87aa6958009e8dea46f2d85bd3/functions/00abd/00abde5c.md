# 00abde5c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00abde5c",
  "name": "FUN_00abde5c",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fbcd21db6de30a07d00b8720eb7e552d1e78aaf258ea455ee6d4b8f4f90fbc5",
  "source_text_sha256": "5fbcd21db6de30a07d00b8720eb7e552d1e78aaf258ea455ee6d4b8f4f90fbc5"
}
~~~

## 呼び出し元

- [00a26020](../00a26/00a26020.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [00440e80](../00440/00440e80.md)
- [00470800](../00470/00470800.md)
- [004800d8](../00480/004800d8.md)
- [00480138](../00480/00480138.md)
- [004802b8](../00480/004802b8.md)
- [004803b0](../00480/004803b0.md)
- [005c175c](../005c1/005c175c.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57c00](../00c57/00c57c00.md)

## 疑似コード / UTF-8 5056 bytes

~~~c

void FUN_00abde5c(long param_1,undefined8 param_2)

{
  ulong uVar1;
  int *piVar2;
  int *piVar3;
  int iVar4;
  char cVar5;
  byte bVar6;
  short sVar7;
  short sVar8;
  undefined4 uVar9;
  undefined8 *puVar10;
  void *__dest;
  undefined8 *puVar11;
  long *plVar12;
  ulong uVar13;
  ulong uVar14;
  undefined8 *puVar15;
  long *plVar16;
  void *__src;
  undefined8 *puVar17;
  int iVar18;
  int *piVar19;
  long lVar20;
  undefined8 *puVar21;
  
  uVar9 = FUN_004803b0(param_2);
  *(undefined4 *)(param_1 + 0x60) = uVar9;
  uVar9 = FUN_004803b0(param_2);
  *(undefined4 *)(param_1 + 100) = uVar9;
                    /* catch() { ... } // from try @ 00abdc80 with catch @ 00abde9c */
  uVar9 = FUN_004803b0(param_2);
  *(undefined4 *)(param_1 + 0x68) = uVar9;
  sVar7 = FUN_00480138(param_2);
                    /* catch() { ... } // from try @ 00abdda4 with catch @ 00abdeb0 */
  iVar18 = (int)sVar7;
  puVar15 = (undefined8 *)(param_1 + 0x30);
  *(undefined8 *)(param_1 + 0x38) = *puVar15;
  if (0 < iVar18) {
    do {
      sVar7 = FUN_00480138(param_2);
      piVar3 = *(int **)(param_1 + 0x38);
                    /* try { // try from 00abdfe0 to 00bbe09f has its CatchHandler @ 00abdee0 */
      if (piVar3 < *(int **)(param_1 + 0x40)) {
        piVar19 = piVar3 + 1;
        *piVar3 = (int)sVar7;
      }
      else {
        __src = (void *)*puVar15;
        lVar20 = (long)piVar3 - (long)__src >> 2;
        uVar1 = lVar20 + 1;
        if (uVar1 >> 0x3e != 0) {
                    /* try { // try from 00abe0a8 to 00bbe143 has its CatchHandler @ 00abdee0 */
                    /* WARNING: Subroutine does not return */
          FUN_00470800(puVar15);
        }
        uVar13 = (long)*(int **)(param_1 + 0x40) - (long)__src;
        uVar14 = (long)uVar13 >> 1;
        if (uVar14 <= uVar1) {
          uVar14 = uVar1;
        }
        if (0x7ffffffffffffffb < uVar13) {
          uVar14 = 0x3fffffffffffffff;
        }
        if (uVar14 == 0) {
          __dest = (void *)0x0;
        }
        else {
          if (uVar14 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
            FUN_00440e80();
          }
          __dest = (void *)_Znwm(uVar14 << 2);
        }
        piVar2 = (int *)((long)__dest + lVar20 * 4);
        piVar19 = piVar2 + 1;
        *piVar2 = (int)sVar7;
        memcpy(__dest,__src,(long)piVar3 - (long)__src);
        *(void **)(param_1 + 0x30) = __dest;
        *(int **)(param_1 + 0x38) = piVar19;
        *(void **)(param_1 + 0x40) = (void *)((long)__dest + uVar14 * 4);
        if (__src != (void *)0x0) {
          _ZdlPv(__src);
        }
      }
      iVar18 = iVar18 + -1;
      *(int **)(param_1 + 0x38) = piVar19;
    } while (iVar18 != 0);
  }
  sVar7 = FUN_00480138(param_2);
  puVar15 = (undefined8 *)(param_1 + 0x50);
  plVar16 = (long *)(param_1 + 0x48);
                    /* try { // try from 00abdee0 to 00bbdfbb has its CatchHandler @ 00abdee0
                       catch() { ... } // from try @ 00abdee0 with catch @ 00abdee0
                       catch() { ... } // from try @ 00abdfe0 with catch @ 00abdee0
                       catch() { ... } // from try @ 00abe0a8 with catch @ 00abdee0 */
  FUN_005c175c(plVar16,*puVar15);
  *puVar15 = 0;
  *(undefined8 *)(param_1 + 0x58) = 0;
  *(undefined8 **)(param_1 + 0x48) = puVar15;
  if (0 < sVar7) {
    iVar18 = 0;
    do {
      sVar8 = FUN_00480138(param_2);
      iVar4 = (int)sVar8;
      cVar5 = FUN_004800d8(param_2);
      puVar11 = (undefined8 *)*puVar15;
      puVar17 = puVar15;
      puVar21 = puVar15;
      if ((undefined8 *)*puVar15 != (undefined8 *)0x0) {
        do {
          while (puVar10 = puVar11, puVar17 = puVar10, iVar4 < *(int *)((long)puVar10 + 0x1c)) {
            puVar11 = (undefined8 *)*puVar10;
            puVar21 = puVar10;
            if ((undefined8 *)*puVar10 == (undefined8 *)0x0) goto LAB_00abdf88;
          }
          if (iVar4 <= *(int *)((long)puVar10 + 0x1c)) goto LAB_00abdf18;
          puVar11 = (undefined8 *)puVar10[1];
        } while ((undefined8 *)puVar10[1] != (undefined8 *)0x0);
        puVar21 = puVar10 + 1;
      }
LAB_00abdf88:
      puVar10 = (undefined8 *)_Znwm(0x28);
      *puVar10 = 0;
      puVar10[1] = 0;
      puVar10[2] = puVar17;
      *puVar21 = puVar10;
      plVar12 = (long *)*plVar16;
      *(int *)((long)puVar10 + 0x1c) = iVar4;
      *(undefined4 *)(puVar10 + 4) = 0;
      puVar11 = puVar10;
      if (*plVar12 != 0) {
        *plVar16 = *plVar12;
                    /* try { // try from 00abdfbc to 00bbdfdf has its CatchHandler @ 00abe0f4 */
        puVar11 = (undefined8 *)*puVar21;
      }
      FUN_0043bb64(*(undefined8 *)(param_1 + 0x50),puVar11);
      *(long *)(param_1 + 0x58) = *(long *)(param_1 + 0x58) + 1;
LAB_00abdf18:
      iVar18 = iVar18 + 1;
      *(int *)(puVar10 + 4) = (int)cVar5;
    } while (iVar18 != sVar7);
  }
  bVar6 = FUN_004802b8(param_2);
  *(byte *)(param_1 + 0x6c) = bVar6 & 1;
                    /* try { // try from 00abe0a0 to 00bbe0a7 has its CatchHandler @ 00abe0d8 */
  return;
}

~~~
