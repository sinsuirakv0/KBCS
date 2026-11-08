# 00ae3fac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00ae3fac",
  "name": "_ZN8firebase11LogSetLevelENS_8LogLevelE",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a05458c3e8ff96d9c35e94a50942ac1dc4f7acf8cd5211a2456bd16322c5fd3",
  "source_text_sha256": "2a05458c3e8ff96d9c35e94a50942ac1dc4f7acf8cd5211a2456bd16322c5fd3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde190](../00bde/00bde190.md)

## 疑似コード / UTF-8 203 bytes

~~~c

void _ZN8firebase11LogSetLevelENS_8LogLevelE(undefined4 param_1)

{
  *(undefined4 *)PTR__ZN8firebase11g_log_levelE_00c1b7d0 = param_1;
  _ZN8firebase19LogSetPlatformLevelENS_8LogLevelE();
  return;
}

~~~
