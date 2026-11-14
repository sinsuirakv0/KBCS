# 00bfa0cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfa0cc",
  "name": "_ZNSt6__ndk112system_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bd422ff0037ee70d846014d93427837c9fdce786e1149570a7d38e9ca537c047",
  "source_text_sha256": "bd422ff0037ee70d846014d93427837c9fdce786e1149570a7d38e9ca537c047"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c5f220](../00c5f/00c5f220.md)

## 疑似コード / UTF-8 123 bytes

~~~c

void _ZNSt6__ndk112system_errorD0Ev(void *param_1)

{
  _ZNSt6__ndk112system_errorD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
