# 00b6bfdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b6bfdc",
  "name": "_ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 640,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c4db6b72ba7917b092ff2aa58c8f10a9f34daf360b48c6a65ad644509b1f8892",
  "source_text_sha256": "c4db6b72ba7917b092ff2aa58c8f10a9f34daf360b48c6a65ad644509b1f8892"
}
~~~

## 呼び出し元

- [00c5b570](../00c5b/00c5b570.md)

## 呼び出し先

- [00c5b560](../00c5b/00c5b560.md)

## 疑似コード / UTF-8 5395 bytes

~~~c

undefined4
_ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
          (int *param_1,long *param_2)

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
  if (((uVar9 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar8 = param_2[1];
    if (uVar8 < 5) {
      return 0;
    }
    uVar10 = uVar8 - 4;
    if (uVar10 < uVar9) {
      return 0;
    }
                    /* try { // try from 00b6c020 to 00c6c0f7 has its CatchHandler @ 00b6c020
                       catch() { ... } // from try @ 00b6c020 with catch @ 00b6c020
                       catch() { ... } // from try @ 00b6c14c with catch @ 00b6c020 */
    iVar5 = *param_1;
    uVar6 = (int)param_2[7] + 1;
    uVar1 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar6;
    *(uint *)((long)param_2 + 0x3c) = uVar1;
    if ((((uVar6 <= *(uint *)(param_2 + 2)) && (uVar1 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar11 = uVar9 - (long)iVar5, (uVar11 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
       (uVar11 <= uVar8 - 2)) {
      uVar4 = *(ushort *)(lVar7 + uVar11);
      if ((((uVar4 & 1) == 0) || ((char)param_2[3] == '\0')) && ((uVar4 & 1) == 0)) {
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
            if ((int)*(uint *)(lVar7 + uVar11) < 1) {
              return 0;
            }
            if (uVar8 - 1 < uVar11 + *(uint *)(lVar7 + uVar11)) {
              return 0;
            }
          }
                    /* try { // try from 00b6c0f8 to 00c6c14b has its CatchHandler @ 00b6c228 */
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
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar10 < uVar11) {
                return 0;
              }
            }
            if ((ulong)param_2[4] <= (ulong)*puVar3) {
              return 0;
            }
            uVar2 = (ulong)*puVar3 + 4;
                    /* try { // try from 00b6c14c to 00c6c253 has its CatchHandler @ 00b6c020 */
            if (uVar8 - 1 < uVar2 + uVar11) {
              return 0;
            }
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
            if ((ulong)puVar12[3] != 0) {
              uVar11 = uVar9 + puVar12[3];
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
                  if ((char)param_2[3] != '\0') {
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
                    /* catch() { ... } // from try @ 00b6c0f8 with catch @ 00b6c228 */
                uVar9 = _ZNK8firebase3fbs11AndroidInfo6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                  (lVar7,param_2);
                if ((uVar9 & 1) == 0) {
                  return 0;
                }
                uVar6 = *(uint *)(param_2 + 7);
              }
            }
          }
        }
        *(uint *)(param_2 + 7) = uVar6 - 1;
        return 1;
      }
    }
  }
  return 0;
}

~~~
