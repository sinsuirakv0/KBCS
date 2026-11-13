# 00bfbf7c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfbf7c",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1ERKS3_",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f1c21db945dca0692193f922f9e31000a0f59c4fe9d3f68393694b47cc08e37a",
  "source_text_sha256": "f1c21db945dca0692193f922f9e31000a0f59c4fe9d3f68393694b47cc08e37a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a8a0](../00c5a/00c5a8a0.md)

## 疑似コード / UTF-8 585 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1ERKS3_(long *param_1,long param_2)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEE_00c9b918 + 0x10);
  _ZNSt6__ndk16localeC1ERKS0_(param_1 + 1,param_2 + 8);
  lVar1 = *(long *)(param_2 + 0x10);
  param_1[3] = *(long *)(param_2 + 0x18);
  param_1[2] = lVar1;
  lVar1 = *(long *)(param_2 + 0x20);
  param_1[5] = *(long *)(param_2 + 0x28);
  param_1[4] = lVar1;
  lVar1 = *(long *)(param_2 + 0x30);
  param_1[7] = *(long *)(param_2 + 0x38);
  param_1[6] = lVar1;
  return;
}

~~~
