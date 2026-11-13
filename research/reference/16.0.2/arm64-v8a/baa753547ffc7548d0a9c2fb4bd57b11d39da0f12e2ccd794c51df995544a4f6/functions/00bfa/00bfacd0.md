# 00bfacd0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfacd0",
  "name": "_ZNSt6__ndk115__thread_struct25notify_all_at_thread_exitEPNS_18condition_variableEPNS_5mutexE",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9a5d462c5f4797aa2307af2354e026287f78a0cdae7f39440a90547e067efa76",
  "source_text_sha256": "9a5d462c5f4797aa2307af2354e026287f78a0cdae7f39440a90547e067efa76"
}
~~~

## 呼び出し元

- [00c5e2d0](../00c5e/00c5e2d0.md)

## 呼び出し先

- [00bfaa64](../00bfa/00bfaa64.md)

## 疑似コード / UTF-8 179 bytes

~~~c

void _ZNSt6__ndk115__thread_struct25notify_all_at_thread_exitEPNS_18condition_variableEPNS_5mutexE
               (undefined8 *param_1)

{
  FUN_00bfaa64(*param_1);
  return;
}

~~~
