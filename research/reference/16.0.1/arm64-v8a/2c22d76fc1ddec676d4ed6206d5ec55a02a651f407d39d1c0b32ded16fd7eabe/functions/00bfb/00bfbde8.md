# 00bfbde8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfbde8",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE9sputbackcEc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b5916ec98df9f97dfe66b702a878748a4f7ea8e8a308519450e58bc0235e4656",
  "source_text_sha256": "b5916ec98df9f97dfe66b702a878748a4f7ea8e8a308519450e58bc0235e4656"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 535 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE9sputbackcEc(long *param_1,byte param_2)

{
  ulong uVar1;
  byte *pbVar2;
  
  if ((param_1[2] != param_1[3]) && (pbVar2 = (byte *)(param_1[3] + -1), *pbVar2 == param_2)) {
    param_1[3] = (long)pbVar2;
    return (ulong)*pbVar2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bfbe1c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar1 = (**(code **)(*param_1 + 0x58))(param_1,param_2);
  return uVar1;
}

~~~
