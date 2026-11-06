# 00babe6c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00babe6c",
  "name": "FUN_00babe6c",
  "size": 604,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dee472cc8c24a181099fe882dffa869bb9e1962557bf517244acbfdfb6138c43",
  "source_text_sha256": "dee472cc8c24a181099fe882dffa869bb9e1962557bf517244acbfdfb6138c43"
}
~~~

## 呼び出し元

- [00babe04](../00bab/00babe04.md)
- [00bac640](../00bac/00bac640.md)
- [00baecc4](../00bae/00baecc4.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 3700 bytes

~~~c

undefined8
FUN_00babe6c(long param_1,ushort *param_2,long *param_3,undefined1 *param_4,long param_5,
            long *param_6,ulong param_7,uint param_8)

{
  uint uVar1;
  ushort uVar2;
  ushort uVar3;
  undefined1 *puVar4;
  uint uVar5;
  ushort *puVar6;
  byte *pbVar7;
  byte bVar8;
  
  *param_3 = param_1;
  *param_6 = (long)param_4;
  if ((param_8 >> 1 & 1) != 0) {
    if (param_5 - (long)param_4 < 3) {
      return 1;
    }
    *param_6 = (long)(param_4 + 1);
    *param_4 = 0xef;
    puVar4 = (undefined1 *)*param_6;
    *param_6 = (long)(puVar4 + 1);
    *puVar4 = 0xbb;
    puVar4 = (undefined1 *)*param_6;
    *param_6 = (long)(puVar4 + 1);
    *puVar4 = 0xbf;
  }
  puVar6 = (ushort *)*param_3;
  do {
    if (param_2 <= puVar6) {
      return 0;
    }
    uVar2 = *puVar6;
    if (param_7 < uVar2) {
      return 2;
    }
    uVar5 = (uint)uVar2;
    if (uVar2 < 0x80) {
      pbVar7 = (byte *)*param_6;
      if (param_5 - (long)pbVar7 < 1) {
        return 1;
      }
      *param_6 = (long)(pbVar7 + 1);
      *pbVar7 = (byte)uVar2;
    }
    else {
      if (uVar2 < 0x800) {
        pbVar7 = (byte *)*param_6;
        if (param_5 - (long)pbVar7 < 2) {
          return 1;
        }
        *param_6 = (long)(pbVar7 + 1);
        bVar8 = (byte)(uVar2 >> 6) | 0xc0;
      }
      else {
        bVar8 = (byte)(uVar2 >> 8);
        if (uVar2 >> 0xb < 0x1b) {
          pbVar7 = (byte *)*param_6;
          if (param_5 - (long)pbVar7 < 3) {
            return 1;
          }
          *param_6 = (long)(pbVar7 + 1);
          *pbVar7 = bVar8 >> 4 | 0xe0;
          pbVar7 = (byte *)*param_6;
          bVar8 = (byte)(uVar2 >> 6) & 0x3f | 0x80;
        }
        else {
          if (uVar2 >> 10 < 0x37) {
            if ((long)param_2 - (long)puVar6 < 4) {
              return 1;
            }
            uVar3 = puVar6[1];
            if ((uVar3 & 0xfc00) != 0xdc00) {
              return 2;
            }
            if (param_5 - *param_6 < 4) {
              return 1;
            }
                    /* try { // try from 00bac018 to 00cac033 has its CatchHandler @ 00bac348 */
            if (param_7 < ((ulong)uVar3 & 0x3ff | ((ulong)uVar5 & 0x3ff) << 10) + 0x10000) {
              return 2;
            }
            *param_3 = (long)(puVar6 + 1);
            pbVar7 = (byte *)*param_6;
            uVar1 = (uVar2 >> 6 & 0xf) + 1;
                    /* try { // try from 00bac034 to 00cac1df has its CatchHandler @ 00babe48 */
            *param_6 = (long)(pbVar7 + 1);
            *pbVar7 = (byte)(uVar1 >> 2) | 0xf0;
            pbVar7 = (byte *)*param_6;
            *param_6 = (long)(pbVar7 + 1);
            *pbVar7 = (byte)((uVar1 & 3) << 4) | (byte)(uVar2 >> 2) & 0xf | 0x80;
            pbVar7 = (byte *)*param_6;
            *param_6 = (long)(pbVar7 + 1);
            *pbVar7 = (byte)((uVar5 & 3) << 4) | (byte)(uVar3 >> 6) & 0xf | 0x80;
            pbVar7 = (byte *)*param_6;
            *param_6 = (long)(pbVar7 + 1);
            *pbVar7 = (byte)uVar3 & 0x3f | 0x80;
            goto LAB_00babf20;
          }
          if (uVar5 < 0xe000) {
            return 2;
          }
          pbVar7 = (byte *)*param_6;
          if (param_5 - (long)pbVar7 < 3) {
            return 1;
          }
          *param_6 = (long)(pbVar7 + 1);
          *pbVar7 = bVar8 >> 4 | 0xe0;
          pbVar7 = (byte *)*param_6;
          bVar8 = (byte)(uVar2 >> 6) & 0xbf;
        }
        *param_6 = (long)(pbVar7 + 1);
      }
      *pbVar7 = bVar8;
      pbVar7 = (byte *)*param_6;
      *param_6 = (long)(pbVar7 + 1);
      *pbVar7 = (byte)uVar2 & 0x3f | 0x80;
    }
LAB_00babf20:
    puVar6 = (ushort *)(*param_3 + 2);
    *param_3 = (long)puVar6;
  } while( true );
}

~~~
