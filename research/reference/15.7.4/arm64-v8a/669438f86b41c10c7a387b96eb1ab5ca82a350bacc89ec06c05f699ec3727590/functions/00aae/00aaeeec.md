# 00aaeeec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00aaeeec",
  "name": "FUN_00aaeeec",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "577f4c61b692250f2c268bc89f42cdf57327730886dfbcadc10ca7d261748dd4",
  "source_text_sha256": "577f4c61b692250f2c268bc89f42cdf57327730886dfbcadc10ca7d261748dd4"
}
~~~

## 呼び出し元

- [00695904](../00695/00695904.md)
- [0081c6a0](../0081c/0081c6a0.md)
- [009a2998](../009a2/009a2998.md)
- [009bd6c4](../009bd/009bd6c4.md)
- [009eae0c](../009ea/009eae0c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 243 bytes

~~~c

void FUN_00aaeeec(undefined8 *param_1)

{
  *(undefined1 *)((long)param_1 + 0x2c) = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  *param_1 = 0;
  *(undefined8 *)((long)param_1 + 0x1c) = 0;
  *(undefined4 *)((long)param_1 + 0x24) = 0;
  return;
}

~~~
