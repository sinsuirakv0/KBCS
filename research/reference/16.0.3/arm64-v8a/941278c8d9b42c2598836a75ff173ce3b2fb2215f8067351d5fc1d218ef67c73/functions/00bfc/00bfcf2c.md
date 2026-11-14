# 00bfcf2c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfcf2c",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e6968b6809ee53419275acb4760f351208442e6a48aa0152dd94a1dbde90af99",
  "source_text_sha256": "e6968b6809ee53419275acb4760f351208442e6a48aa0152dd94a1dbde90af99"
}
~~~

## 呼び出し元

- [00c59290](../00c59/00c59290.md)

## 呼び出し先

- [00c5b840](../00c5b/00c5b840.md)

## 疑似コード / UTF-8 340 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEE_00c9c8e8 + 0x10);
  _ZNSt6__ndk16localeC2Ev(param_1 + 1);
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  return;
}

~~~
