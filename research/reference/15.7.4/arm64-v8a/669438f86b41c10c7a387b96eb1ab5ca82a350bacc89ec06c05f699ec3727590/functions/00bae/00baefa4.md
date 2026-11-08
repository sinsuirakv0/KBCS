# 00baefa4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00baefa4",
  "name": "_ZNSt6__ndk117__widen_from_utf8ILm16EED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3d526d619a9d36faa5cd98a5a6a629311c79a7cfd2c506bbfb1accd79b1a780f",
  "source_text_sha256": "3d526d619a9d36faa5cd98a5a6a629311c79a7cfd2c506bbfb1accd79b1a780f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1c10](../00be1/00be1c10.md)

## 疑似コード / UTF-8 146 bytes

~~~c

void _ZNSt6__ndk117__widen_from_utf8ILm16EED0Ev(void *param_1)

{
  _ZNSt6__ndk116__narrow_to_utf8ILm32EED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
