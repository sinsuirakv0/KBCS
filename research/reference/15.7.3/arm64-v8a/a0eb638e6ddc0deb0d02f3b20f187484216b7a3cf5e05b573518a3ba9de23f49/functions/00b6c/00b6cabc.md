# 00b6cabc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b6cabc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a2aec9770231094bc0897245999b1fd90613dce3eccdcf71f0e43f2f4106798",
  "source_text_sha256": "4a2aec9770231094bc0897245999b1fd90613dce3eccdcf71f0e43f2f4106798"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00be0db0](../00be0/00be0db0.md)

## 疑似コード / UTF-8 223 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv(void *param_1)

{
  if (param_1 != (void *)0x0) {
    _ZN8firebase4auth10CredentialD1Ev();
    _ZdlPv(param_1);
    return;
  }
  return;
}

~~~
