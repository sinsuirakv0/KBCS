# 00ae3fbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae3fbc.md)

## 関数情報

~~~json
{
  "address": "00ae3fbc",
  "name": "firebase::LogGetLevel",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "572ec09f0f46131dd0f4fb9f4d7ad694c9c0457536ec0ab037cfc5c399da6855",
  "source_text_sha256": "572ec09f0f46131dd0f4fb9f4d7ad694c9c0457536ec0ab037cfc5c399da6855"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 136 bytes

~~~c

/* firebase::LogGetLevel() */

undefined4 firebase::LogGetLevel(void)

{
  return *(undefined4 *)PTR_g_log_level_00c1b7d0;
}

~~~
