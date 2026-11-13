# 00aa1dcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aa1dcc",
  "name": "FUN_00aa1dcc",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "681c19c16fce87a04e503be4ca3f3f4198600a21a4ddd489867afde8698f812f",
  "source_text_sha256": "681c19c16fce87a04e503be4ca3f3f4198600a21a4ddd489867afde8698f812f"
}
~~~

## 呼び出し元

- [00aa02d8](../00aa0/00aa02d8.md)
- [00aa1dcc](../00aa1/00aa1dcc.md)

## 呼び出し先

- [00aa1dcc](../00aa1/00aa1dcc.md)
- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 359 bytes

~~~c

void FUN_00aa1dcc(undefined8 param_1,undefined8 *param_2)

{
  void *__ptr;
  
  if (param_2 != (undefined8 *)0x0) {
    FUN_00aa1dcc(param_1,*param_2);
    FUN_00aa1dcc(param_1,param_2[1]);
    __ptr = (void *)param_2[5];
    if (__ptr != (void *)0x0) {
      param_2[6] = __ptr;
      _ZdlPv(__ptr);
    }
    _ZdlPv(param_2);
    return;
  }
  return;
}

~~~
