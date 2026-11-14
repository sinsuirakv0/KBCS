# 00bfceb0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfceb0",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE7sungetcEv",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e2cea07a0ea076b0dc1f4ed56a17e56591ff479ba5a7ad5aa2d4ad46c9e9861",
  "source_text_sha256": "8e2cea07a0ea076b0dc1f4ed56a17e56591ff479ba5a7ad5aa2d4ad46c9e9861"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 488 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE7sungetcEv(long *param_1)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = param_1[3];
  if (param_1[2] != lVar1) {
    param_1[3] = lVar1 + -1;
    return (ulong)*(byte *)(lVar1 + -1);
  }
                    /* WARNING: Could not recover jumptable at 0x00bfcedc. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar2 = (**(code **)(*param_1 + 0x58))(param_1,0xffffffff);
  return uVar2;
}

~~~
