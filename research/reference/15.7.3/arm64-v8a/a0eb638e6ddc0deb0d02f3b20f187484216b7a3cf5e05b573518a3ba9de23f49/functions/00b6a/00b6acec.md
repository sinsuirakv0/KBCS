# 00b6acec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b6acec",
  "name": "_ZN8firebase4auth22GameCenterAuthProvider21IsPlayerAuthenticatedEv",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e74028d8f05ef886ce86e4855f3c4b524b9cdc0e06a3acc4a2ac3e0758f7362",
  "source_text_sha256": "0e74028d8f05ef886ce86e4855f3c4b524b9cdc0e06a3acc4a2ac3e0758f7362"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"is_gamecenter_available_on_android"
~~~

## 疑似コード / UTF-8 172 bytes

~~~c

undefined8 _ZN8firebase4auth22GameCenterAuthProvider21IsPlayerAuthenticatedEv(void)

{
  _ZN8firebase9LogAssertEPKcz("is_gamecenter_available_on_android");
  return 0;
}

~~~
