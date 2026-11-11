# 004baacc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "004baacc",
  "name": "_ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4_",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "88b3979b8c5ba87de1ff380792f19eceeca082f7b5a365ffc458e27a42bf22b0",
  "source_text_sha256": "88b3979b8c5ba87de1ff380792f19eceeca082f7b5a365ffc458e27a42bf22b0"
}
~~~

## 呼び出し元

- [00c58d00](../00c58/00c58d00.md)

## 呼び出し先

- [00c58b20](../00c58/00c58b20.md)
- [00c58cf0](../00c58/00c58cf0.md)

## 疑似コード / UTF-8 1330 bytes

~~~c

void _ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4_
               (undefined8 *param_1,undefined8 param_2,undefined8 param_3,long *param_4)

{
  long lVar1;
  int iVar2;
  uint uVar3;
  ulong uVar4;
  ulong uVar5;
  long lVar6;
  
  lVar6 = *param_4;
  lVar1 = param_4[1];
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  uVar4 = lVar1 - lVar6 >> 2;
  *(undefined4 *)(param_1 + 3) = 1;
  uVar5 = uVar4;
  if (lVar1 - lVar6 == 0) {
LAB_004bab34:
    if (uVar5 == 0) {
      lVar6 = 0;
    }
    else {
      uVar5 = uVar5 - 1;
      if (uVar5 < uVar4) {
        uVar3 = *(uint *)(lVar6 + uVar5 * 4);
      }
      else {
        uVar3 = 0;
      }
      lVar6 = 0x20;
      do {
        if ((uVar3 >> (ulong)((int)lVar6 - 1U & 0x1f) & 1) != 0) break;
        lVar6 = lVar6 + -1;
      } while (lVar6 != 0);
      lVar6 = lVar6 + uVar5 * 0x20;
    }
  }
  else {
    do {
      if (*(int *)(lVar6 + -4 + uVar5 * 4) != 0) goto LAB_004bab34;
      uVar5 = uVar5 - 1;
    } while (uVar5 != 0);
    lVar6 = 0;
  }
  do {
    do {
      _ZN5Botan6BigInt9randomizeERNS_21RandomNumberGeneratorEmb(param_1,param_2,lVar6,0);
      iVar2 = _ZNK5Botan6BigInt3cmpERKS0_b(param_1,param_3,1);
    } while (iVar2 < 0);
    iVar2 = _ZNK5Botan6BigInt3cmpERKS0_b(param_1,param_4,1);
  } while (-1 < iVar2);
  return;
}

~~~
