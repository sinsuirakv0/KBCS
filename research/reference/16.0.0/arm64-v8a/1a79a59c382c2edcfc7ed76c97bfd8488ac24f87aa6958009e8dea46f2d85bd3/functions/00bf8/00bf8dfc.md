# 00bf8dfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bf8dfc",
  "name": "_ZNSt6__ndk118condition_variable10notify_allEv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "db5e4f1ab1876b56fe93c9097bfa85979662c926ee28fd29210087a9cc6bf506",
  "source_text_sha256": "db5e4f1ab1876b56fe93c9097bfa85979662c926ee28fd29210087a9cc6bf506"
}
~~~

## 呼び出し元

- [00c57f80](../00c57/00c57f80.md)

## 呼び出し先

- [00c5ddc0](../00c5d/00c5ddc0.md)

## 疑似コード / UTF-8 158 bytes

~~~c

int _ZNSt6__ndk118condition_variable10notify_allEv(pthread_cond_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_cond_broadcast(param_1);
  return iVar1;
}

~~~
