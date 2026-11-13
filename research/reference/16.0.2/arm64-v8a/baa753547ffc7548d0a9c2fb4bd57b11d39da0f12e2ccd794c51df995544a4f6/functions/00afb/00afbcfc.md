# 00afbcfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afbcfc",
  "name": "FUN_00afbcfc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "059f91d860cb433e8160d2c93093036d415d7267b7ac9bf6b89c4857151ec263",
  "source_text_sha256": "059f91d860cb433e8160d2c93093036d415d7267b7ac9bf6b89c4857151ec263"
}
~~~

## 呼び出し元

- [005f2da8](../005f2/005f2da8.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 248 bytes

~~~c

void FUN_00afbcfc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x849c0) = *(int *)(lVar1 + 0x849c0) + param_3;
  return;
}

~~~
