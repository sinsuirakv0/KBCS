# 00bbbba4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bbbba4",
  "name": "_ZN8firebase9messaging28SetRegistrationOnInitEnabledEb",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "efafa7f6aaecbe929c9386bbe04beb413ad294e119d9b5e85a851fa83ab4c1ea",
  "source_text_sha256": "efafa7f6aaecbe929c9386bbe04beb413ad294e119d9b5e85a851fa83ab4c1ea"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a6e0](../00c5a/00c5a6e0.md)

## 疑似コード / UTF-8 167 bytes

~~~c

void _ZN8firebase9messaging28SetRegistrationOnInitEnabledEb(uint param_1)

{
  _ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb(param_1 & 1);
  return;
}

~~~
