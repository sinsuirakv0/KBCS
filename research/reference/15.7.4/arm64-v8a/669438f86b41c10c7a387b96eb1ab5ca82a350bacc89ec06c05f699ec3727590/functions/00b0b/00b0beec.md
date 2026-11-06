# 00b0beec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00b0beec",
  "name": "_ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers8VerifierE",
  "size": 608,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a696791560a42c2f1a2c2410912a77ee73931d2b907f877b1c2efe71954bcb23",
  "source_text_sha256": "a696791560a42c2f1a2c2410912a77ee73931d2b907f877b1c2efe71954bcb23"
}
~~~

## 呼び出し元

- [00bdead0](../00bde/00bdead0.md)

## 呼び出し先

- [00bdeac0](../00bde/00bdeac0.md)

## 疑似コード / UTF-8 4924 bytes

~~~c

undefined4
_ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers8VerifierE(int *param_1,long *param_2)

{
  uint uVar1;
  ulong uVar2;
  uint *puVar3;
  ushort uVar4;
  int iVar5;
  uint uVar6;
  long lVar7;
  ulong uVar8;
  ulong uVar9;
  ulong uVar10;
  ulong uVar11;
  ushort *puVar12;
  
  lVar7 = *param_2;
  uVar9 = (long)param_1 - lVar7;
                    /* try { // try from 00b0bf04 to 00c0bf0f has its CatchHandler @ 00b0c320 */
  if (((uVar9 & 3) == 0) || ((char)param_2[5] == '\0')) {
                    /* try { // try from 00b0bf10 to 00c0bf1b has its CatchHandler @ 00b0c304 */
    uVar8 = param_2[1];
                    /* try { // try from 00b0bf1c to 00c0bf2b has its CatchHandler @ 00b0c2f0 */
    if (uVar8 < 5) {
      return 0;
    }
    uVar10 = uVar8 - 4;
    if (uVar10 < uVar9) {
      return 0;
    }
                    /* try { // try from 00b0bf2c to 00c0bf77 has its CatchHandler @ 00b0bea4 */
    iVar5 = *param_1;
    uVar6 = (int)param_2[2] + 1;
    uVar1 = (int)param_2[3] + 1;
    *(uint *)(param_2 + 2) = uVar6;
    *(uint *)(param_2 + 3) = uVar1;
                    /* try { // try from 00b0bf78 to 00c0bf87 has its CatchHandler @ 00b0c2e8 */
    if (((((uVar6 <= *(uint *)((long)param_2 + 0x14)) && (uVar1 <= *(uint *)((long)param_2 + 0x1c)))
         && ((uVar11 = uVar9 - (long)iVar5, (uVar11 & 1) == 0 || ((char)param_2[5] == '\0')))) &&
        (uVar11 <= uVar8 - 2)) &&
       ((uVar4 = *(ushort *)(lVar7 + uVar11), (uVar4 & 1) == 0 || ((char)param_2[5] == '\0')))) {
      if (uVar8 <= uVar4) {
        return 0;
      }
      if (uVar8 - uVar4 < uVar11) {
        return 0;
      }
      puVar12 = (ushort *)((long)param_1 - (long)*param_1);
      uVar4 = *puVar12;
      if (4 < uVar4) {
        if ((ulong)puVar12[2] != 0) {
          uVar11 = uVar9 + puVar12[2];
          if ((uVar11 & 3) == 0) {
                    /* try { // try from 00b0bff4 to 00c0c00b has its CatchHandler @ 00b0c324 */
            if (uVar10 < uVar11) {
              return 0;
            }
          }
          else {
                    /* try { // try from 00b0bfd8 to 00c0bfdf has its CatchHandler @ 00b0c328 */
            if ((char)param_2[5] != '\0') {
              return 0;
            }
            if (uVar10 < uVar11) {
              return 0;
            }
          }
          if ((int)*(uint *)(lVar7 + uVar11) < 1) {
            return 0;
          }
          if (uVar8 - 1 < uVar11 + *(uint *)(lVar7 + uVar11)) {
            return 0;
          }
        }
        if (((ulong)puVar12[2] != 0) &&
           (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[2]),
           puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
          uVar11 = (long)puVar3 - lVar7;
          if ((uVar11 & 3) == 0) {
            if (uVar10 < uVar11) {
              return 0;
            }
          }
          else {
            if ((char)param_2[5] != '\0') {
              return 0;
            }
            if (uVar10 < uVar11) {
              return 0;
            }
          }
          if (0x7ffffffe < *puVar3) {
            return 0;
          }
          uVar2 = (ulong)*puVar3 + 4;
          if (uVar8 - 1 < uVar2 + uVar11) {
            return 0;
          }
                    /* try { // try from 00b0c080 to 00c0c087 has its CatchHandler @ 00b0c338 */
          if (uVar8 <= uVar2) {
            return 0;
          }
          if (uVar8 - uVar2 < uVar11) {
            return 0;
          }
          if (*(char *)(lVar7 + uVar2 + uVar11) != '\0') {
            return 0;
          }
        }
        if (6 < uVar4) {
          if (((ulong)puVar12[3] != 0) && (uVar10 < uVar9 + puVar12[3])) {
            return 0;
          }
          if (8 < uVar4) {
            if ((ulong)puVar12[4] != 0) {
              uVar9 = uVar9 + puVar12[4];
              if ((uVar9 & 3) == 0) {
                if (uVar10 < uVar9) {
                  return 0;
                }
              }
              else {
                if ((char)param_2[5] != '\0') {
                  return 0;
                }
                if (uVar10 < uVar9) {
                  return 0;
                }
              }
              if ((int)*(uint *)(lVar7 + uVar9) < 1) {
                return 0;
              }
              if (uVar8 - 1 < uVar9 + *(uint *)(lVar7 + uVar9)) {
                return 0;
              }
            }
            if (((ulong)puVar12[4] != 0) &&
               (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[4]),
               lVar7 = (long)puVar3 + (ulong)*puVar3, lVar7 != 0)) {
              uVar9 = _ZNK8firebase3fbs11AndroidInfo6VerifyERN11flatbuffers8VerifierE(lVar7);
              if ((uVar9 & 1) == 0) {
                return 0;
              }
              uVar6 = *(uint *)(param_2 + 2);
            }
          }
        }
      }
      *(uint *)(param_2 + 2) = uVar6 - 1;
      return 1;
    }
  }
  return 0;
}

~~~
