# 00b7edcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00b7edcc",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b618ca873f154b734ca720951478c68919994b2b749791c6ece2f0c31ae4f6c5",
  "source_text_sha256": "b618ca873f154b734ca720951478c68919994b2b749791c6ece2f0c31ae4f6c5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd980](../00bdd/00bdd980.md)
- [00be12e0](../00be1/00be12e0.md)

## 疑似コード / UTF-8 307 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE
               (undefined8 param_1,long *param_2,undefined8 param_3)

{
  (**(code **)(*param_2 + 0x10))();
  _ZNSt6__ndk16localeC1ERKS0_(param_1,param_2 + 1);
  _ZNSt6__ndk16localeaSERKS0_(param_2 + 1,param_3);
  return;
}

~~~
