# 00b7cfbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00b7cfbc",
  "name": "_ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "428e69339109ed2e4f09cee9abe5300c2d3b3cc01d1d144a2b3e79c12cef92c8",
  "source_text_sha256": "428e69339109ed2e4f09cee9abe5300c2d3b3cc01d1d144a2b3e79c12cef92c8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004377fc](../00437/004377fc.md)
- [00be1120](../00be1/00be1120.md)

## 疑似コード / UTF-8 363 bytes

~~~c

void _ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv(long *param_1)

{
  if (*param_1 != 0) {
    _ZNSt6__ndk117__assoc_sub_state24set_value_at_thread_exitEv();
    return;
  }
                    /* try { // try from 00b7cfd0 to 00c7d023 has its CatchHandler @ 00b7888c */
                    /* WARNING: Subroutine does not return */
  FUN_004377fc(3);
}

~~~
