# 00bfb4cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfb4cc",
  "name": "_ZNSt6__ndk111timed_mutex6unlockEv",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f4cfe0d12c79d7f713952587c85dd7a626e10573e22cf248a6a34fc40c87ebe",
  "source_text_sha256": "9f4cfe0d12c79d7f713952587c85dd7a626e10573e22cf248a6a34fc40c87ebe"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c591c0](../00c59/00c591c0.md)
- [00c5a1b0](../00c5a/00c5a1b0.md)
- [00c5c740](../00c5c/00c5c740.md)
- [00c5c750](../00c5c/00c5c750.md)

## 関連文字列（未確認候補）

~~~text
"mutex lock failed"
~~~

## 疑似コード / UTF-8 456 bytes

~~~c

int _ZNSt6__ndk111timed_mutex6unlockEv(pthread_mutex_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_mutex_lock(param_1);
  if (iVar1 == 0) {
    *(undefined1 *)((long)param_1 + 0x58) = 0;
    _ZNSt6__ndk118condition_variable10notify_oneEv(param_1 + 1);
    iVar1 = pthread_mutex_unlock(param_1);
    return iVar1;
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"mutex lock failed");
}

~~~
