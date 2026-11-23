# 00bc0efc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bc0ad4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0ad4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/detail_skipped-0006.md#compare-4c06989bf9d2edf657d95fefee03c962)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/detail_skipped-0008.md#compare-07fcf3a2b9881a183886a16bcb598775)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc0efc",
  "name": "_ZNK3com6google8firebase9messaging3cpp32SerializedUnregistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4685ce8c4df36508f5dbe0aac2106c4bcdb50ce94e81fa9555b1ff8909b90872",
  "source_text_sha256": "4685ce8c4df36508f5dbe0aac2106c4bcdb50ce94e81fa9555b1ff8909b90872"
}
~~~

## 呼び出し元

- [00c5d520](../00c5d/00c5d520.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 3125 bytes

~~~c

undefined4
_ZNK3com6google8firebase9messaging3cpp32SerializedUnregistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
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
