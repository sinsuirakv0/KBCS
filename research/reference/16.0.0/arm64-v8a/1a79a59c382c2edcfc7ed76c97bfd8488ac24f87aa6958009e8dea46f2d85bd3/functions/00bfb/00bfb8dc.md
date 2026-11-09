# 00bfb8dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfb8dc",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "29df578467124302e54f80ac5d43c6f1de7336d9444012fd8f8db34a80765029",
  "source_text_sha256": "29df578467124302e54f80ac5d43c6f1de7336d9444012fd8f8db34a80765029"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 764 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv(long *param_1)

{
  ulong uVar1;
  byte *pbVar2;
  
  if ((byte *)param_1[3] == (byte *)param_1[4]) {
    uVar1 = (**(code **)(*param_1 + 0x50))();
    if ((int)uVar1 == -1) {
      return uVar1;
    }
    pbVar2 = (byte *)param_1[3];
    if (pbVar2 == (byte *)param_1[4]) goto LAB_00bfb938;
  }
  else {
    pbVar2 = (byte *)param_1[3] + 1;
    param_1[3] = (long)pbVar2;
    if (pbVar2 == (byte *)param_1[4]) {
LAB_00bfb938:
                    /* WARNING: Could not recover jumptable at 0x00bfb94c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      uVar1 = (**(code **)(*param_1 + 0x48))();
      return uVar1;
    }
  }
  return (ulong)*pbVar2;
}

~~~
