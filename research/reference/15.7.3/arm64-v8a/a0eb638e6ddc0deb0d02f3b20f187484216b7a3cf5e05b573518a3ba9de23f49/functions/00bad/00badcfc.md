# 00badcfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00badcfc",
  "name": "FUN_00badcfc",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9282525f3c49fd2b9ebb86b8086689a76fb41d84f58a83f44a1426f99efc928d",
  "source_text_sha256": "9282525f3c49fd2b9ebb86b8086689a76fb41d84f58a83f44a1426f99efc928d"
}
~~~

## 呼び出し元

- [00badcdc](../00bad/00badcdc.md)
- [00bae64c](../00bae/00bae64c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1182 bytes

~~~c

int FUN_00badcfc(ushort *param_1,long param_2,ulong param_3,ulong param_4,uint param_5)

{
  uint uVar1;
  byte bVar2;
  bool bVar3;
  ushort *puVar4;
  ulong uVar5;
  
  puVar4 = param_1;
  if (((1 < param_2 - (long)param_1) && ((param_5 >> 2 & 1) != 0)) && ((char)*param_1 == -1)) {
    puVar4 = param_1 + (*(char *)((long)param_1 + 1) == -2);
  }
  if ((puVar4 < (ushort *)(param_2 + -1)) && (param_3 != 0)) {
    uVar5 = 1;
    do {
      uVar1 = (uint)*puVar4;
      bVar2 = *(byte *)((long)puVar4 + 1) & 0xfc;
      if (bVar2 == 0xd8) {
                    /* try { // try from 00baddcc to 00cade53 has its CatchHandler @ 00badf38 */
        if (((param_2 - (long)puVar4 < 4) || ((*(byte *)((long)puVar4 + 3) & 0xfc) != 0xdc)) ||
           (param_4 < ((uint)(byte)puVar4[1] | (*(byte *)((long)puVar4 + 3) & 3) << 8 |
                      (uVar1 & 0x3ff) << 10) + 0x10000)) break;
        puVar4 = puVar4 + 2;
      }
      else if ((bVar2 == 0xdc) || (puVar4 = puVar4 + (uVar1 <= param_4), param_4 < uVar1)) break;
      bVar3 = uVar5 < param_3;
      uVar5 = uVar5 + 1;
    } while (puVar4 < (ushort *)(param_2 + -1) && bVar3);
  }
  return (int)puVar4 - (int)param_1;
}

~~~
