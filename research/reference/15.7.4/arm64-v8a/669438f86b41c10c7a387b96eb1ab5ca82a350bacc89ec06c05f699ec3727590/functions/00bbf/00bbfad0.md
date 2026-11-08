# 00bbfad0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bbfad0",
  "name": "FUN_00bbfad0",
  "size": 808,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4746c9cff12fab10f19ce2789654994d91ce964a2532c6cd324129f59fd56b75",
  "source_text_sha256": "4746c9cff12fab10f19ce2789654994d91ce964a2532c6cd324129f59fd56b75"
}
~~~

## 呼び出し元

- [00bbd308](../00bbd/00bbd308.md)
- [00bbfad0](../00bbf/00bbfad0.md)
- [00bc1754](../00bc1/00bc1754.md)
- [00bc2f0c](../00bc2/00bc2f0c.md)

## 呼び出し先

- [00bbd308](../00bbd/00bbd308.md)
- [00bbde5c](../00bbd/00bbde5c.md)
- [00bbfad0](../00bbf/00bbfad0.md)
- [00bbff70](../00bbf/00bbff70.md)
- [00bc2f0c](../00bc2/00bc2f0c.md)
- [00bc48e0](../00bc4/00bc48e0.md)
- [00bca9c4](../00bca/00bca9c4.md)
- [00bdb180](../00bdb/00bdb180.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
"yptnk"
~~~

## 疑似コード / UTF-8 5841 bytes

~~~c

undefined8 * FUN_00bbfad0(long *param_1)

{
  long *__src;
  undefined8 *puVar1;
  long lVar2;
  long *__ptr;
  void *pvVar3;
  char *pcVar4;
  long lVar5;
  byte *pbVar6;
  long lVar7;
  undefined **ppuVar8;
  undefined1 uVar9;
  byte *pbVar10;
  uint uVar11;
  size_t __n;
  long *plVar12;
  undefined1 auVar13 [16];
  
  pbVar6 = (byte *)*param_1;
  pbVar10 = (byte *)param_1[1];
  if (pbVar10 == pbVar6) {
    uVar11 = 0;
  }
  else {
    uVar11 = (uint)*pbVar6;
  }
  uVar11 = uVar11 - 0x4a >> 1 | uVar11 << 0x1f;
                    /* try { // try from 00bbfb0c to 00cbfb0f has its CatchHandler @ 00bc8b2c */
  if ((int)uVar11 < 5) {
    if (uVar11 == 0) {
      lVar7 = param_1[2];
      lVar5 = param_1[3];
      pbVar6 = pbVar6 + 1;
      __src = param_1 + 5;
      *param_1 = (long)pbVar6;
      while ((pbVar6 == pbVar10 || (*pbVar6 != 0x45))) {
        lVar2 = FUN_00bbfad0(param_1);
        if (lVar2 == 0) {
          return (undefined8 *)0x0;
        }
        plVar12 = (long *)param_1[3];
        if (plVar12 == (long *)param_1[4]) {
          __ptr = (long *)param_1[2];
          __n = (long)plVar12 - (long)__ptr;
          if (__ptr == __src) {
            pvVar3 = malloc(__n * 2);
            if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
              abort();
            }
            if (plVar12 != __src) {
              memcpy(pvVar3,__src,__n);
            }
                    /* try { // try from 00bbfc4c to 00cbfc5f has its CatchHandler @ 00bc87ec */
            param_1[2] = (long)pvVar3;
          }
          else {
            pvVar3 = realloc(__ptr,__n * 2);
            param_1[2] = (long)pvVar3;
            if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
              abort();
            }
          }
          plVar12 = (long *)((long)pvVar3 + __n);
          param_1[4] = (long)((long)pvVar3 + ((long)__n >> 2) * 8);
        }
        param_1[3] = (long)(plVar12 + 1);
                    /* try { // try from 00bbfbd8 to 00cbfbdb has its CatchHandler @ 00bc8890 */
        *plVar12 = lVar2;
        pbVar10 = (byte *)param_1[1];
                    /* try { // try from 00bbfbdc to 00cbfc4b has its CatchHandler @ 00bbf570 */
        pbVar6 = (byte *)*param_1;
      }
      *param_1 = (long)(pbVar6 + 1);
      auVar13 = FUN_00bbff70(param_1,lVar5 - lVar7 >> 3);
      pvVar3 = (void *)param_1[0x266];
                    /* try { // try from 00bbfcb4 to 00cbfcbf has its CatchHandler @ 00bc8a70 */
      lVar7 = *(long *)((long)pvVar3 + 8);
                    /* try { // try from 00bbfcc0 to 00cbfccf has its CatchHandler @ 00bc8a68 */
      puVar1 = pvVar3;
      if (lVar7 - 0xfd0U < 0xfffffffffffff010) {
        puVar1 = malloc(0x1000);
        if (puVar1 == (void *)0x0) {
LAB_00bbfdf4:
                    /* WARNING: Subroutine does not return */
          _ZSt9terminatev();
        }
        lVar7 = 0;
        *puVar1 = pvVar3;
        puVar1[1] = 0;
        param_1[0x266] = (long)puVar1;
      }
      lVar5 = (long)puVar1 + lVar7;
                    /* try { // try from 00bbfcf0 to 00cbfd63 has its CatchHandler @ 00bc8bc4 */
      ppuVar8 = &PTR_FUN_00c19808;
      *(long *)((long)puVar1 + 8) = lVar7 + 0x20;
      uVar9 = 0x29;
LAB_00bbfd00:
      *(undefined8 *)(lVar5 + 0x10) = ppuVar8;
      *(undefined1 *)(lVar5 + 0x18) = uVar9;
      *(undefined1 (*) [16])(lVar5 + 0x20) = auVar13;
      *(ushort *)(lVar5 + 0x19) = *(ushort *)(lVar5 + 0x19) & 0xf000 | 0x540;
      return (undefined8 *)(lVar5 + 0x10);
    }
    if (uVar11 == 1) {
      if (((ulong)((long)pbVar10 - (long)pbVar6) < 2) || (pbVar6[1] != 0x5a)) {
        puVar1 = (undefined8 *)FUN_00bc48e0(param_1);
        return puVar1;
      }
      *param_1 = (long)(pbVar6 + 2);
      puVar1 = (undefined8 *)FUN_00bbd308(param_1);
joined_r0x00bbfb6c:
      if (puVar1 != (undefined8 *)0x0) {
        pcVar4 = (char *)*param_1;
                    /* try { // try from 00bbfb74 to 00cbfb77 has its CatchHandler @ 00bc8ad0 */
        if ((pcVar4 == (char *)param_1[1]) || (*pcVar4 != 'E')) {
          puVar1 = (undefined8 *)0x0;
        }
        else {
          *param_1 = (long)(pcVar4 + 1);
        }
      }
      return puVar1;
    }
  }
  else if (uVar11 == 5) {
    if ((pbVar10 != pbVar6) && (*pbVar6 == 0x54)) {
      if ((ulong)((long)pbVar10 - (long)pbVar6) < 2) {
        uVar11 = 0;
      }
      else {
        uVar11 = (uint)pbVar6[1];
      }
      pcVar4 = memchr("yptnk",uVar11,5);
      if ((pcVar4 != (char *)0x0) && (pcVar4 != "")) {
        lVar7 = FUN_00bca9c4(param_1,0);
        if (lVar7 == 0) {
          return (undefined8 *)0x0;
        }
        lVar5 = FUN_00bbfad0(param_1);
        auVar13._8_8_ = lVar5;
        auVar13._0_8_ = lVar7;
                    /* try { // try from 00bbfd7c to 00cbfd83 has its CatchHandler @ 00bc8b2c */
        if (lVar5 == 0) {
          return (undefined8 *)0x0;
        }
        pvVar3 = (void *)param_1[0x266];
        lVar7 = *(long *)((long)pvVar3 + 8);
        puVar1 = pvVar3;
        if (lVar7 - 0xfd0U < 0xfffffffffffff010) {
          puVar1 = malloc(0x1000);
          if (puVar1 == (void *)0x0) goto LAB_00bbfdf4;
          lVar7 = 0;
          *puVar1 = pvVar3;
          puVar1[1] = 0;
                    /* try { // try from 00bbfdac to 00cbfdbf has its CatchHandler @ 00bc87e8 */
          param_1[0x266] = (long)puVar1;
        }
        lVar5 = (long)puVar1 + lVar7;
        ppuVar8 = &PTR_FUN_00c19878;
        *(long *)((long)puVar1 + 8) = lVar7 + 0x20;
        uVar9 = 0x22;
        goto LAB_00bbfd00;
      }
    }
  }
  else if (uVar11 == 7) {
    *param_1 = (long)(pbVar6 + 1);
    puVar1 = (undefined8 *)FUN_00bc2f0c(param_1);
    goto joined_r0x00bbfb6c;
  }
  puVar1 = (undefined8 *)FUN_00bbde5c(param_1);
  return puVar1;
}

~~~
