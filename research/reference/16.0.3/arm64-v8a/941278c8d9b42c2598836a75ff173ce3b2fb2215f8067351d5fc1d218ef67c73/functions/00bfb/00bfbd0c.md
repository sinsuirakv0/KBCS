# 00bfbd0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfbd0c",
  "name": "FUN_00bfbd0c",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5c70326a5cc4a5593cb73625d4fa898e8a394dbc7ba639179434414fd8b44d92",
  "source_text_sha256": "5c70326a5cc4a5593cb73625d4fa898e8a394dbc7ba639179434414fd8b44d92"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c591f0](../00c59/00c591f0.md)

## 疑似コード / UTF-8 160 bytes

~~~c

void FUN_00bfbd0c(void *param_1)

{
  if (param_1 != (void *)0x0) {
    _ZNSt6__ndk115__thread_structD1Ev();
    _ZdlPv(param_1);
    return;
  }
  return;
}

~~~
