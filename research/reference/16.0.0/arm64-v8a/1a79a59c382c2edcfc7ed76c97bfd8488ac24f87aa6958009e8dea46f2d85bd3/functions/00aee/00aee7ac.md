# 00aee7ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aee7ac",
  "name": "FUN_00aee7ac",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "12d3d61d673cd858316d09a13e8c88bc65f4901e74ebc8c8cab22a9a6ce83e5c",
  "source_text_sha256": "12d3d61d673cd858316d09a13e8c88bc65f4901e74ebc8c8cab22a9a6ce83e5c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_00aee7ac(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c8da68;
  param_2[1] = uVar1;
  return;
}

~~~
