# 00ae3fac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae3fac.md)

## 関数情報

~~~json
{
  "address": "00ae3fac",
  "name": "firebase::LogSetLevel",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a3d7828c7430923475153d749e79a9875acbbfa36d772d0d1f7ae50beb5c6b81",
  "source_text_sha256": "a3d7828c7430923475153d749e79a9875acbbfa36d772d0d1f7ae50beb5c6b81"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde190](../00bde/00bde190.md)

## 疑似コード 1/1 / UTF-8 202 bytes

~~~c

/* firebase::LogSetLevel(firebase::LogLevel) */

void firebase::LogSetLevel(undefined4 param_1)

{
  *(undefined4 *)PTR_g_log_level_00c1b7d0 = param_1;
  LogSetPlatformLevel();
  return;
}

~~~
