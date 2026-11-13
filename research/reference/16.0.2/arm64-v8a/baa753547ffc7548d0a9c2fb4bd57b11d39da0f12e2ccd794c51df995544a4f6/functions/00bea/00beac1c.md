# 00beac1c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00beac1c",
  "name": "FUN_00beac1c",
  "size": 704,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f7386be9917f78ef3e968ca59e690499eb5a1d8ba4a544d8e663ea935976f20",
  "source_text_sha256": "1f7386be9917f78ef3e968ca59e690499eb5a1d8ba4a544d8e663ea935976f20"
}
~~~

## 呼び出し元

- [00be3fbc](../00be3/00be3fbc.md)

## 呼び出し先

- [00beaedc](../00bea/00beaedc.md)

## 疑似コード / UTF-8 4307 bytes

~~~c

bool FUN_00beac1c(short *param_1,short *param_2)

{
  short sVar1;
  long lVar2;
  short sVar3;
  short sVar4;
  ulong uVar5;
  int iVar6;
  short sVar7;
  short *psVar8;
  long lVar9;
  short sVar10;
  short *psVar11;
  short *psVar12;
  long lVar13;
  short *psVar14;
  
  uVar5 = (long)param_2 - (long)param_1 >> 1;
  if (2 < (long)uVar5) {
    if (uVar5 == 3) {
      sVar10 = param_1[1];
      sVar4 = *param_1;
      sVar1 = param_2[-1];
      if (sVar4 <= sVar10) {
        if (sVar10 <= sVar1) {
          return true;
        }
        param_1[1] = sVar1;
        param_2[-1] = sVar10;
        sVar4 = *param_1;
        if (param_1[1] < sVar4) {
          *param_1 = param_1[1];
          param_1[1] = sVar4;
          return true;
        }
        return true;
      }
      if (sVar1 < sVar10) {
        *param_1 = sVar1;
      }
      else {
        *param_1 = sVar10;
        param_1[1] = sVar4;
        if (sVar4 <= param_2[-1]) {
          return true;
        }
        param_1[1] = param_2[-1];
      }
      goto LAB_00beaeb0;
    }
    if (uVar5 != 4) {
      if (uVar5 == 5) {
        FUN_00beaedc(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00beacb0;
    }
    sVar4 = *param_1;
    psVar12 = param_1 + 1;
    sVar10 = *psVar12;
    psVar8 = param_1 + 2;
    sVar1 = *psVar8;
    psVar11 = param_1;
    if (sVar10 < sVar4) {
      psVar14 = psVar8;
      sVar3 = sVar4;
      if (sVar10 <= sVar1) {
        *param_1 = sVar10;
        param_1[1] = sVar4;
        sVar10 = sVar1;
        psVar11 = psVar12;
        goto joined_r0x00beae3c;
      }
    }
    else {
      sVar7 = sVar1;
      if (sVar10 <= sVar1) goto LAB_00beae54;
      *psVar12 = sVar1;
      *psVar8 = sVar10;
      psVar14 = psVar12;
      sVar3 = sVar10;
joined_r0x00beae3c:
      sVar7 = sVar10;
      if (sVar4 <= sVar1) goto LAB_00beae54;
    }
    *psVar11 = sVar1;
    *psVar14 = sVar4;
    sVar7 = sVar3;
LAB_00beae54:
    if (sVar7 <= param_2[-1]) {
      return true;
    }
    *psVar8 = param_2[-1];
    param_2[-1] = sVar7;
    sVar4 = *psVar8;
    sVar10 = *psVar12;
    if (sVar4 < sVar10) {
      sVar1 = *param_1;
      param_1[1] = sVar4;
      param_1[2] = sVar10;
      if (sVar4 < sVar1) {
                    /* try { // try from 00beae8c to 00ceafef has its CatchHandler @ 00beae8c
                       catch() { ... } // from try @ 00beae8c with catch @ 00beae8c
                       catch() { ... } // from try @ 00beaff8 with catch @ 00beae8c */
        *param_1 = sVar4;
        param_1[1] = sVar1;
        return true;
      }
      return true;
    }
    return true;
  }
  if (uVar5 < 2) {
    return true;
  }
  if (uVar5 == 2) {
    sVar4 = *param_1;
    if (sVar4 <= param_2[-1]) {
      return true;
    }
    *param_1 = param_2[-1];
LAB_00beaeb0:
    param_2[-1] = sVar4;
    return true;
  }
LAB_00beacb0:
  sVar4 = *param_1;
  psVar8 = param_1 + 1;
  sVar10 = *psVar8;
  psVar12 = param_1 + 2;
  sVar1 = *psVar12;
  psVar11 = param_1;
  if (sVar10 < sVar4) {
    psVar14 = psVar12;
    if (sVar10 <= sVar1) {
      *param_1 = sVar10;
      param_1[1] = sVar4;
      psVar11 = psVar8;
      goto joined_r0x00bead90;
    }
  }
  else {
    if (sVar10 <= sVar1) goto LAB_00bead9c;
    *psVar8 = sVar1;
    *psVar12 = sVar10;
    psVar14 = psVar8;
joined_r0x00bead90:
    if (sVar4 <= sVar1) goto LAB_00bead9c;
  }
  *psVar11 = sVar1;
  *psVar14 = sVar4;
LAB_00bead9c:
  if (param_1 + 3 != param_2) {
    iVar6 = 0;
    lVar9 = 6;
    psVar11 = param_1 + 3;
    do {
      psVar8 = psVar11;
      sVar4 = *psVar8;
      sVar10 = *psVar12;
      lVar13 = lVar9;
      if (sVar4 < sVar10) {
        do {
          lVar2 = lVar13 + -2;
          *(short *)((long)param_1 + lVar13) = sVar10;
          psVar11 = param_1;
          if (lVar2 == 0) goto LAB_00beadb8;
          sVar10 = *(short *)((long)param_1 + lVar13 + -4);
          lVar13 = lVar2;
        } while (sVar4 < sVar10);
        psVar11 = (short *)((long)param_1 + lVar2);
LAB_00beadb8:
        iVar6 = iVar6 + 1;
        *psVar11 = sVar4;
        if (iVar6 == 8) {
          return psVar8 + 1 == param_2;
        }
      }
      lVar9 = lVar9 + 2;
      psVar11 = psVar8 + 1;
      psVar12 = psVar8;
    } while (psVar8 + 1 != param_2);
  }
  return true;
}

~~~
