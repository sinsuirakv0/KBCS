# 00bfbe9c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfbe9c",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a456916b9bf9228f7136d6b288c7d72ae25f5128ff94fe6bcea2159818c7aa8a",
  "source_text_sha256": "a456916b9bf9228f7136d6b288c7d72ae25f5128ff94fe6bcea2159818c7aa8a"
}
~~~

## 呼び出し元

- [00c581f0](../00c58/00c581f0.md)

## 呼び出し先

- [00c5a7a0](../00c5a/00c5a7a0.md)

## 疑似コード / UTF-8 340 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEE_00c9b848 + 0x10);
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
