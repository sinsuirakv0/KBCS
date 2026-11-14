# 00bfcf1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfcf1c",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sputnEPKcl",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a3bba09d60f55b73f6e170eb50b00d083ddc80c2d5cd99b1bd3be277be5d4b13",
  "source_text_sha256": "a3bba09d60f55b73f6e170eb50b00d083ddc80c2d5cd99b1bd3be277be5d4b13"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 299 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sputnEPKcl(long *param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bfcf28. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 0x60))();
  return;
}

~~~
