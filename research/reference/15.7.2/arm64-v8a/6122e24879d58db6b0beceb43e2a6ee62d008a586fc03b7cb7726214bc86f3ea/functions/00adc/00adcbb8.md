# 00adcbb8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00adccc4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccc4.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00adcbb8",
  "name": "FUN_00adcbb8",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8ef64b5264d795acc1b0b0a20e63f560d6047ad01ee7e79f5ca7fd18787c0b05",
  "source_text_sha256": "8ef64b5264d795acc1b0b0a20e63f560d6047ad01ee7e79f5ca7fd18787c0b05"
}
~~~

## 呼び出し元

- [0073e0c8](../0073e/0073e0c8.md)
- [0073e6dc](../0073e/0073e6dc.md)
- [0073eb18](../0073e/0073eb18.md)
- [0073ed78](../0073e/0073ed78.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 108 bytes

~~~c

void FUN_00adcbb8(undefined8 *param_1)

{
  param_1[1] = *param_1;
  param_1[4] = param_1[3];
  return;
}

~~~
