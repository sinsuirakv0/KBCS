# 00bfe6bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfe6bc",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEv",
  "size": 196,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5de0382271c7a8fb7241d6abc2f5a2681149235814834513e200ad9378db4cea",
  "source_text_sha256": "5de0382271c7a8fb7241d6abc2f5a2681149235814834513e200ad9378db4cea"
}
~~~

## 呼び出し元

- [00c5f400](../00c5f/00c5f400.md)

## 呼び出し先

- [00c59340](../00c59/00c59340.md)
- [00c5ae70](../00c5a/00c5ae70.md)

## 疑似コード / UTF-8 879 bytes

~~~c

uint _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEv(long *param_1)

{
  long lVar1;
  byte *pbVar2;
  long *plVar3;
  uint uVar4;
  uint uVar5;
  char local_24 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_24,param_1,1);
  if (local_24[0] == '\0') {
    return 0xffffffff;
  }
  plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
  pbVar2 = (byte *)plVar3[3];
  if (pbVar2 == (byte *)plVar3[4]) {
    uVar5 = (**(code **)(*plVar3 + 0x50))();
    if (uVar5 == 0xffffffff) {
      uVar4 = 6;
      goto LAB_00bfe748;
    }
  }
  else {
    plVar3[3] = (long)(pbVar2 + 1);
    uVar5 = (uint)*pbVar2;
  }
  uVar4 = 0;
  param_1[1] = 1;
LAB_00bfe748:
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | uVar4);
  return uVar5;
}

~~~
