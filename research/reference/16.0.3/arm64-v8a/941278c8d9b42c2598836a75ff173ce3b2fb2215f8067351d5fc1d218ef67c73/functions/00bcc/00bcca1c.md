# 00bcca1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcca1c",
  "name": "FUN_00bcca1c",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "13fbd37beaa8f8d15eee91b83baf8229e61904ae00ba273c895d979488d745dc",
  "source_text_sha256": "13fbd37beaa8f8d15eee91b83baf8229e61904ae00ba273c895d979488d745dc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)

## 疑似コード / UTF-8 191 bytes

~~~c

void FUN_00bcca1c(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)*param_1;
  if (__ptr != (void *)0x0) {
    param_1[1] = __ptr;
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
