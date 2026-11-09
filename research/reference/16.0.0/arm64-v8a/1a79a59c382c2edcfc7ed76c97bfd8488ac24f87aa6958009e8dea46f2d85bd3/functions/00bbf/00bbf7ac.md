# 00bbf7ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bbf7ac",
  "name": "_ZNK3com6google8firebase9messaging3cpp8DataPair6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 648,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "223deea9cd94b4f8d65dc06d836a8289dfc977ca8e46df8d67d6af0558438628",
  "source_text_sha256": "223deea9cd94b4f8d65dc06d836a8289dfc977ca8e46df8d67d6af0558438628"
}
~~~

## 呼び出し元

- [00c5d130](../00c5d/00c5d130.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 5741 bytes

~~~c

undefined4
_ZNK3com6google8firebase9messaging3cpp8DataPair6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
          (int *param_1,long *param_2)

{
  uint uVar1;
  uint uVar2;
  ulong uVar3;
  uint *puVar4;
  ushort uVar5;
  int iVar6;
  long lVar7;
  long lVar8;
  ulong uVar9;
  ulong uVar10;
  ulong uVar11;
  ulong uVar12;
  ushort *puVar13;
  
  lVar8 = *param_2;
  uVar11 = (long)param_1 - lVar8;
  if (((uVar11 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar9 = param_2[1];
    if ((uVar9 < 5) || (uVar10 = uVar9 - 4, uVar10 < uVar11)) {
      return 0;
    }
    lVar7 = param_2[7];
    iVar6 = *param_1;
    uVar1 = (int)lVar7 + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
    if ((((uVar1 <= *(uint *)(param_2 + 2)) && (uVar2 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar12 = uVar11 - (long)iVar6, (uVar12 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
       (uVar12 <= uVar9 - 2)) {
      uVar5 = *(ushort *)(lVar8 + uVar12);
      if ((((uVar5 & 1) == 0) || ((char)param_2[3] == '\0')) && ((uVar5 & 1) == 0)) {
        if (uVar9 <= uVar5) {
          return 0;
        }
        if (uVar9 - uVar5 < uVar12) {
          return 0;
        }
        puVar13 = (ushort *)((long)param_1 - (long)*param_1);
        if (4 < *puVar13) {
          if ((ulong)puVar13[2] != 0) {
            uVar12 = uVar11 + puVar13[2];
            if ((uVar12 & 3) == 0) {
              if (uVar10 < uVar12) {
                return 0;
              }
            }
            else {
                    /* catch() { ... } // from try @ 00bbf754 with catch @ 00bbf87c */
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar10 < uVar12) {
                return 0;
              }
            }
            if ((int)*(uint *)(lVar8 + uVar12) < 1) {
              return 0;
            }
                    /* catch() { ... } // from try @ 00bbf95c with catch @ 00bbf8ac
                       catch() { ... } // from try @ 00bbfa9c with catch @ 00bbf8ac
                       catch() { ... } // from try @ 00bbfb88 with catch @ 00bbf8ac
                       catch() { ... } // from try @ 00bbfcf8 with catch @ 00bbf8ac
                       catch() { ... } // from try @ 00bbfda8 with catch @ 00bbf8ac
                       catch() { ... } // from try @ 00bc0080 with catch @ 00bbf8ac */
            if (uVar9 - 1 < uVar12 + *(uint *)(lVar8 + uVar12)) {
              return 0;
            }
          }
          if (((ulong)puVar13[2] != 0) &&
             (puVar4 = (uint *)((long)param_1 + (ulong)puVar13[2]),
             puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
            uVar12 = (long)puVar4 - lVar8;
            if ((uVar12 & 3) == 0) {
              if (uVar10 < uVar12) {
                return 0;
              }
            }
            else {
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar10 < uVar12) {
                return 0;
              }
            }
            if ((ulong)param_2[4] <= (ulong)*puVar4) {
              return 0;
            }
            uVar3 = (ulong)*puVar4 + 4;
            if (uVar9 - 1 < uVar3 + uVar12) {
              return 0;
            }
            if (uVar9 <= uVar3) {
              return 0;
            }
            if (uVar9 - uVar3 < uVar12) {
              return 0;
            }
            if (*(char *)(lVar8 + uVar3 + uVar12) != '\0') {
              return 0;
            }
          }
                    /* try { // try from 00bbf93c to 00cbf95b has its CatchHandler @ 00bc0130 */
          if (6 < *puVar13) {
            if ((ulong)puVar13[3] != 0) {
              uVar11 = uVar11 + puVar13[3];
              if ((uVar11 & 3) == 0) {
                if (uVar10 < uVar11) {
                  return 0;
                }
              }
              else {
                    /* try { // try from 00bbf95c to 00cbfa4f has its CatchHandler @ 00bbf8ac */
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar10 < uVar11) {
                  return 0;
                }
              }
              if ((int)*(uint *)(lVar8 + uVar11) < 1) {
                return 0;
              }
              if (uVar9 - 1 < uVar11 + *(uint *)(lVar8 + uVar11)) {
                return 0;
              }
            }
            if (((ulong)puVar13[3] != 0) &&
               (puVar4 = (uint *)((long)param_1 + (ulong)puVar13[3]),
               puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
              uVar11 = (long)puVar4 - lVar8;
              if ((uVar11 & 3) == 0) {
                if (uVar10 < uVar11) {
                  return 0;
                }
              }
              else {
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar10 < uVar11) {
                  return 0;
                }
              }
              if ((ulong)param_2[4] <= (ulong)*puVar4) {
                return 0;
              }
              uVar10 = (ulong)*puVar4 + 4;
              if (uVar9 - 1 < uVar10 + uVar11) {
                return 0;
              }
              if (uVar9 <= uVar10) {
                return 0;
              }
              if (uVar9 - uVar10 < uVar11) {
                return 0;
              }
              if (*(char *)(lVar8 + uVar10 + uVar11) != '\0') {
                return 0;
              }
            }
          }
        }
        *(int *)(param_2 + 7) = (int)lVar7;
        return 1;
      }
    }
  }
  return 0;
}

~~~
