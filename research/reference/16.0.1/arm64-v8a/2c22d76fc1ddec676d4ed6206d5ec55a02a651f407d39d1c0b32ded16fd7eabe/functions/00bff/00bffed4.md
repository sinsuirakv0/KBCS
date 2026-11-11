# 00bffed4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bffed4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5pbumpEi",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ec24fdd483a6c231c9166c8330b136122f5c65fe233947b734071e99cee7125",
  "source_text_sha256": "7ec24fdd483a6c231c9166c8330b136122f5c65fe233947b734071e99cee7125"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5pbumpEi(long param_1,int param_2)

{
  *(long *)(param_1 + 0x30) = *(long *)(param_1 + 0x30) + (long)param_2 * 4;
  return;
}

~~~
