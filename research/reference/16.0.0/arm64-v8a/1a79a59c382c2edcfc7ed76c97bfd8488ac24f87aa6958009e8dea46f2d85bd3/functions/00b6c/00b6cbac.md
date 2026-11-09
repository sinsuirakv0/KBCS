# 00b6cbac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b6cbac",
  "name": "_ZNK8firebase3fbs17AnalyticsProperty6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d62325fe6ec5b110f99140ba539caf10eb9b51628ad42032e0a7d128b2af99c1",
  "source_text_sha256": "d62325fe6ec5b110f99140ba539caf10eb9b51628ad42032e0a7d128b2af99c1"
}
~~~

## 呼び出し元

- [00c5b5b0](../00c5b/00c5b5b0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 4029 bytes

~~~c

undefined4
_ZNK8firebase3fbs17AnalyticsProperty6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
          (int *param_1,long *param_2)

{
  uint uVar1;
  uint uVar2;
  uint *puVar3;
  ushort uVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  ulong uVar8;
  ulong uVar9;
  ulong uVar10;
  ulong uVar11;
  ushort *puVar12;
  
  lVar7 = *param_2;
  uVar10 = (long)param_1 - lVar7;
  if (((uVar10 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar8 = param_2[1];
    if ((uVar8 < 5) || (uVar9 = uVar8 - 4, uVar9 < uVar10)) {
      return 0;
    }
    lVar6 = param_2[7];
    iVar5 = *param_1;
    uVar1 = (int)lVar6 + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
                    /* catch() { ... } // from try @ 00b6caa8 with catch @ 00b6cc14 */
    if ((((uVar1 <= *(uint *)(param_2 + 2)) && (uVar2 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar11 = uVar10 - (long)iVar5, (uVar11 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
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
        if (4 < *puVar12) {
          if ((ulong)puVar12[2] != 0) {
            uVar10 = uVar10 + puVar12[2];
            if ((uVar10 & 3) == 0) {
              if (uVar9 < uVar10) {
                return 0;
              }
            }
            else {
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar9 < uVar10) {
                return 0;
              }
            }
            if ((int)*(uint *)(lVar7 + uVar10) < 1) {
              return 0;
            }
            if (uVar8 - 1 < uVar10 + *(uint *)(lVar7 + uVar10)) {
              return 0;
            }
          }
          if (((ulong)puVar12[2] != 0) &&
             (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[2]),
             puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
            uVar10 = (long)puVar3 - lVar7;
            if ((uVar10 & 3) == 0) {
              if (uVar9 < uVar10) {
                return 0;
              }
            }
            else {
              if ((char)param_2[3] != '\0') {
                return 0;
              }
                    /* try { // try from 00b6cce4 to 00c6cdb3 has its CatchHandler @ 00b6cce4
                       catch() { ... } // from try @ 00b6cce4 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6cdd4 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6cee4 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6cf64 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6d038 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6d16c with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6d370 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6d490 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6d600 with catch @ 00b6cce4 */
              if (uVar9 < uVar10) {
                return 0;
              }
            }
            if ((ulong)param_2[4] <= (ulong)*puVar3) {
              return 0;
            }
            uVar9 = (ulong)*puVar3 + 4;
            if (uVar8 - 1 < uVar9 + uVar10) {
              return 0;
            }
            if (uVar8 <= uVar9) {
              return 0;
            }
            if (uVar8 - uVar9 < uVar10) {
              return 0;
            }
            if (*(char *)(lVar7 + uVar9 + uVar10) != '\0') {
              return 0;
            }
          }
        }
        *(int *)(param_2 + 7) = (int)lVar6;
        return 1;
      }
    }
  }
  return 0;
}

~~~
