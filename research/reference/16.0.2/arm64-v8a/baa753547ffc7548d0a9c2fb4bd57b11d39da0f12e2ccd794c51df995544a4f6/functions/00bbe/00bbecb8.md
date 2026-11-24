# 00bbecb8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbec1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbec1c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0080.md#compare-eb028551d2f0c83cc08a3a0d2f1fdcf5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/high-0010.md#compare-955fbef8b7d91e1e95b79c9b3b3b8a34)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbecb8",
  "name": "_ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "343ae5b253d53c4cf5f9a7b9773dbf3a64f4d70350feb75408f1e6585a902ebd",
  "source_text_sha256": "343ae5b253d53c4cf5f9a7b9773dbf3a64f4d70350feb75408f1e6585a902ebd"
}
~~~

## 呼び出し元

- [00c5d5a0](../00c5d/00c5d5a0.md)

## 呼び出し先

- [00c5d5b0](../00c5d/00c5d5b0.md)
- [00c5d5d0](../00c5d/00c5d5d0.md)
- [00c5d5e0](../00c5d/00c5d5e0.md)
- [00c5d5f0](../00c5d/00c5d5f0.md)

## 疑似コード / UTF-8 4399 bytes

~~~c

undefined4
_ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
          (int *param_1,long *param_2)

{
  uint uVar1;
  uint uVar2;
  uint *puVar3;
  ushort uVar4;
  int iVar5;
  long lVar6;
  ulong uVar7;
  ulong uVar8;
  ulong uVar9;
  ulong uVar10;
  ushort *puVar11;
  
  lVar6 = *param_2;
  uVar8 = (long)param_1 - lVar6;
                    /* try { // try from 00bbecdc to 00cbecf7 has its CatchHandler @ 00bbf420 */
  if (((uVar8 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar7 = param_2[1];
    if (uVar7 < 5) {
      return 0;
    }
    uVar9 = uVar7 - 4;
                    /* try { // try from 00bbecf8 to 00cbeda3 has its CatchHandler @ 00bbe868 */
    if (uVar9 < uVar8) {
      return 0;
    }
    iVar5 = *param_1;
    uVar1 = (int)param_2[7] + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
    if ((((uVar1 <= *(uint *)(param_2 + 2)) && (uVar2 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar10 = uVar8 - (long)iVar5, (uVar10 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
       (uVar10 <= uVar7 - 2)) {
      uVar4 = *(ushort *)(lVar6 + uVar10);
      if ((((uVar4 & 1) == 0) || ((char)param_2[3] == '\0')) && ((uVar4 & 1) == 0)) {
        if (uVar7 <= uVar4) {
          return 0;
        }
        if (uVar7 - uVar4 < uVar10) {
          return 0;
        }
        puVar11 = (ushort *)((long)param_1 - (long)*param_1);
        if (4 < *puVar11) {
          if (((ulong)puVar11[2] != 0) && (uVar7 - 1 < uVar8 + puVar11[2])) {
            return 0;
          }
          if (*puVar11 < 7) {
            lVar6 = 0;
            uVar4 = puVar11[2];
          }
          else {
            if ((ulong)puVar11[3] != 0) {
              uVar8 = uVar8 + puVar11[3];
                    /* try { // try from 00bbedc0 to 00cbf163 has its CatchHandler @ 00bbe868 */
              if ((uVar8 & 3) == 0) {
                if (uVar9 < uVar8) {
                  return 0;
                }
              }
              else {
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar9 < uVar8) {
                  return 0;
                }
              }
              if ((int)*(uint *)(lVar6 + uVar8) < 1) {
                return 0;
              }
              if (uVar7 - 1 < uVar8 + *(uint *)(lVar6 + uVar8)) {
                return 0;
              }
            }
            lVar6 = 0;
            if ((ulong)puVar11[3] != 0) {
              puVar3 = (uint *)((long)param_1 + (ulong)puVar11[3]);
              lVar6 = (long)puVar3 + (ulong)*puVar3;
            }
            uVar4 = puVar11[2];
          }
          if ((ulong)uVar4 != 0) {
            switch(*(undefined1 *)((long)param_1 + (ulong)uVar4)) {
            case 1:
              if (lVar6 == 0) goto switchD_00bbee54_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 2:
              if (lVar6 == 0) goto switchD_00bbee54_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp23SerializedTokenReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 3:
              if (lVar6 == 0) goto switchD_00bbee54_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp30SerializedRegistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 4:
              if (lVar6 == 0) goto switchD_00bbee54_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp32SerializedUnregistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            default:
              goto switchD_00bbee54_default;
            }
            if ((uVar8 & 1) == 0) {
              return 0;
            }
          }
        }
switchD_00bbee54_default:
        *(int *)(param_2 + 7) = (int)param_2[7] + -1;
        return 1;
      }
    }
  }
                    /* try { // try from 00bbeda4 to 00cbedbf has its CatchHandler @ 00bbf428 */
  return 0;
}

~~~
