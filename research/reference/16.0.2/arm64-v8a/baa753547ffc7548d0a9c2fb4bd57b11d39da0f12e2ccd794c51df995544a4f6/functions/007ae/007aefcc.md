# 007aefcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "007aefcc",
  "name": "FUN_007aefcc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "969928c555d6b089fc991b0c8518720049f69c8f3b0e545cb08d99a5c117b358",
  "source_text_sha256": "969928c555d6b089fc991b0c8518720049f69c8f3b0e545cb08d99a5c117b358"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 383 bytes

~~~c

long FUN_007aefcc(long param_1,long param_2)

{
                    /* catch() { ... } // from try @ 007ae02c with catch @ 007aefcc */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN19FriendInviteManager22onErrorInputInviteCodeEiE3$_0") {
    param_1 = 0;
  }
                    /* catch() { ... } // from try @ 007ae024 with catch @ 007aefe4 */
  return param_1;
}

~~~
