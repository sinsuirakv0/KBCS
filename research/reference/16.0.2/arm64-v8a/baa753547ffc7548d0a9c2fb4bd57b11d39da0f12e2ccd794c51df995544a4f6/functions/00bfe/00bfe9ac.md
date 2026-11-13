# 00bfe9ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfe9ac",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3edf5b601679214f4dddc088638730a102550e7244bff11003a452390bb6685a",
  "source_text_sha256": "3edf5b601679214f4dddc088638730a102550e7244bff11003a452390bb6685a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5e3f0](../00c5e/00c5e3f0.md)

## 疑似コード / UTF-8 672 bytes

~~~c

void _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_(long *param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  undefined4 uVar3;
  undefined4 uVar4;
  undefined8 uVar5;
  
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  lVar2 = (long)param_2 + *(long *)(*param_2 + -0x18);
  _ZNSt6__ndk18ios_base4swapERS0_(lVar1,lVar2);
  uVar5 = *(undefined8 *)(lVar1 + 0x88);
  uVar3 = *(undefined4 *)(lVar2 + 0x90);
  *(undefined8 *)(lVar1 + 0x88) = *(undefined8 *)(lVar2 + 0x88);
  uVar4 = *(undefined4 *)(lVar1 + 0x90);
  *(undefined8 *)(lVar2 + 0x88) = uVar5;
  *(undefined4 *)(lVar1 + 0x90) = uVar3;
  *(undefined4 *)(lVar2 + 0x90) = uVar4;
  return;
}

~~~
