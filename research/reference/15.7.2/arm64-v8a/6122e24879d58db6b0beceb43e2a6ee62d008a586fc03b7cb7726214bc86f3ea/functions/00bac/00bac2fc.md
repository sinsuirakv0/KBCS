# 00bac2fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bac2fc.md)

## 関数情報

~~~json
{
  "address": "00bac2fc",
  "name": "FUN_00bac2fc",
  "size": 512,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4f23e192e96f69400939feaf42dd776c23e6d4e1d46a4ac1f0f98852127b3ee0",
  "source_text_sha256": "4f23e192e96f69400939feaf42dd776c23e6d4e1d46a4ac1f0f98852127b3ee0"
}
~~~
## 呼び出し元

- [00bac2e0](../00bac/00bac2e0.md)
- [00bac62c](../00bac/00bac62c.md)
- [00baeb7c](../00bae/00baeb7c.md)
- [00baecc0](../00bae/00baecc0.md)
- [00baee04](../00bae/00baee04.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 2638 bytes

~~~c

int FUN_00bac2fc(byte *param_1,byte *param_2,ulong param_3,ulong param_4,uint param_5)

{
  long lVar1;
  byte bVar2;
  byte bVar3;
  byte *pbVar4;
  ulong uVar5;
  uint uVar6;
  uint uVar7;
  uint uVar8;
  byte bVar9;
  
  pbVar4 = param_1;
  if ((((2 < (long)param_2 - (long)param_1) && ((param_5 >> 2 & 1) != 0)) && (*param_1 == 0xef)) &&
     (param_1[1] == 0xbb)) {
    lVar1 = 3;
    if (param_1[2] != 0xbf) {
      lVar1 = 0;
    }
    pbVar4 = param_1 + lVar1;
  }
  if ((pbVar4 < param_2) && (param_3 != 0)) {
    uVar5 = 0;
    while( true ) {
      bVar2 = *pbVar4;
      if (param_4 < bVar2) break;
      if ((char)bVar2 < '\0') {
        if (bVar2 < 0xc2) break;
        uVar6 = (uint)bVar2;
        if (bVar2 < 0xe0) {
          if ((((long)param_2 - (long)pbVar4 < 2) || ((pbVar4[1] & 0xc0) != 0x80)) ||
             (param_4 < (pbVar4[1] & 0x3f | (uVar6 & 0x1f) << 6))) break;
          pbVar4 = pbVar4 + 2;
        }
        else if (bVar2 < 0xf0) {
          if ((long)param_2 - (long)pbVar4 < 3) break;
          uVar7 = (uint)pbVar4[1];
          if (uVar6 == 0xed) {
            uVar8 = uVar7 & 0xe0;
LAB_00bac45c:
            if (uVar8 != 0x80) break;
          }
          else {
            if (uVar6 != 0xe0) {
              uVar8 = uVar7 & 0xc0;
              goto LAB_00bac45c;
            }
            if ((uVar7 & 0xe0) != 0xa0) break;
          }
          if (((pbVar4[2] & 0xc0) != 0x80) ||
             (param_4 < ((uVar6 & 0xf) << 0xc | (uVar7 & 0x3f) << 6 | pbVar4[2] & 0x3f))) break;
          pbVar4 = pbVar4 + 3;
        }
        else {
          if (((0xf4 < uVar6) || ((long)param_2 - (long)pbVar4 < 4)) || (param_3 - uVar5 < 2))
          break;
          bVar3 = pbVar4[1];
          if (uVar6 == 0xf4) {
            bVar9 = bVar3 & 0xf0;
LAB_00bac4a0:
            if (bVar9 != 0x80) break;
          }
          else {
            if (uVar6 != 0xf0) {
              bVar9 = bVar3 & 0xc0;
              goto LAB_00bac4a0;
            }
            if (0x2f < bVar3 - 0x90) break;
          }
          if ((((pbVar4[2] & 0xc0) != 0x80) || ((pbVar4[3] & 0xc0) != 0x80)) ||
             (param_4 < (((ulong)bVar2 & 7) << 0x12 | ((ulong)bVar3 & 0x3f) << 0xc |
                         ((ulong)pbVar4[2] & 0x3f) << 6 | (ulong)pbVar4[3] & 0x3f))) break;
          uVar5 = uVar5 + 1;
          pbVar4 = pbVar4 + 4;
        }
      }
      else {
        pbVar4 = pbVar4 + 1;
      }
      if ((param_2 <= pbVar4) || (uVar5 = uVar5 + 1, param_3 <= uVar5)) break;
    }
  }
  return (int)pbVar4 - (int)param_1;
}

~~~
