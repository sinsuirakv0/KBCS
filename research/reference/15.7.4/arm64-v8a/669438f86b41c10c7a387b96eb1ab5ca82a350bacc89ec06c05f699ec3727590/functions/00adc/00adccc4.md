# 00adccc4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00adcbb8`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adcbb8.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00adccc4",
  "name": "FUN_00adccc4",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aac33cf46f12bf1f7a8267405a3dfa79b389a32708010386339ad246337dcd51",
  "source_text_sha256": "aac33cf46f12bf1f7a8267405a3dfa79b389a32708010386339ad246337dcd51"
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

void FUN_00adccc4(undefined8 *param_1)

{
  param_1[1] = *param_1;
  param_1[4] = param_1[3];
  return;
}

~~~
