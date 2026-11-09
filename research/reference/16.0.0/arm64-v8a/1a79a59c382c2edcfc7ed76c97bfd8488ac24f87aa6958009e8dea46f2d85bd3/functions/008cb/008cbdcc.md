# 008cbdcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "008cbdcc",
  "name": "FUN_008cbdcc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "287d59069088103b92afd2352f13a43e2466ed80eba93d089db1750c18fa2845",
  "source_text_sha256": "287d59069088103b92afd2352f13a43e2466ed80eba93d089db1750c18fa2845"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_008cbdcc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c83a68;
  param_2[1] = uVar1;
  return;
}

~~~
