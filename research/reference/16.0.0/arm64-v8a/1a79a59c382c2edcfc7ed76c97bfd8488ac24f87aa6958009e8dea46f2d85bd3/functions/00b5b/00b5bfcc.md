# 00b5bfcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b5bfcc",
  "name": "_ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED2Ev",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "47f0da81cf6ffaf94a21baeab889d4505a46bf40f309bd6e2903c330aad1bce5",
  "source_text_sha256": "47f0da81cf6ffaf94a21baeab889d4505a46bf40f309bd6e2903c330aad1bce5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57aa0](../00c57/00c57aa0.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)

## 疑似コード / UTF-8 718 bytes

~~~c

void _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED2Ev
               (long *param_1)

{
  long lVar1;
  long *plVar2;
  
  lVar1 = param_1[4];
  *param_1 = (long)(
                   PTR__ZTVNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEEE_00c9b388
                   + 0x10);
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  if (((char)param_1[5] == '\0') && (plVar2 = (long *)param_1[3], plVar2 != (long *)0x0)) {
    param_1[3] = 0;
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
    (**(code **)(*plVar2 + 8))(plVar2);
  }
  else {
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  _ZNSt6__ndk119__shared_weak_countD1Ev(param_1);
  return;
}

~~~
