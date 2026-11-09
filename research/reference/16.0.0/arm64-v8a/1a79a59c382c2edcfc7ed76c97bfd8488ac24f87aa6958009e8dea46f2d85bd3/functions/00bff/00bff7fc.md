# 00bff7fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bff7fc",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sgetcEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "218797393cb55adf06b0ae9b9ad59adc6dcc04ad63c34c19e8c5c0ff99cd2ab1",
  "source_text_sha256": "218797393cb55adf06b0ae9b9ad59adc6dcc04ad63c34c19e8c5c0ff99cd2ab1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 422 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sgetcEv(long *param_1)

{
  ulong uVar1;
  
  if ((uint *)param_1[3] != (uint *)param_1[4]) {
    return (ulong)*(uint *)param_1[3];
  }
                    /* WARNING: Could not recover jumptable at 0x00bff81c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar1 = (**(code **)(*param_1 + 0x48))();
  return uVar1;
}

~~~
