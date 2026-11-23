# 00b5bfcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afc248`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc248.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0060.md#compare-fbb7df1617faa1973672c68165e0361d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
