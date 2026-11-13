# 00bfa1cc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfa1cc",
  "name": "_ZNSt6__ndk15mutex4lockEv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6a09bf60f6e907cbf77359d35e00face011e0c1ea964fdc0b39b44725fd3203",
  "source_text_sha256": "d6a09bf60f6e907cbf77359d35e00face011e0c1ea964fdc0b39b44725fd3203"
}
~~~

## 呼び出し元

- [00c581b0](../00c58/00c581b0.md)

## 呼び出し先

- [00c581f0](../00c58/00c581f0.md)
- [00c5b770](../00c5b/00c5b770.md)

## 関連文字列（未確認候補）

~~~text
"mutex lock failed"
~~~

## 疑似コード / UTF-8 287 bytes

~~~c

void _ZNSt6__ndk15mutex4lockEv(pthread_mutex_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_mutex_lock(param_1);
  if (iVar1 == 0) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"mutex lock failed");
}

~~~
