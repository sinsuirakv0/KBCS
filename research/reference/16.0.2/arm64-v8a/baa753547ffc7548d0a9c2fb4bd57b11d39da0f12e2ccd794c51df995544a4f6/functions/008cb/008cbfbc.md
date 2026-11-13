# 008cbfbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "008cbfbc",
  "name": "FUN_008cbfbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "85dc996144cbf35e22a89f0735e3c8a8e01f507210b01669fe7982badb46e0fc",
  "source_text_sha256": "85dc996144cbf35e22a89f0735e3c8a8e01f507210b01669fe7982badb46e0fc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 283 bytes

~~~c

void FUN_008cbfbc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 008cbfc0 to 009cbfd3 has its CatchHandler @ 008cce08 */
  *param_2 = &PTR_FUN_00c83f38;
  param_2[1] = uVar1;
  return;
}

~~~
