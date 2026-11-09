# 00acbe7c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acbe7c",
  "name": "FUN_00acbe7c",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ec548f80c2b98a6f35f9d2ad5a9c3f952246a5c0938f7fecd3f9ada677a267a",
  "source_text_sha256": "9ec548f80c2b98a6f35f9d2ad5a9c3f952246a5c0938f7fecd3f9ada677a267a"
}
~~~

## 呼び出し元

- [00acbb50](../00acb/00acbb50.md)

## 呼び出し先

- [00acb88c](../00acb/00acb88c.md)
- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 195 bytes

~~~c

void FUN_00acbe7c(long param_1)

{
  void *__ptr;
  
  __ptr = *(void **)(param_1 + 0x18);
  if (__ptr != (void *)0x0) {
    FUN_00acb88c(__ptr);
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
