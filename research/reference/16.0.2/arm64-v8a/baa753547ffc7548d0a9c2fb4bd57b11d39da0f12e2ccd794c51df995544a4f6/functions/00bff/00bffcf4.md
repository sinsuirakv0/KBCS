# 00bffcf4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bffcf4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE9sputbackcEw",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99a147f332c44e4b2a67a5b71a02db0c3925e0f4636d54bfb5b1a64a65c60024",
  "source_text_sha256": "99a147f332c44e4b2a67a5b71a02db0c3925e0f4636d54bfb5b1a64a65c60024"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 520 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE9sputbackcEw(long *param_1,uint param_2)

{
  ulong uVar1;
  uint *puVar2;
  
  if ((param_1[2] != param_1[3]) && (puVar2 = (uint *)(param_1[3] + -4), *puVar2 == param_2)) {
    param_1[3] = (long)puVar2;
    return (ulong)param_2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bffd28. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar1 = (**(code **)(*param_1 + 0x58))();
  return uVar1;
}

~~~
