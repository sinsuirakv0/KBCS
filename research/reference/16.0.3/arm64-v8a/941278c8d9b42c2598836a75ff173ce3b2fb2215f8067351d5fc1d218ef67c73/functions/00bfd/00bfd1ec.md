# 00bfd1ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfd1ec",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4swapERS3_",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4b68eee8f3c74fc533c83aa741097ea1b752e6b6fc9d5593330ebdd7be7987cb",
  "source_text_sha256": "4b68eee8f3c74fc533c83aa741097ea1b752e6b6fc9d5593330ebdd7be7987cb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5f3c0](../00c5f/00c5f3c0.md)

## 疑似コード / UTF-8 791 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4swapERS3_(long *param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  long lVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  undefined8 uVar6;
  
  lVar1 = *param_2;
  lVar2 = *param_1;
  lVar3 = param_1[1];
  param_1[1] = param_2[1];
  param_2[1] = lVar3;
  lVar2 = (long)param_1 + *(long *)(lVar2 + -0x18);
  lVar1 = (long)param_2 + *(long *)(lVar1 + -0x18);
  _ZNSt6__ndk18ios_base4swapERS0_(lVar2,lVar1);
  uVar6 = *(undefined8 *)(lVar2 + 0x88);
  uVar4 = *(undefined4 *)(lVar1 + 0x90);
  *(undefined8 *)(lVar2 + 0x88) = *(undefined8 *)(lVar1 + 0x88);
  uVar5 = *(undefined4 *)(lVar2 + 0x90);
  *(undefined8 *)(lVar1 + 0x88) = uVar6;
  *(undefined4 *)(lVar2 + 0x90) = uVar4;
  *(undefined4 *)(lVar1 + 0x90) = uVar5;
  return;
}

~~~
