# 004ccabc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "004ccabc",
  "name": "_ZN5Botan17hex_decode_lockedERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97bfba8ffde36ccc779f72a7f8dd159bbac466780f43bf9fc30db48889797a90",
  "source_text_sha256": "97bfba8ffde36ccc779f72a7f8dd159bbac466780f43bf9fc30db48889797a90"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004b3868](../004b3/004b3868.md)
- [0054084c](../00540/0054084c.md)
- [00c59b80](../00c59/00c59b80.md)

## 疑似コード / UTF-8 722 bytes

~~~c

void _ZN5Botan17hex_decode_lockedERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb
               (long *param_1,byte *param_2,undefined4 param_3)

{
  byte *pbVar1;
  ulong uVar2;
  ulong uVar3;
  
  uVar2 = *(ulong *)(param_2 + 8);
  pbVar1 = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    pbVar1 = param_2 + 1;
    uVar2 = (ulong)(*param_2 >> 1);
  }
  FUN_004b3868(param_1,(uVar2 >> 1) + 1);
  uVar2 = _ZN5Botan10hex_decodeEPhPKcmb(*param_1,pbVar1,uVar2,param_3);
  uVar3 = param_1[1] - *param_1;
  if (uVar2 < uVar3 || uVar2 - uVar3 == 0) {
    if (uVar2 < uVar3) {
      param_1[1] = *param_1 + uVar2;
    }
  }
  else {
    FUN_0054084c(param_1,uVar2 - uVar3);
  }
  return;
}

~~~
