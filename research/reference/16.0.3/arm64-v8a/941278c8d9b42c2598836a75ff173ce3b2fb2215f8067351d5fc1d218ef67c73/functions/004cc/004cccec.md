# 004cccec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "004cccec",
  "name": "_ZN5Botan10hex_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "75107ca700aab970a10909437c44114c49ab45289eaeca65a478c736c759cd3e",
  "source_text_sha256": "75107ca700aab970a10909437c44114c49ab45289eaeca65a478c736c759cd3e"
}
~~~

## 呼び出し元

- [00c5a200](../00c5a/00c5a200.md)

## 呼び出し先

- [00c5a1f0](../00c5a/00c5a1f0.md)

## 疑似コード / UTF-8 421 bytes

~~~c

void _ZN5Botan10hex_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb
               (byte *param_1,undefined4 param_2)

{
  ulong uVar1;
  byte *pbVar2;
  
  uVar1 = *(ulong *)(param_1 + 8);
  pbVar2 = *(byte **)(param_1 + 0x10);
  if ((*param_1 & 1) == 0) {
    pbVar2 = param_1 + 1;
    uVar1 = (ulong)(*param_1 >> 1);
  }
  _ZN5Botan10hex_decodeEPKcmb(pbVar2,uVar1,param_2);
  return;
}

~~~
