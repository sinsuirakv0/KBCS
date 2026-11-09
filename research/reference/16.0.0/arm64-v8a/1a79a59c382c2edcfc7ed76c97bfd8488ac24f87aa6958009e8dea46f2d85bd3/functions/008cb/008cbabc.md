# 008cbabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "008cbabc",
  "name": "FUN_008cbabc",
  "size": 688,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ef2baff6d6527183749618460ade3697358ca32473d3bf57d64f5b745029b82",
  "source_text_sha256": "9ef2baff6d6527183749618460ade3697358ca32473d3bf57d64f5b745029b82"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [00470800](../00470/00470800.md)
- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [008514b8](../00851/008514b8.md)
- [008bf568](../008bf/008bf568.md)
- [008c3818](../008c3/008c3818.md)
- [008c41ac](../008c4/008c41ac.md)
- [008c4530](../008c4/008c4530.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57c00](../00c57/00c57c00.md)

## 疑似コード / UTF-8 4294 bytes

~~~c

void FUN_008cbabc(long param_1,undefined8 param_2,int *param_3)

{
  int *piVar1;
  ulong uVar2;
  int *piVar3;
  long *plVar4;
  bool bVar5;
  undefined8 uVar6;
  long lVar7;
  void *__dest;
  long lVar8;
  undefined8 uVar9;
  ulong uVar10;
  ulong uVar11;
  byte bVar12;
  long lVar13;
  void *__src;
  int iVar14;
  int *piVar15;
  byte bVar16;
  long *plVar17;
  long *plVar18;
  
                    /* try { // try from 008cbacc to 009cbbeb has its CatchHandler @ 008cb5a0 */
  iVar14 = *param_3;
  if (iVar14 == 4) {
    lVar13 = *(long *)(param_1 + 8);
    lVar7 = FUN_008514b8();
    *(undefined4 *)(lVar7 + 0x44e134) = 0;
    lVar7 = FUN_008514b8();
    *(undefined8 *)(*(long *)(lVar7 + 0x44ded0) + 0x20) =
         *(undefined8 *)(*(long *)(lVar7 + 0x44ded0) + 0x18);
    plVar17 = *(long **)(lVar13 + 0x28);
    if (plVar17 == (long *)(lVar13 + 0x30)) {
      bVar12 = 0;
    }
    else {
      bVar16 = 0;
      do {
        iVar14 = (int)*(ulong *)((long)plVar17 + 0x1c);
        uVar2 = *(ulong *)((long)plVar17 + 0x1c) & 0xff00000000;
        bVar12 = (uVar2 != 0 && iVar14 == 100) | bVar16;
        if ((uVar2 != 0) && (uVar2 == 0 || iVar14 != 100)) {
          lVar7 = FUN_008514b8();
          lVar7 = *(long *)(lVar7 + 0x44ded0);
          piVar3 = *(int **)(lVar7 + 0x20);
          if (piVar3 < *(int **)(lVar7 + 0x28)) {
            piVar15 = piVar3 + 1;
            *piVar3 = iVar14;
          }
          else {
            __src = *(void **)(lVar7 + 0x18);
            lVar8 = (long)piVar3 - (long)__src >> 2;
            uVar2 = lVar8 + 1;
            if (uVar2 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
              FUN_00470800(lVar7 + 0x18);
            }
                    /* try { // try from 008cbbec to 009cbc03 has its CatchHandler @ 008cccdc */
            uVar10 = (long)*(int **)(lVar7 + 0x28) - (long)__src;
            uVar11 = (long)uVar10 >> 1;
            if (uVar11 <= uVar2) {
              uVar11 = uVar2;
            }
                    /* try { // try from 008cbc04 to 009cbd77 has its CatchHandler @ 008cb5a0 */
            if (0x7ffffffffffffffb < uVar10) {
              uVar11 = 0x3fffffffffffffff;
            }
            if (uVar11 == 0) {
              __dest = (void *)0x0;
            }
            else {
              if (uVar11 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
                FUN_00440e80();
              }
              __dest = (void *)_Znwm(uVar11 << 2);
            }
            piVar1 = (int *)((long)__dest + lVar8 * 4);
            piVar15 = piVar1 + 1;
            *piVar1 = iVar14;
            memcpy(__dest,__src,(long)piVar3 - (long)__src);
            *(void **)(lVar7 + 0x18) = __dest;
            *(int **)(lVar7 + 0x20) = piVar15;
            *(void **)(lVar7 + 0x28) = (void *)((long)__dest + uVar11 * 4);
            if (__src != (void *)0x0) {
              _ZdlPv(__src);
            }
          }
          *(int **)(lVar7 + 0x20) = piVar15;
          lVar7 = FUN_008514b8();
          *(undefined4 *)(lVar7 + 0x44e134) = 1;
          bVar12 = bVar16;
        }
        plVar4 = (long *)plVar17[1];
        plVar18 = plVar17;
        if ((long *)plVar17[1] == (long *)0x0) {
          do {
            plVar17 = (long *)plVar18[2];
            bVar5 = (long *)*plVar17 != plVar18;
            plVar18 = plVar17;
          } while (bVar5);
        }
        else {
          do {
            plVar17 = plVar4;
            plVar4 = (long *)*plVar17;
          } while ((long *)*plVar17 != (long *)0x0);
        }
        bVar16 = bVar12;
      } while (plVar17 != (long *)(lVar13 + 0x30));
    }
    lVar7 = FUN_008514b8();
    lVar8 = FUN_008514b8();
    FUN_008c3818(&DAT_0044dd00 + lVar7,*(undefined4 *)(lVar8 + 0x44e134),1,0xffffffff,bVar12);
    lVar7 = FUN_008514b8();
    FUN_008c41ac(&DAT_0044dd00 + lVar7);
    lVar7 = FUN_008514b8();
    FUN_008c4530(&DAT_0044dd00 + lVar7,1);
    lVar7 = FUN_008514b8();
    *(undefined4 *)(lVar7 + 0x44de74) = 0xffffffff;
    FUN_008bf568(lVar13);
    return;
  }
  if (iVar14 == 3) {
    uVar6 = FUN_0047acb4();
    uVar9 = 0xb;
  }
  else {
    if (iVar14 != 0) {
      return;
    }
    uVar6 = FUN_0047acb4();
    uVar9 = 10;
  }
  FUN_0047cd94(uVar6,uVar9,0);
  return;
}

~~~
