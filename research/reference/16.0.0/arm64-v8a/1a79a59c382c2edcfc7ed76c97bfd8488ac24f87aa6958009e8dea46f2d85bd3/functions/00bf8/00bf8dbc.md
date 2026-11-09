# 00bf8dbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bf8dbc",
  "name": "_ZNSt6__ndk118condition_variableD2Ev",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "74fd08fc12304c0baaa9593947540b9b92c2164ff9cf357cff8ee28f280a5eb9",
  "source_text_sha256": "74fd08fc12304c0baaa9593947540b9b92c2164ff9cf357cff8ee28f280a5eb9"
}
~~~

## 呼び出し元

- [00c57cd0](../00c57/00c57cd0.md)

## 呼び出し先

- [00c5d220](../00c5d/00c5d220.md)

## 疑似コード / UTF-8 146 bytes

~~~c

int _ZNSt6__ndk118condition_variableD2Ev(pthread_cond_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_cond_destroy(param_1);
  return iVar1;
}

~~~
