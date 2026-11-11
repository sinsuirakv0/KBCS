# 007fefec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "007fefec",
  "name": "FUN_007fefec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c1f60cc41966e8ce690e8dff879c3e869f8d88faa36e94497380e3ca3eb320b",
  "source_text_sha256": "7c1f60cc41966e8ce690e8dff879c3e869f8d88faa36e94497380e3ca3eb320b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)

## 疑似コード / UTF-8 232 bytes

~~~c

void FUN_007fefec(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)param_1[2];
  *param_1 = &PTR_FUN_00c7e030;
  if (__ptr != (void *)0x0) {
    param_1[3] = __ptr;
    _ZdlPv(__ptr);
  }
  _ZdlPv(param_1);
  return;
}

~~~
