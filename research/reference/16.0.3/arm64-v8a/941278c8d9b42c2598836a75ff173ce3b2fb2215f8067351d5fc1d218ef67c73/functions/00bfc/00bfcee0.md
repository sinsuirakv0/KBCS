# 00bfcee0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfcee0",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sputcEc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "613906a5f90ca8fc14a5ee900ae25d693de32555b0ddd4eed5a9b8e90274020b",
  "source_text_sha256": "613906a5f90ca8fc14a5ee900ae25d693de32555b0ddd4eed5a9b8e90274020b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 533 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sputcEc(long *param_1,byte param_2)

{
  byte *pbVar1;
  ulong uVar2;
  
  pbVar1 = (byte *)param_1[6];
  if (pbVar1 != (byte *)param_1[7]) {
    param_1[6] = (long)(pbVar1 + 1);
    *pbVar1 = param_2;
    return (ulong)param_2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bfcf18. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar2 = (**(code **)(*param_1 + 0x68))(param_1,param_2);
  return uVar2;
}

~~~
