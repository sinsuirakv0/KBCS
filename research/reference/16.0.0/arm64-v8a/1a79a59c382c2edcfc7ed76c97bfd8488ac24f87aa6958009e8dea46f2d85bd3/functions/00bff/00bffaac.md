# 00bffaac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bffaac",
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
