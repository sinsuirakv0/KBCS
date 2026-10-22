# 007cffdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007cffdc.md)

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
  "source_sha256": "8e77143d9d41768c5d85511d7b7d3357ce5bd75aefbf36bb6ef4a1bdc633798b",
  "source_text_sha256": "8e77143d9d41768c5d85511d7b7d3357ce5bd75aefbf36bb6ef4a1bdc633798b"
}
~~~
## 呼び出し元

- [007cffa8](../007cf/007cffa8.md)
- [007d0be0](../007d0/007d0be0.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0081f580](../0081f/0081f580.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdb140](../00bdb/00bdb140.md)

## 疑似コード 1/1 / UTF-8 1882 bytes

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
  pbVar2 = operator_new(0x1f60);
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
