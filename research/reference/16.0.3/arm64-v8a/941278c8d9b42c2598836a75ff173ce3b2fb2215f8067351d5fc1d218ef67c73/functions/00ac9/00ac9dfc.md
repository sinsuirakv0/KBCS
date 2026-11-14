# 00ac9dfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00ac9dfc",
  "name": "FUN_00ac9dfc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "114f472a925b6d36bcf6bd3a3417f44e1c3657ff227bcb593272ab0ebfa193b8",
  "source_text_sha256": "114f472a925b6d36bcf6bd3a3417f44e1c3657ff227bcb593272ab0ebfa193b8"
}
~~~

## 呼び出し元

- [00a735f8](../00a73/00a735f8.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 169 bytes

~~~c

void FUN_00ac9dfc(long param_1,int param_2,int param_3)

{
  *(float *)(param_1 + 0x208) = (float)param_2;
  *(float *)(param_1 + 0x20c) = (float)param_3;
  return;
}

~~~
