# 00abf0bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00abf0bc",
  "name": "FUN_00abf0bc",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0686c8833ea2ec27b9f2bbb555960d79ff583d95a5e279c81a65edddad2fe60",
  "source_text_sha256": "d0686c8833ea2ec27b9f2bbb555960d79ff583d95a5e279c81a65edddad2fe60"
}
~~~

## 呼び出し元

- [00a271bc](../00a27/00a271bc.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [00441220](../00441/00441220.md)
- [00470ba0](../00470/00470ba0.md)
- [00480478](../00480/00480478.md)
- [004804d8](../00480/004804d8.md)
- [00480658](../00480/00480658.md)
- [00480750](../00480/00480750.md)
- [005c1b8c](../005c1/005c1b8c.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c590a0](../00c59/00c590a0.md)

## 疑似コード / UTF-8 4707 bytes

~~~c

void FUN_00abf0bc(long param_1,undefined8 param_2)

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
  
  uVar9 = FUN_00480750(param_2);
  *(undefined4 *)(param_1 + 0x60) = uVar9;
  uVar9 = FUN_00480750(param_2);
  *(undefined4 *)(param_1 + 100) = uVar9;
  uVar9 = FUN_00480750(param_2);
  *(undefined4 *)(param_1 + 0x68) = uVar9;
  sVar7 = FUN_004804d8(param_2);
  iVar18 = (int)sVar7;
  puVar15 = (undefined8 *)(param_1 + 0x30);
  *(undefined8 *)(param_1 + 0x38) = *puVar15;
  if (0 < iVar18) {
    do {
      sVar7 = FUN_004804d8(param_2);
                    /* try { // try from 00abf23c to 00bbf243 has its CatchHandler @ 00abf274 */
      piVar3 = *(int **)(param_1 + 0x38);
                    /* try { // try from 00abf244 to 00bbf2df has its CatchHandler @ 00abf07c */
      if (piVar3 < *(int **)(param_1 + 0x40)) {
        piVar19 = piVar3 + 1;
        *piVar3 = (int)sVar7;
      }
      else {
        __src = (void *)*puVar15;
        lVar20 = (long)piVar3 - (long)__src >> 2;
        uVar1 = lVar20 + 1;
        if (uVar1 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
          FUN_00470ba0(puVar15);
        }
        uVar13 = (long)*(int **)(param_1 + 0x40) - (long)__src;
        uVar14 = (long)uVar13 >> 1;
        if (uVar14 <= uVar1) {
          uVar14 = uVar1;
        }
                    /* catch() { ... } // from try @ 00abf23c with catch @ 00abf274 */
        if (0x7ffffffffffffffb < uVar13) {
          uVar14 = 0x3fffffffffffffff;
        }
        if (uVar14 == 0) {
          __dest = (void *)0x0;
        }
        else {
          if (uVar14 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
            FUN_00441220();
          }
                    /* catch() { ... } // from try @ 00abf158 with catch @ 00abf290 */
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
  sVar7 = FUN_004804d8(param_2);
  puVar15 = (undefined8 *)(param_1 + 0x50);
  plVar16 = (long *)(param_1 + 0x48);
  FUN_005c1b8c(plVar16,*puVar15);
  *puVar15 = 0;
  *(undefined8 *)(param_1 + 0x58) = 0;
  *(undefined8 **)(param_1 + 0x48) = puVar15;
                    /* try { // try from 00abf158 to 00bbf17b has its CatchHandler @ 00abf290 */
  if (0 < sVar7) {
    iVar18 = 0;
    do {
      sVar8 = FUN_004804d8(param_2);
      iVar4 = (int)sVar8;
      cVar5 = FUN_00480478(param_2);
      puVar11 = (undefined8 *)*puVar15;
      puVar17 = puVar15;
      puVar21 = puVar15;
      if ((undefined8 *)*puVar15 != (undefined8 *)0x0) {
        do {
          while (puVar10 = puVar11, puVar17 = puVar10, iVar4 < *(int *)((long)puVar10 + 0x1c)) {
            puVar11 = (undefined8 *)*puVar10;
            puVar21 = puVar10;
            if ((undefined8 *)*puVar10 == (undefined8 *)0x0) goto LAB_00abf1e8;
          }
          if (iVar4 <= *(int *)((long)puVar10 + 0x1c)) goto LAB_00abf178;
          puVar11 = (undefined8 *)puVar10[1];
        } while ((undefined8 *)puVar10[1] != (undefined8 *)0x0);
        puVar21 = puVar10 + 1;
      }
LAB_00abf1e8:
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
        puVar11 = (undefined8 *)*puVar21;
      }
      FUN_0043bf04(*(undefined8 *)(param_1 + 0x50),puVar11);
      *(long *)(param_1 + 0x58) = *(long *)(param_1 + 0x58) + 1;
LAB_00abf178:
                    /* try { // try from 00abf17c to 00bbf23b has its CatchHandler @ 00abf07c */
      iVar18 = iVar18 + 1;
      *(int *)(puVar10 + 4) = (int)cVar5;
    } while (iVar18 != sVar7);
  }
  bVar6 = FUN_00480658(param_2);
  *(byte *)(param_1 + 0x6c) = bVar6 & 1;
  return;
}

~~~
