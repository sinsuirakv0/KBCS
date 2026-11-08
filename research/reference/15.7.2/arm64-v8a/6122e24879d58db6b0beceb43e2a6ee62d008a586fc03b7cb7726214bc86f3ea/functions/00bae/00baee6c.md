# 00baee6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00baee6c",
  "name": "_ZNSt6__ndk116__narrow_to_utf8ILm32EED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bc77379b2f97043393c6ec3a913d84319d0bde4f3ec066308aa5c90d796dd2ef",
  "source_text_sha256": "bc77379b2f97043393c6ec3a913d84319d0bde4f3ec066308aa5c90d796dd2ef"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1b00](../00be1/00be1b00.md)

## 疑似コード / UTF-8 145 bytes

~~~c

void _ZNSt6__ndk116__narrow_to_utf8ILm32EED0Ev(void *param_1)

{
  _ZNSt6__ndk116__narrow_to_utf8ILm32EED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
