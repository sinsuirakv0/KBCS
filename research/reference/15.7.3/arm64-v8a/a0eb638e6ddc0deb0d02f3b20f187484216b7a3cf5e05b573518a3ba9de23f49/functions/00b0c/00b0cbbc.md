# 00b0cbbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b0caf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0caf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0064.md#compare-c84b996e31f6db5c896c181e2811a959)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0cbbc",
  "name": "_ZNK8firebase3fbs10AdsService6VerifyERN11flatbuffers8VerifierE",
  "size": 832,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "87f050f7c5abffe1e4d9d7a450474fb5d5d6672cb7dee50a41043ec1b2a86f19",
  "source_text_sha256": "87f050f7c5abffe1e4d9d7a450474fb5d5d6672cb7dee50a41043ec1b2a86f19"
}
~~~

## 呼び出し元

- [00bdea50](../00bde/00bdea50.md)

## 呼び出し先

- [00bdeab0](../00bde/00bdeab0.md)

## 疑似コード / UTF-8 7735 bytes

~~~c

undefined4
_ZNK8firebase3fbs10AdsService6VerifyERN11flatbuffers8VerifierE(int *param_1,long *param_2)

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
  
                    /* try { // try from 00b0cbc0 to 00c0cbcb has its CatchHandler @ 00b0cc40 */
  lVar7 = *param_2;
  uVar9 = (long)param_1 - lVar7;
                    /* try { // try from 00b0cbdc to 00c0cbe7 has its CatchHandler @ 00b0cc3c */
  if (((uVar9 & 3) == 0) || ((char)param_2[5] == '\0')) {
    uVar8 = param_2[1];
    if (uVar8 < 5) {
      return 0;
    }
    uVar10 = uVar8 - 4;
                    /* try { // try from 00b0cbf8 to 00c0cc03 has its CatchHandler @ 00b0cc38 */
    if (uVar10 < uVar9) {
      return 0;
    }
                    /* try { // try from 00b0cc04 to 00c0cc6f has its CatchHandler @ 00b0cb5c */
    iVar5 = *param_1;
    uVar6 = (int)param_2[2] + 1;
    uVar1 = (int)param_2[3] + 1;
    *(uint *)(param_2 + 2) = uVar6;
    *(uint *)(param_2 + 3) = uVar1;
                    /* catch() { ... } // from try @ 00b0cbf8 with catch @ 00b0cc38 */
                    /* catch() { ... } // from try @ 00b0cbdc with catch @ 00b0cc3c */
                    /* catch() { ... } // from try @ 00b0cbc0 with catch @ 00b0cc40 */
                    /* catch() { ... } // from try @ 00b0cba4 with catch @ 00b0cc44 */
                    /* catch() { ... } // from try @ 00b0cb98 with catch @ 00b0cc48 */
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
        if (((ulong)puVar12[2] != 0) && (uVar10 < uVar9 + puVar12[2])) {
          return 0;
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
          if (((ulong)puVar12[3] != 0) &&
             (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[3]),
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
          if (8 < uVar4) {
            if ((ulong)puVar12[4] != 0) {
              uVar11 = uVar9 + puVar12[4];
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
              if ((int)*(uint *)(lVar7 + uVar11) < 1) {
                return 0;
              }
              if (uVar8 - 1 < uVar11 + *(uint *)(lVar7 + uVar11)) {
                return 0;
              }
            }
                    /* try { // try from 00b0cdf4 to 00c0ce5f has its CatchHandler @ 00b0cdf4
                       catch() { ... } // from try @ 00b0cdf4 with catch @ 00b0cdf4
                       catch() { ... } // from try @ 00b0ce68 with catch @ 00b0cdf4
                       catch() { ... } // from try @ 00b0cfa4 with catch @ 00b0cdf4 */
            if (((ulong)puVar12[4] != 0) &&
               (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[4]),
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
              if (uVar8 <= uVar2) {
                return 0;
              }
                    /* try { // try from 00b0ce60 to 00c0ce67 has its CatchHandler @ 00b0cfb8 */
              if (uVar8 - uVar2 < uVar11) {
                return 0;
              }
                    /* try { // try from 00b0ce68 to 00c0ce97 has its CatchHandler @ 00b0cdf4 */
              if (*(char *)(lVar7 + uVar2 + uVar11) != '\0') {
                return 0;
              }
            }
            if (10 < uVar4) {
              if ((ulong)puVar12[5] != 0) {
                uVar9 = uVar9 + puVar12[5];
                if ((uVar9 & 3) == 0) {
                  if (uVar10 < uVar9) {
                    return 0;
                  }
                }
                else {
                  if ((char)param_2[5] != '\0') {
                    return 0;
                  }
                    /* try { // try from 00b0ce98 to 00c0cea3 has its CatchHandler @ 00b0cfac */
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
                    /* try { // try from 00b0ced8 to 00c0cedf has its CatchHandler @ 00b0cfa8 */
              if (((ulong)puVar12[5] != 0) &&
                 (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[5]),
                 lVar7 = (long)puVar3 + (ulong)*puVar3, lVar7 != 0)) {
                uVar9 = _ZNK8firebase3fbs16AnalyticsService6VerifyERN11flatbuffers8VerifierE
                                  (lVar7,param_2);
                if ((uVar9 & 1) == 0) {
                  return 0;
                }
                uVar6 = *(uint *)(param_2 + 2);
              }
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
