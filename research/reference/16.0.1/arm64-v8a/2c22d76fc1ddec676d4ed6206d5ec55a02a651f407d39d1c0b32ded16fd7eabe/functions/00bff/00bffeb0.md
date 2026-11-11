# 00bffeb0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bffeb0",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5gbumpEi",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9cf7b57781e9f692ab2834914c05f988e9d5536be729cb9a69b4933936f904c1",
  "source_text_sha256": "9cf7b57781e9f692ab2834914c05f988e9d5536be729cb9a69b4933936f904c1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5gbumpEi(long param_1,int param_2)

{
  *(long *)(param_1 + 0x18) = *(long *)(param_1 + 0x18) + (long)param_2 * 4;
  return;
}

~~~
