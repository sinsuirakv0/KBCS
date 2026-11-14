# 00bf1aac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bf1aac",
  "name": "_ZNSt13runtime_errorC1ERKS_",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a4a1fde258bb9c43ea24e89a2389c646c167c275307773ff25de635039256ce2",
  "source_text_sha256": "a4a1fde258bb9c43ea24e89a2389c646c167c275307773ff25de635039256ce2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c54d30](../00c54/00c54d30.md)

## 疑似コード / UTF-8 245 bytes

~~~c

void _ZNSt13runtime_errorC1ERKS_(long *param_1,long param_2)

{
  long lVar1;
  
  lVar1 = *(long *)(param_2 + 8);
  *param_1 = (long)(PTR__ZTVSt13runtime_error_00c9cb38 + 0x10);
  param_1[1] = lVar1;
  FUN_00c54d30(1,lVar1 + -8);
  return;
}

~~~
