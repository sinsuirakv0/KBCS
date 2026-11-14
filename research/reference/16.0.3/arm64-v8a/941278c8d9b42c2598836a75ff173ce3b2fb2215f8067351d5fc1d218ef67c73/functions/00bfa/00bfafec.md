# 00bfafec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfafec",
  "name": "_ZNSt6__ndk17promiseIvE28set_exception_at_thread_exitESt13exception_ptr",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c2e9bf0b89dcda319b57bb25b48af1ae75d21dbce02597a2b616b85119042ee",
  "source_text_sha256": "7c2e9bf0b89dcda319b57bb25b48af1ae75d21dbce02597a2b616b85119042ee"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0045aa34](../0045a/0045aa34.md)
- [00c59390](../00c59/00c59390.md)
- [00c59550](../00c59/00c59550.md)
- [00c5f2e0](../00c5f/00c5f2e0.md)

## 疑似コード / UTF-8 473 bytes

~~~c

void _ZNSt6__ndk17promiseIvE28set_exception_at_thread_exitESt13exception_ptr(long *param_1)

{
  long lVar1;
  undefined1 auStack_8 [8];
  
  lVar1 = *param_1;
  if (lVar1 != 0) {
    _ZNSt13exception_ptrC1ERKS_(auStack_8);
    _ZNSt6__ndk117__assoc_sub_state28set_exception_at_thread_exitESt13exception_ptr(lVar1,auStack_8)
    ;
    _ZNSt13exception_ptrD1Ev(auStack_8);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_0045aa34(3);
}

~~~
