# 00bfda8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfda8c",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "696d3ad6676e0f0528d26a011671b2ce4fafb22e2519b18da9c04409b7dc3d8e",
  "source_text_sha256": "696d3ad6676e0f0528d26a011671b2ce4fafb22e2519b18da9c04409b7dc3d8e"
}
~~~

## 呼び出し元

- [00c5e380](../00c5e/00c5e380.md)

## 呼び出し先

- [00c582a0](../00c58/00c582a0.md)
- [00c59dd0](../00c59/00c59dd0.md)

## 疑似コード / UTF-8 1699 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc
                 (long *param_1,long *param_2,uint param_3)

{
  long lVar1;
  uint uVar2;
  undefined1 *puVar3;
  uint uVar4;
  int iVar5;
  long *plVar6;
  char local_24 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_24,param_1,1);
  if (local_24[0] != '\0') {
    while( true ) {
      plVar6 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      if ((byte *)plVar6[3] == (byte *)plVar6[4]) {
        uVar4 = (**(code **)(*plVar6 + 0x48))();
        if (uVar4 == 0xffffffff) {
          uVar4 = 2;
          goto LAB_00bfdba8;
        }
      }
      else {
        uVar4 = (uint)*(byte *)plVar6[3];
      }
      if ((uVar4 & 0xff) == (param_3 & 0xff)) break;
      puVar3 = (undefined1 *)param_2[6];
      if (puVar3 == (undefined1 *)param_2[7]) {
        iVar5 = (**(code **)(*param_2 + 0x68))(param_2,uVar4 & 0xff);
        if (iVar5 == -1) break;
      }
      else {
        param_2[6] = (long)(puVar3 + 1);
        *puVar3 = (char)uVar4;
      }
      if (param_1[1] != 0x7fffffffffffffff) {
        param_1[1] = param_1[1] + 1;
      }
      plVar6 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      if (plVar6[3] == plVar6[4]) {
        (**(code **)(*plVar6 + 0x50))();
      }
      else {
        plVar6[3] = plVar6[3] + 1;
      }
    }
    uVar4 = 0;
LAB_00bfdba8:
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar2 = uVar4 | 4;
    if (param_1[1] != 0) {
      uVar2 = uVar4;
    }
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | uVar2);
  }
  return param_1;
}

~~~
