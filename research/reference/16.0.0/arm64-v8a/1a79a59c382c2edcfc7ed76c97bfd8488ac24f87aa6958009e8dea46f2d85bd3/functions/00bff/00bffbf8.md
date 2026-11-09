# 00bffbf8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bffbf8",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5uflowEv",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dc78b8a5227dfa2cc60375a0f15abad0d5c263316197fb00d6a8b8aeca18ac44",
  "source_text_sha256": "dc78b8a5227dfa2cc60375a0f15abad0d5c263316197fb00d6a8b8aeca18ac44"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 286 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5uflowEv(long *param_1)

{
  ulong uVar1;
  
  uVar1 = (**(code **)(*param_1 + 0x48))();
  if ((int)uVar1 != -1) {
    uVar1 = (ulong)*(uint *)param_1[3];
    param_1[3] = (long)((uint *)param_1[3] + 1);
  }
  return uVar1;
}

~~~
