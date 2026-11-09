# 00bf8ddc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bf8ddc",
  "name": "_ZNSt6__ndk118condition_variable10notify_oneEv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "793c4ab79f1a875866e958c6792d46710950e802b81ee6228adc88cf4e7bca95",
  "source_text_sha256": "793c4ab79f1a875866e958c6792d46710950e802b81ee6228adc88cf4e7bca95"
}
~~~

## 呼び出し元

- [00c58d10](../00c58/00c58d10.md)

## 呼び出し先

- [00c5d230](../00c5d/00c5d230.md)

## 疑似コード / UTF-8 155 bytes

~~~c

int _ZNSt6__ndk118condition_variable10notify_oneEv(pthread_cond_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_cond_signal(param_1);
  return iVar1;
}

~~~
