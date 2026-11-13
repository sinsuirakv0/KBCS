# 00bffd2c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bffd2c",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE7sungetcEv",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3c7e3fa38c5cdaf0eb2045217860649a6a39ad8d962f37f3f0d6bdc66f92cec",
  "source_text_sha256": "d3c7e3fa38c5cdaf0eb2045217860649a6a39ad8d962f37f3f0d6bdc66f92cec"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 534 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE7sungetcEv(long *param_1)

{
  uint uVar1;
  ulong uVar2;
  uint *puVar3;
  
  if (param_1[2] != param_1[3]) {
    puVar3 = (uint *)(param_1[3] + -4);
    uVar1 = *puVar3;
    param_1[3] = (long)puVar3;
    return (ulong)uVar1;
  }
                    /* WARNING: Could not recover jumptable at 0x00bffd5c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar2 = (**(code **)(*param_1 + 0x58))(param_1,0xffffffff);
  return uVar2;
}

~~~
