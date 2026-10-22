# 00ab1cbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ab1cbc.md)

## 関数情報

~~~json
{
  "address": "00ab1cbc",
  "name": "FUN_00ab1cbc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "491f271e1d73ddf00f7cdbd798fa87272a0fa0aae0e2992649cb578a3c9d5777",
  "source_text_sha256": "491f271e1d73ddf00f7cdbd798fa87272a0fa0aae0e2992649cb578a3c9d5777"
}
~~~
## 呼び出し元

- [00596128](../00596/00596128.md)

## 呼び出し先

- [0041be0c](../0041b/0041be0c.md)
- [0041cddc](../0041c/0041cddc.md)
- [0044df7c](../0044d/0044df7c.md)
- [0044e05c](../0044e/0044e05c.md)
- [009d8a60](../009d8/009d8a60.md)
- [009dafc4](../009da/009dafc4.md)
- [009dafd0](../009da/009dafd0.md)

## 疑似コード 1/1 / UTF-8 1103 bytes

~~~c

void FUN_00ab1cbc(long param_1)

{
  undefined *puVar1;
  ulong uVar2;
  long *plVar3;
  byte bVar4;
  undefined *puVar5;
  undefined8 uVar6;
  undefined4 uVar7;
  long lVar8;
  
  FUN_009dafc4(param_1 + 0x397700);
  FUN_009d8a60();
  FUN_009dafd0();
  FUN_0041be0c();
  FUN_0041cddc();
  puVar5 = PTR_DAT_00c1b710;
  lVar8 = 0;
  do {
    puVar1 = puVar5 + lVar8;
    bVar4 = puVar1[0x18];
    uVar2 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar2 = *(ulong *)(puVar1 + 0x20);
    }
    if (uVar2 == 0x13) {
      plVar3 = (long *)(puVar1 + 0x19);
      if ((bVar4 & 1) != 0) {
        plVar3 = *(long **)(puVar1 + 0x28);
      }
      if ((*plVar3 != 0x7461446567616d49 || plVar3[1] != 0x702e6c61636f4c61) ||
          *(long *)((long)plVar3 + 0xb) != 0x6b6361702e6c6163) goto LAB_00ab1d30;
      uVar7 = 1;
    }
    else {
LAB_00ab1d30:
      uVar7 = 0;
    }
    uVar6 = FUN_0044df7c();
    FUN_0044e05c(uVar6,puVar1,puVar1 + 0x18,uVar7);
    lVar8 = lVar8 + 0x30;
    if (lVar8 == 0x150) {
      return;
    }
  } while( true );
}

~~~
