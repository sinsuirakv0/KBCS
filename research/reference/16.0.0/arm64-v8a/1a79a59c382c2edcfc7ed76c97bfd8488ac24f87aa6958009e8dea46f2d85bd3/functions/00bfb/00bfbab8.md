# 00bfbab8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfbab8",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1ERKS3_",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c0ff58cce4f9929eaeabb6d8048779a4b2ede04d61b28ba4d45ad1f3e61b2db8",
  "source_text_sha256": "c0ff58cce4f9929eaeabb6d8048779a4b2ede04d61b28ba4d45ad1f3e61b2db8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a3d0](../00c5a/00c5a3d0.md)

## 疑似コード / UTF-8 585 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1ERKS3_(long *param_1,long param_2)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEE_00c9b448 + 0x10);
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
