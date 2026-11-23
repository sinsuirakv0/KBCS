# 00beddb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0175.md#review-2a5c84bb92f03675ccce97000e33c3fe)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beddb8",
  "name": "FUN_00beddb8",
  "size": 672,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9eab096f37bfea793651ba5732bad1046855dee3d7ee11e614456302826c63e8",
  "source_text_sha256": "9eab096f37bfea793651ba5732bad1046855dee3d7ee11e614456302826c63e8"
}
~~~

## 呼び出し元

- [00be7400](../00be7/00be7400.md)

## 呼び出し先

- [00bee058](../00bee/00bee058.md)

## 疑似コード / UTF-8 4363 bytes

~~~c

bool FUN_00beddb8(float *param_1,float *param_2)

{
  long lVar1;
  ulong uVar2;
  float *pfVar3;
  int iVar4;
  float *pfVar5;
  float *pfVar6;
  long lVar7;
  float *pfVar8;
  long lVar9;
  float fVar10;
  float fVar11;
  float fVar12;
  float fVar13;
  float fVar14;
  
  uVar2 = (long)param_2 - (long)param_1 >> 2;
  if (2 < (long)uVar2) {
    if (uVar2 == 3) {
      fVar10 = *param_1;
      fVar12 = param_1[1];
      fVar13 = param_2[-1];
                    /* try { // try from 00bede30 to 00cee037 has its CatchHandler @ 00bed9b8 */
      if (fVar10 <= fVar12) {
        if (fVar12 <= fVar13) {
          return true;
        }
        param_1[1] = fVar13;
        param_2[-1] = fVar12;
        fVar10 = *param_1;
        if (param_1[1] < fVar10) {
          *param_1 = param_1[1];
          param_1[1] = fVar10;
          return true;
        }
        return true;
      }
      if (fVar12 <= fVar13) {
        *param_1 = fVar12;
        param_1[1] = fVar10;
        if (fVar10 <= param_2[-1]) {
          return true;
        }
        param_1[1] = param_2[-1];
      }
      else {
        *param_1 = fVar13;
      }
      goto LAB_00bee02c;
    }
    if (uVar2 != 4) {
      if (uVar2 == 5) {
        FUN_00bee058(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00bede48;
    }
    fVar12 = *param_1;
    pfVar8 = param_1 + 1;
    fVar10 = *pfVar8;
    pfVar3 = param_1 + 2;
    fVar13 = *pfVar3;
    pfVar5 = param_1;
    if (fVar12 <= fVar10) {
      fVar11 = fVar13;
      if (fVar10 <= fVar13) goto LAB_00bedfdc;
      *pfVar8 = fVar13;
      *pfVar3 = fVar10;
      pfVar6 = pfVar8;
      fVar14 = fVar10;
joined_r0x00bedfc4:
      fVar11 = fVar10;
      if (fVar12 <= fVar13) goto LAB_00bedfdc;
    }
    else {
      pfVar6 = pfVar3;
      fVar14 = fVar12;
      if (fVar10 <= fVar13) {
        *param_1 = fVar10;
        param_1[1] = fVar12;
        fVar10 = fVar13;
        pfVar5 = pfVar8;
        goto joined_r0x00bedfc4;
      }
    }
    *pfVar5 = fVar13;
    *pfVar6 = fVar12;
    fVar11 = fVar14;
LAB_00bedfdc:
    if (fVar11 <= param_2[-1]) {
      return true;
    }
    *pfVar3 = param_2[-1];
    param_2[-1] = fVar11;
    fVar10 = *pfVar3;
    fVar12 = *pfVar8;
    if (fVar10 < fVar12) {
      fVar13 = *param_1;
      param_1[1] = fVar10;
      param_1[2] = fVar12;
      if (fVar10 < fVar13) {
        *param_1 = fVar10;
        param_1[1] = fVar13;
        return true;
      }
      return true;
    }
    return true;
  }
  if (uVar2 < 2) {
    return true;
  }
  if (uVar2 == 2) {
    fVar10 = *param_1;
    if (fVar10 <= param_2[-1]) {
      return true;
    }
    *param_1 = param_2[-1];
LAB_00bee02c:
    param_2[-1] = fVar10;
    return true;
  }
LAB_00bede48:
  fVar10 = *param_1;
  pfVar3 = param_1 + 1;
  fVar13 = *pfVar3;
  pfVar8 = param_1 + 2;
  fVar12 = *pfVar8;
  pfVar5 = param_1;
  if (fVar10 <= fVar13) {
    if (fVar13 <= fVar12) goto LAB_00bedf24;
    *pfVar3 = fVar12;
    *pfVar8 = fVar13;
    pfVar6 = pfVar3;
joined_r0x00bedf18:
    if (fVar10 <= fVar12) goto LAB_00bedf24;
  }
  else {
    pfVar6 = pfVar8;
    if (fVar13 <= fVar12) {
      *param_1 = fVar13;
      param_1[1] = fVar10;
      pfVar5 = pfVar3;
      goto joined_r0x00bedf18;
    }
  }
  *pfVar5 = fVar12;
  *pfVar6 = fVar10;
LAB_00bedf24:
  if (param_1 + 3 != param_2) {
    iVar4 = 0;
    lVar7 = 0xc;
    pfVar5 = param_1 + 3;
    do {
      pfVar3 = pfVar5;
      fVar10 = *pfVar3;
      fVar12 = *pfVar8;
      lVar9 = lVar7;
      if (fVar10 < fVar12) {
        do {
          lVar1 = lVar9 + -4;
          *(float *)((long)param_1 + lVar9) = fVar12;
          pfVar5 = param_1;
          if (lVar1 == 0) goto LAB_00bedf40;
          fVar12 = *(float *)((long)param_1 + lVar9 + -8);
          lVar9 = lVar1;
        } while (fVar10 < fVar12);
        pfVar5 = (float *)((long)param_1 + lVar1);
LAB_00bedf40:
        iVar4 = iVar4 + 1;
        *pfVar5 = fVar10;
        if (iVar4 == 8) {
                    /* try { // try from 00bee048 to 00cee057 has its CatchHandler @ 00bee220 */
          return pfVar3 + 1 == param_2;
        }
      }
      lVar7 = lVar7 + 4;
      pfVar5 = pfVar3 + 1;
      pfVar8 = pfVar3;
    } while (pfVar3 + 1 != param_2);
  }
                    /* try { // try from 00bee038 to 00cee043 has its CatchHandler @ 00bee230 */
  return true;
}

~~~
