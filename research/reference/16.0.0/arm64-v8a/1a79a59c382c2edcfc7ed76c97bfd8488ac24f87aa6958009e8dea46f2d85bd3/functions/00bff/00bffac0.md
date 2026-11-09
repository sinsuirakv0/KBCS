# 00bffac0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bffac0",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4setpEPwS4_",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7259760e0046c5e836d5e3ee4d27a9c235e05320c156c4ddab9900c87ee20d0b",
  "source_text_sha256": "7259760e0046c5e836d5e3ee4d27a9c235e05320c156c4ddab9900c87ee20d0b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 289 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4setpEPwS4_
               (long param_1,undefined8 param_2,undefined8 param_3)

{
  *(undefined8 *)(param_1 + 0x28) = param_2;
  *(undefined8 *)(param_1 + 0x30) = param_2;
  *(undefined8 *)(param_1 + 0x38) = param_3;
  return;
}

~~~
