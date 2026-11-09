# 00acbe1c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acbe1c",
  "name": "FUN_00acbe1c",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f95dbbb153ab12f99834fb51016d4ea4c0e621d24b2f166773324971c4eb105",
  "source_text_sha256": "2f95dbbb153ab12f99834fb51016d4ea4c0e621d24b2f166773324971c4eb105"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00acb88c](../00acb/00acb88c.md)
- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 208 bytes

~~~c

void FUN_00acbe1c(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)*param_1;
  *param_1 = 0;
  if (__ptr != (void *)0x0) {
    FUN_00acb88c(__ptr);
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
