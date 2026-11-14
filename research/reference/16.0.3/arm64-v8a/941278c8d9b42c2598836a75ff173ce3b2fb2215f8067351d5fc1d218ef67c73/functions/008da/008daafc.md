# 008daafc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "008daafc",
  "name": "FUN_008daafc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9dfaf0c989cdd542d559a047b3a40a9ca767d987821b79c732d83ca189091189",
  "source_text_sha256": "9dfaf0c989cdd542d559a047b3a40a9ca767d987821b79c732d83ca189091189"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008ba17c](../008ba/008ba17c.md)

## 疑似コード / UTF-8 155 bytes

~~~c

void FUN_008daafc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  if (*param_3 == 2) {
    FUN_008ba17c(*param_2);
    return;
  }
  return;
}

~~~
