# 007cbdac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007cbdac.md)

## 関数情報

~~~json
{
  "address": "007cbdac",
  "name": "FUN_007cbdac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1c275e40c5ff5819f568816b6858f0835a3a4eeb4df62b6cb718c193d4df2631",
  "source_text_sha256": "1c275e40c5ff5819f568816b6858f0835a3a4eeb4df62b6cb718c193d4df2631"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード 1/1 / UTF-8 329 bytes

~~~c

void FUN_007cbdac(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)param_1[2];
  *param_1 = &PTR_FUN_00bffef8;
  if (__ptr != (void *)0x0) {
    param_1[3] = __ptr;
    _ZdlPv(__ptr);
  }
                    /* try { // try from 007cbde8 to 008cbe0f has its CatchHandler @ 007cde44 */
  _ZdlPv(param_1);
  return;
}

~~~
