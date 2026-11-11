# 00bffcc4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bffcc4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sputcEw",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9fc8558f7bbfd2626a38e620b5ee4b2ed0245cd0afb88dca09149432418dbfdd",
  "source_text_sha256": "9fc8558f7bbfd2626a38e620b5ee4b2ed0245cd0afb88dca09149432418dbfdd"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 525 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sputcEw(long *param_1,uint param_2)

{
  uint *puVar1;
  ulong uVar2;
  
  puVar1 = (uint *)param_1[6];
  if (puVar1 != (uint *)param_1[7]) {
    *puVar1 = param_2;
    param_1[6] = (long)(puVar1 + 1);
    return (ulong)param_2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bffcf4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar2 = (**(code **)(*param_1 + 0x68))(param_1);
  return uVar2;
}

~~~
