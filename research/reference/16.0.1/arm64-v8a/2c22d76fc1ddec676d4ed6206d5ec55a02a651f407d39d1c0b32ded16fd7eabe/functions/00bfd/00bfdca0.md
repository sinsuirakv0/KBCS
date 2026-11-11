# 00bfdca0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfdca0",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5ad19d36ac03fc6dacd11d2b0f0d953df77c81c6465359db2821dd90fb4bca36",
  "source_text_sha256": "5ad19d36ac03fc6dacd11d2b0f0d953df77c81c6465359db2821dd90fb4bca36"
}
~~~

## 呼び出し元

- [00c5e390](../00c5e/00c5e390.md)

## 呼び出し先

- [00c582a0](../00c58/00c582a0.md)
- [00c59dd0](../00c59/00c59dd0.md)

## 疑似コード / UTF-8 2043 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc
                 (long *param_1,undefined1 *param_2,long param_3,uint param_4)

{
  uint uVar1;
  long *plVar2;
  uint uVar3;
  long lVar4;
  undefined1 *puVar5;
  byte local_54 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_54,param_1,1);
  uVar3 = (uint)local_54[0];
  if (local_54[0] != 0) {
    while( true ) {
      plVar2 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      if ((byte *)plVar2[3] == (byte *)plVar2[4]) {
        uVar3 = (**(code **)(*plVar2 + 0x48))();
        if (uVar3 == 0xffffffff) {
          uVar3 = 2;
          goto joined_r0x00bfde0c;
        }
      }
      else {
        uVar3 = (uint)*(byte *)plVar2[3];
      }
      if ((uVar3 & 0xff) == (param_4 & 0xff)) {
        plVar2 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
        if (plVar2[3] == plVar2[4]) {
          (**(code **)(*plVar2 + 0x50))();
        }
        else {
          plVar2[3] = plVar2[3] + 1;
        }
        if (param_1[1] == 0x7fffffffffffffff) {
          uVar3 = 0;
        }
        else {
          uVar3 = 0;
          param_1[1] = param_1[1] + 1;
        }
        goto joined_r0x00bfde0c;
      }
      if (param_3 + -1 <= param_1[1]) break;
      lVar4 = *param_1;
      puVar5 = param_2 + 1;
      *param_2 = (char)uVar3;
      plVar2 = *(long **)((long)param_1 + *(long *)(lVar4 + -0x18) + 0x28);
      if (plVar2[3] == plVar2[4]) {
        (**(code **)(*plVar2 + 0x50))();
      }
      else {
        plVar2[3] = plVar2[3] + 1;
      }
      param_2 = puVar5;
      if (param_1[1] != 0x7fffffffffffffff) {
        param_1[1] = param_1[1] + 1;
      }
    }
    uVar3 = 4;
  }
joined_r0x00bfde0c:
  if (0 < param_3) {
    *param_2 = 0;
  }
  lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
  uVar1 = uVar3 | 4;
  if (param_1[1] != 0) {
    uVar1 = uVar3;
  }
  _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | uVar1);
  return param_1;
}

~~~
