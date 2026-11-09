# 00bfaac4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfaac4",
  "name": "_ZNSt6__ndk117iostream_categoryEv",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc47307183cf9b19063f199a722ee44630cd2e50b5f3a46f3abd52fe6ac612e2",
  "source_text_sha256": "cc47307183cf9b19063f199a722ee44630cd2e50b5f3a46f3abd52fe6ac612e2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)

## 疑似コード / UTF-8 243 bytes

~~~c

undefined ** _ZNSt6__ndk117iostream_categoryEv(void)

{
  int iVar1;
  
  if (((DAT_01126f90 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01126f90), iVar1 != 0)) {
    __cxa_guard_release(&DAT_01126f90);
  }
  return &PTR_PTR_00ca4400;
}

~~~
