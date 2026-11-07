# 00bacaa4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bac998`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac998.md) · [本文差分](../../changes/00bacaa4.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bacaa4",
  "name": "FUN_00bacaa4",
  "size": 580,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95e372287260f5153b2fdf3b92d9c78fdcfe555da8b6f778665da1bb8fc8fda1",
  "source_text_sha256": "95e372287260f5153b2fdf3b92d9c78fdcfe555da8b6f778665da1bb8fc8fda1"
}
~~~

## 呼び出し元

- [00baca3c](../00bac/00baca3c.md)
- [00bad070](../00bad/00bad070.md)
- [00bad198](../00bad/00bad198.md)
- [00bad728](../00bad/00bad728.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 3405 bytes

~~~c

bool FUN_00bacaa4(long param_1,byte *param_2,long *param_3,long param_4,uint *param_5,long *param_6,
                 ulong param_7,uint param_8)

{
  uint uVar1;
  byte bVar2;
  uint *puVar3;
  long lVar4;
  byte *pbVar5;
  uint uVar6;
  uint uVar7;
  uint *puVar8;
  
  *param_3 = param_1;
  *param_6 = param_4;
  pbVar5 = (byte *)*param_3;
  if (((((param_8 >> 2 & 1) != 0) && (2 < (long)param_2 - (long)pbVar5)) && (*pbVar5 == 0xef)) &&
     ((pbVar5[1] == 0xbb && (pbVar5[2] == 0xbf)))) {
    pbVar5 = pbVar5 + 3;
    *param_3 = (long)pbVar5;
  }
  if (param_2 <= pbVar5) {
    return false;
  }
  puVar3 = (uint *)*param_6;
  do {
    puVar8 = puVar3;
    if (param_5 <= puVar8) break;
    bVar2 = *pbVar5;
    uVar6 = (uint)bVar2;
    if ((char)bVar2 < '\0') {
      if (uVar6 < 0xc2) {
        return (bool)2;
      }
      if (uVar6 < 0xe0) {
        if ((long)param_2 - (long)pbVar5 < 2) {
          return true;
        }
        if ((pbVar5[1] & 0xc0) != 0x80) {
          return (bool)2;
        }
        lVar4 = 2;
        uVar6 = pbVar5[1] & 0x3f | (uVar6 & 0x1f) << 6;
        if (param_7 < uVar6) {
          return (bool)2;
        }
      }
      else if (uVar6 < 0xf0) {
        if ((long)param_2 - (long)pbVar5 < 2) {
          return true;
        }
        uVar7 = (uint)pbVar5[1];
        if (uVar6 == 0xed) {
          uVar1 = uVar7 & 0xe0;
joined_r0x00bacc10:
          if (uVar1 != 0x80) {
            return (bool)2;
          }
        }
        else {
          if (uVar6 != 0xe0) {
            uVar1 = uVar7 & 0xc0;
            goto joined_r0x00bacc10;
          }
          if ((uVar7 & 0xe0) != 0xa0) {
            return (bool)2;
          }
        }
        if ((long)param_2 - (long)pbVar5 == 2) {
          return true;
        }
        if (((pbVar5[2] & 0xc0) != 0x80) ||
           (uVar6 = (uVar6 & 0xf) << 0xc | (uVar7 & 0x3f) << 6 | pbVar5[2] & 0x3f, param_7 < uVar6))
        {
          return (bool)2;
        }
        lVar4 = 3;
      }
      else {
        if (0xf4 < uVar6) {
          return (bool)2;
        }
        lVar4 = (long)param_2 - (long)pbVar5;
        if (lVar4 < 2) {
          return true;
        }
        uVar7 = (uint)pbVar5[1];
        if (uVar6 == 0xf4) {
          uVar1 = uVar7 & 0xf0;
joined_r0x00bacc60:
          if (uVar1 != 0x80) {
            return (bool)2;
          }
        }
        else {
          if (uVar6 != 0xf0) {
            uVar1 = uVar7 & 0xc0;
            goto joined_r0x00bacc60;
          }
          if (0x2f < uVar7 - 0x90) {
            return (bool)2;
          }
        }
        if (lVar4 == 2) {
          return true;
        }
        if ((pbVar5[2] & 0xc0) != 0x80) {
          return (bool)2;
        }
        if (lVar4 == 3) {
          return true;
        }
        if ((pbVar5[3] & 0xc0) != 0x80) {
          return (bool)2;
        }
        uVar6 = (uVar6 & 7) << 0x12 | (uVar7 & 0x3f) << 0xc | (pbVar5[2] & 0x3f) << 6 |
                pbVar5[3] & 0x3f;
        if (param_7 < uVar6) {
          return (bool)2;
        }
        lVar4 = 4;
      }
    }
    else {
      if (param_7 < bVar2) {
        return (bool)2;
      }
      lVar4 = 1;
    }
    *puVar8 = uVar6;
    *param_3 = (long)(pbVar5 + lVar4);
    lVar4 = *param_6;
    *param_6 = lVar4 + 4;
    pbVar5 = (byte *)*param_3;
    puVar3 = (uint *)(lVar4 + 4);
  } while (pbVar5 < param_2);
  return param_5 <= puVar8;
}

~~~
