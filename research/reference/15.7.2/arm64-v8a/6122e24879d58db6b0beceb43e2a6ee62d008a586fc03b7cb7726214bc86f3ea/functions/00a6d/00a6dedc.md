# 00a6dedc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a6dedc.md)

## 関数情報

~~~json
{
  "address": "00a6dedc",
  "name": "FUN_00a6dedc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "29950411b3fe3c800eb1ab13cfe12a2ebffe2a13137f6c116e0ea26a877e9889",
  "source_text_sha256": "29950411b3fe3c800eb1ab13cfe12a2ebffe2a13137f6c116e0ea26a877e9889"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 245 bytes

~~~c

long FUN_00a6dedc(long param_1,long param_2)

{
  param_1 = param_1 + 0x18;
  if (*(char **)(param_2 + 8) !=
      "NSt6__ndk110shared_ptrI6UIViewE27__shared_ptr_default_deleteIS1_S1_EE") {
    param_1 = 0;
  }
  return param_1;
}

~~~
