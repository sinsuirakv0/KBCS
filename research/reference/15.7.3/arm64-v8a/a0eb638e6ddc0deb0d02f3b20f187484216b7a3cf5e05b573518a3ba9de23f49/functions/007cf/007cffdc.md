# 007cffdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "007cffdc",
  "name": "FUN_007cffdc",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4486bdce8a96cfb25cfb89da48a68ff2b199baccd2a992a51b987b6b41eda3c",
  "source_text_sha256": "f4486bdce8a96cfb25cfb89da48a68ff2b199baccd2a992a51b987b6b41eda3c"
}
~~~

## 呼び出し元

- [007cffa8](../007cf/007cffa8.md)
- [007d0be0](../007d0/007d0be0.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0081f580](../0081f/0081f580.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb1f0](../00bdb/00bdb1f0.md)

## 疑似コード / UTF-8 1817 bytes

~~~c

bool FUN_007cffdc(int param_1,int param_2)

{
  long lVar1;
  byte *pbVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  
  if (param_1 == -10) {
    return true;
  }
  lVar1 = FUN_0081f580();
  pbVar3 = *(byte **)(BYTE_ARRAY_003975f1 + lVar1 + 0x17);
  if (*(byte **)(BYTE_ARRAY_003975f1 + lVar1 + 0x17) == (byte *)0x0) {
    pbVar4 = BYTE_ARRAY_003975f1 + lVar1 + 0x17;
    pbVar5 = BYTE_ARRAY_003975f1 + lVar1 + 0x17;
  }
  else {
    do {
      while (pbVar2 = pbVar3, pbVar4 = pbVar2, *(int *)(pbVar2 + 0x1c) <= param_1) {
        if (param_1 <= *(int *)(pbVar2 + 0x1c)) goto LAB_007d00ac;
        pbVar3 = *(byte **)(pbVar2 + 8);
        if (*(byte **)(pbVar2 + 8) == (byte *)0x0) {
          pbVar5 = pbVar2 + 8;
          goto LAB_007d0050;
        }
      }
      pbVar3 = *(byte **)pbVar2;
      pbVar5 = pbVar2;
    } while (*(byte **)pbVar2 != (byte *)0x0);
  }
LAB_007d0050:
  pbVar2 = (byte *)_Znwm(0x1f60);
  *(int *)(pbVar2 + 0x1c) = param_1;
  memset(pbVar2 + 0x20,0,8000);
  pbVar2[0] = 0;
  pbVar2[1] = 0;
  pbVar2[2] = 0;
  pbVar2[3] = 0;
  pbVar2[4] = 0;
  pbVar2[5] = 0;
  pbVar2[6] = 0;
  pbVar2[7] = 0;
  pbVar2[8] = 0;
  pbVar2[9] = 0;
  pbVar2[10] = 0;
  pbVar2[0xb] = 0;
  pbVar2[0xc] = 0;
  pbVar2[0xd] = 0;
  pbVar2[0xe] = 0;
  pbVar2[0xf] = 0;
  *(byte **)(pbVar2 + 0x10) = pbVar4;
  *(byte **)pbVar5 = pbVar2;
  pbVar3 = pbVar2;
  if (**(long **)(BYTE_ARRAY_003975f1 + lVar1 + 0xf) != 0) {
    *(long *)(BYTE_ARRAY_003975f1 + lVar1 + 0xf) = **(long **)(BYTE_ARRAY_003975f1 + lVar1 + 0xf);
    pbVar3 = *(byte **)pbVar5;
  }
  FUN_00419064(*(undefined8 *)(BYTE_ARRAY_003975f1 + lVar1 + 0x17),pbVar3);
  *(long *)(BYTE_ARRAY_003975f1 + lVar1 + 0x1f) = *(long *)(BYTE_ARRAY_003975f1 + lVar1 + 0x1f) + 1;
LAB_007d00ac:
  return *(int *)(pbVar2 + (long)param_2 * 0x10 + 0x2c) != 0;
}

~~~
