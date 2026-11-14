# 00bf7bac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bf7bac",
  "name": "_ZNSt6__ndk110to_wstringEi",
  "size": 472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5123c61641a8c2905427bcc8b520cb10550dd43394a7927195727aec9e968877",
  "source_text_sha256": "5123c61641a8c2905427bcc8b520cb10550dd43394a7927195727aec9e968877"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00441220](../00441/00441220.md)
- [006d7aa8](../006d7/006d7aa8.md)
- [00bf92e8](../00bf9/00bf92e8.md)
- [00c58f30](../00c58/00c58f30.md)

## 疑似コード / UTF-8 3884 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void _ZNSt6__ndk110to_wstringEi(ulong *param_1,uint param_2)

{
  uint uVar1;
  undefined1 auVar2 [16];
  undefined1 auVar3 [16];
  undefined1 auVar4 [16];
  undefined1 auVar5 [16];
  byte *pbVar6;
  byte *pbVar7;
  byte *pbVar8;
  uint *puVar9;
  ulong uVar10;
  undefined1 (*pauVar11) [16];
  ulong uVar12;
  uint *puVar13;
  ulong uVar14;
  undefined1 auVar15 [16];
  undefined1 auVar16 [16];
  undefined1 auVar17 [16];
  undefined1 auVar18 [16];
  undefined1 auVar19 [16];
  undefined1 auVar20 [16];
  byte local_3c [11];
  byte bStack_31;
  
  pbVar6 = local_3c;
  pbVar7 = &bStack_31;
  if ((int)param_2 < 0) {
    pbVar6 = (byte *)((ulong)pbVar6 | 1);
    param_2 = -param_2;
    local_3c[0] = 0x2d;
  }
  if ((9 < (long)pbVar7 - (long)pbVar6) ||
     (uVar1 = (uint)((0x20 - (int)LZCOUNT(param_2 | 1)) * 0x4d1) >> 0xc,
     (long)(ulong)((uVar1 - (param_2 < *(uint *)(&DAT_00310878 + (ulong)uVar1 * 4))) + 1) <=
     (long)pbVar7 - (long)pbVar6)) {
    pbVar7 = (byte *)FUN_00bf92e8();
  }
  uVar14 = (long)pbVar7 - (long)local_3c;
  if (0x3ffffffffffffff7 < uVar14) {
    FUN_006d7aa8(param_1);
LAB_00bf7d80:
                    /* WARNING: Subroutine does not return */
    FUN_00441220();
  }
  if (uVar14 < 5) {
    puVar13 = (uint *)((long)param_1 + 4);
    *(char *)param_1 = (char)((int)uVar14 << 1);
  }
  else {
    uVar12 = (uVar14 & 0x3ffffffffffffffe) + 2;
    if ((uVar14 | 1) != 5) {
      uVar12 = uVar14 | 1;
    }
    if (0x3ffffffffffffffe < uVar12) goto LAB_00bf7d80;
    puVar13 = (uint *)_Znwm((uVar12 + 1) * 4);
    param_1[1] = uVar14;
    param_1[2] = (ulong)puVar13;
    *param_1 = uVar12 + 1 | 1;
  }
  auVar5 = _DAT_002c31e0;
  auVar4 = _DAT_002c2d90;
  auVar3 = _DAT_002c28d0;
  auVar2 = _DAT_002c21b0;
  pbVar6 = local_3c;
  if (pbVar6 != pbVar7) {
    uVar14 = (long)pbVar7 - (long)pbVar6;
    if (0x1f < uVar14) {
      uVar10 = uVar14 & 0xffffffffffffffe0;
      puVar9 = puVar13 + uVar10;
      pbVar6 = local_3c + uVar10;
      pauVar11 = (undefined1 (*) [16])&stack0xffffffffffffffd4;
      puVar13 = puVar13 + 0x10;
      uVar12 = uVar10;
      do {
        auVar15 = pauVar11[-1];
        auVar16 = *pauVar11;
        uVar12 = uVar12 - 0x20;
        pauVar11 = pauVar11 + 2;
        auVar17 = a64_TBL(ZEXT816(0),auVar15,auVar2);
        auVar18 = a64_TBL(ZEXT816(0),auVar15,auVar4);
        auVar19 = a64_TBL(ZEXT816(0),auVar15,auVar5);
        auVar15 = a64_TBL(ZEXT816(0),auVar15,auVar3);
        auVar20 = a64_TBL(ZEXT816(0),auVar16,auVar2);
        *(long *)(puVar13 + -6) = auVar18._8_8_;
        *(long *)(puVar13 + -8) = auVar18._0_8_;
        *(long *)(puVar13 + -2) = auVar17._8_8_;
        *(long *)(puVar13 + -4) = auVar17._0_8_;
        auVar17 = a64_TBL(ZEXT816(0),auVar16,auVar4);
        auVar18 = a64_TBL(ZEXT816(0),auVar16,auVar5);
        auVar16 = a64_TBL(ZEXT816(0),auVar16,auVar3);
        *(long *)(puVar13 + -0xe) = auVar15._8_8_;
        *(long *)(puVar13 + -0x10) = auVar15._0_8_;
        *(long *)(puVar13 + -10) = auVar19._8_8_;
        *(long *)(puVar13 + -0xc) = auVar19._0_8_;
        *(long *)(puVar13 + 10) = auVar17._8_8_;
        *(long *)(puVar13 + 8) = auVar17._0_8_;
        *(long *)(puVar13 + 0xe) = auVar20._8_8_;
        *(long *)(puVar13 + 0xc) = auVar20._0_8_;
        *(long *)(puVar13 + 2) = auVar16._8_8_;
        *(long *)puVar13 = auVar16._0_8_;
        *(long *)(puVar13 + 6) = auVar18._8_8_;
        *(long *)(puVar13 + 4) = auVar18._0_8_;
        puVar13 = puVar13 + 0x20;
      } while (uVar12 != 0);
      puVar13 = puVar9;
      if (uVar14 == uVar10) goto LAB_00bf7d5c;
    }
    do {
      pbVar8 = pbVar6 + 1;
      puVar9 = puVar13 + 1;
      *puVar13 = (uint)*pbVar6;
      pbVar6 = pbVar8;
      puVar13 = puVar9;
    } while (pbVar8 != pbVar7);
  }
LAB_00bf7d5c:
  *puVar13 = 0;
  return;
}

~~~
