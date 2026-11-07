# 00baef9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00baf0a8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf0a8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00baef9c",
  "name": "_ZNSt6__ndk18numpunctIcED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "697041c2c57b5dfd4d05c4ed29191cb8cfc8d8f9ff4438451bb8eb6857335ae7",
  "source_text_sha256": "697041c2c57b5dfd4d05c4ed29191cb8cfc8d8f9ff4438451bb8eb6857335ae7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1b40](../00be1/00be1b40.md)

## 疑似コード / UTF-8 119 bytes

~~~c

void _ZNSt6__ndk18numpunctIcED0Ev(void *param_1)

{
  _ZNSt6__ndk18numpunctIcED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
