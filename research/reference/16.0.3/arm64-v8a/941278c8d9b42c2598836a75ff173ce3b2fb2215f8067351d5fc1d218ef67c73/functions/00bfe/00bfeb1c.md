# 00bfeb1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfeb1c",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "75fa039ae1fab26d146a1f6283555b1af5e8f93b24ab2e8825805856c648d1d3",
  "source_text_sha256": "75fa039ae1fab26d146a1f6283555b1af5e8f93b24ab2e8825805856c648d1d3"
}
~~~

## 呼び出し元

- [00c5f420](../00c5f/00c5f420.md)

## 呼び出し先

- [00c59340](../00c59/00c59340.md)
- [00c5ae70](../00c5a/00c5ae70.md)

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
          goto LAB_00bfec38;
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
LAB_00bfec38:
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
