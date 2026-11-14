# 00bfafc8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfafc8",
  "name": "_ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4134f9d0a3f99d5870489083d96f81b1c3f7aa5592a8bd52e514a5b8ab9f25e8",
  "source_text_sha256": "4134f9d0a3f99d5870489083d96f81b1c3f7aa5592a8bd52e514a5b8ab9f25e8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0045aa34](../0045a/0045aa34.md)
- [00c5f2c0](../00c5f/00c5f2c0.md)

## 疑似コード / UTF-8 266 bytes

~~~c

void _ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv(long *param_1)

{
  if (*param_1 != 0) {
    _ZNSt6__ndk117__assoc_sub_state24set_value_at_thread_exitEv();
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_0045aa34(3);
}

~~~
