# 007fefac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007fefac",
  "name": "FUN_007fefac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4b34c580822b4a0d27a63e329b8d269d3387ea21bed1f9b8a443b1b1d88861d4",
  "source_text_sha256": "4b34c580822b4a0d27a63e329b8d269d3387ea21bed1f9b8a443b1b1d88861d4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 232 bytes

~~~c

void FUN_007fefac(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)param_1[2];
  *param_1 = &PTR_FUN_00c7dc30;
  if (__ptr != (void *)0x0) {
    param_1[3] = __ptr;
    _ZdlPv(__ptr);
  }
  _ZdlPv(param_1);
  return;
}

~~~
