# 00bfa5ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfa5ec",
  "name": "_ZNSt6__ndk115future_categoryEv",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3105720acfa0299f93ed656caf1a2657151cad9ce776f202db59ce8f3b9185a6",
  "source_text_sha256": "3105720acfa0299f93ed656caf1a2657151cad9ce776f202db59ce8f3b9185a6"
}
~~~

## 呼び出し元

- [00c593b0](../00c59/00c593b0.md)

## 呼び出し先

- [00c58ef0](../00c58/00c58ef0.md)
- [00c58f10](../00c58/00c58f10.md)

## 疑似コード / UTF-8 236 bytes

~~~c

undefined * _ZNSt6__ndk115future_categoryEv(void)

{
  int iVar1;
  
  if (((DAT_01128430 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01128430), iVar1 != 0)) {
    __cxa_guard_release(&DAT_01128430);
  }
  return &DAT_00ca5898;
}

~~~
