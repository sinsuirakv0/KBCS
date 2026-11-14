# 00bf2fdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bf2fdc",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3ad2ad9d947e837a354e464be79b1e31cb85228cf5358ae89dc6923fdad6f6ba",
  "source_text_sha256": "3ad2ad9d947e837a354e464be79b1e31cb85228cf5358ae89dc6923fdad6f6ba"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00442c7c](../00442/00442c7c.md)

## 疑似コード / UTF-8 540 bytes

~~~c

byte * _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm
                 (byte *param_1,ulong param_2)

{
  ulong uVar1;
  byte bVar2;
  byte *pbVar3;
  
  bVar2 = *param_1;
  uVar1 = (ulong)(bVar2 >> 1);
  if ((bVar2 & 1) != 0) {
    uVar1 = *(ulong *)(param_1 + 8);
  }
  if (param_2 < uVar1) {
    pbVar3 = *(byte **)(param_1 + 0x10);
    if ((bVar2 & 1) == 0) {
      pbVar3 = param_1 + 1;
    }
    return pbVar3 + param_2;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00442c7c();
}

~~~
