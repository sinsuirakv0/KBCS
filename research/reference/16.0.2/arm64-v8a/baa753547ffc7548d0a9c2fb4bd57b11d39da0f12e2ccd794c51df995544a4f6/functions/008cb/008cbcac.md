# 008cbcac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "008cbcac",
  "name": "FUN_008cbcac",
  "size": 688,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3936043747e230f0c3c2ec5cf279e5e49685ab845d871b9da34b161464f467c8",
  "source_text_sha256": "3936043747e230f0c3c2ec5cf279e5e49685ab845d871b9da34b161464f467c8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00440f00](../00440/00440f00.md)
- [00470880](../00470/00470880.md)
- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [00851550](../00851/00851550.md)
- [008bf604](../008bf/008bf604.md)
- [008c38b4](../008c3/008c38b4.md)
- [008c42e4](../008c4/008c42e4.md)
- [008c4668](../008c4/008c4668.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c580d0](../00c58/00c580d0.md)

## 疑似コード / UTF-8 4391 bytes

~~~c

void FUN_008cbcac(long param_1,undefined8 param_2,int *param_3)

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
  
  iVar14 = *param_3;
  if (iVar14 == 4) {
    lVar13 = *(long *)(param_1 + 8);
    lVar7 = FUN_00851550();
    *(undefined4 *)(lVar7 + 0x44e134) = 0;
    lVar7 = FUN_00851550();
    *(undefined8 *)(*(long *)(&DAT_0044ded0 + lVar7) + 0x20) =
         *(undefined8 *)(*(long *)(&DAT_0044ded0 + lVar7) + 0x18);
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
          lVar7 = FUN_00851550();
          lVar7 = *(long *)(&DAT_0044ded0 + lVar7);
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
              FUN_00470880(lVar7 + 0x18);
            }
            uVar10 = (long)*(int **)(lVar7 + 0x28) - (long)__src;
            uVar11 = (long)uVar10 >> 1;
            if (uVar11 <= uVar2) {
              uVar11 = uVar2;
            }
            if (0x7ffffffffffffffb < uVar10) {
              uVar11 = 0x3fffffffffffffff;
            }
            if (uVar11 == 0) {
              __dest = (void *)0x0;
            }
            else {
              if (uVar11 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
                FUN_00440f00();
              }
              __dest = (void *)_Znwm(uVar11 << 2);
                    /* try { // try from 008cbe10 to 009cbe87 has its CatchHandler @ 008ccdb4 */
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
          lVar7 = FUN_00851550();
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
    lVar7 = FUN_00851550();
    lVar8 = FUN_00851550();
    FUN_008c38b4(lVar7 + 0x44dd00,*(undefined4 *)(lVar8 + 0x44e134),1,0xffffffff,bVar12);
    lVar7 = FUN_00851550();
    FUN_008c42e4(lVar7 + 0x44dd00);
                    /* try { // try from 008cbf08 to 009cbf0b has its CatchHandler @ 008ccdfc */
    lVar7 = FUN_00851550();
    FUN_008c4668(lVar7 + 0x44dd00,1);
    lVar7 = FUN_00851550();
                    /* try { // try from 008cbf1c to 009cbf1f has its CatchHandler @ 008cce00 */
                    /* try { // try from 008cbf20 to 009cbf53 has its CatchHandler @ 008ccf34 */
    *(undefined4 *)(lVar7 + 0x44de74) = 0xffffffff;
    FUN_008bf604(lVar13);
    return;
  }
  if (iVar14 == 3) {
    uVar6 = FUN_0047ad34();
    uVar9 = 0xb;
  }
  else {
    if (iVar14 != 0) {
      return;
    }
    uVar6 = FUN_0047ad34();
    uVar9 = 10;
  }
  FUN_0047ce14(uVar6,uVar9,0);
  return;
}

~~~
