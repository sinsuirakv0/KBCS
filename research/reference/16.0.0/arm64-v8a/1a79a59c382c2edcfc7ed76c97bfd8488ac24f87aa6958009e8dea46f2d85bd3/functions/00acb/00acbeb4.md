# 00acbeb4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acbeb4",
  "name": "FUN_00acbeb4",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "307115f6cc2be5cd400746b79133379701acb551b7d8aaf99450ea52584424f7",
  "source_text_sha256": "307115f6cc2be5cd400746b79133379701acb551b7d8aaf99450ea52584424f7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 233 bytes

~~~c

long FUN_00acbeb4(long param_1,long param_2)

{
  param_1 = param_1 + 0x18;
  if (*(char **)(param_2 + 8) !=
      "NSt6__ndk110shared_ptrI6UIViewE27__shared_ptr_default_deleteIS1_S1_EE") {
    param_1 = 0;
  }
  return param_1;
}

~~~
