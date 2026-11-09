# 00a7dbfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00a7dbfc",
  "name": "FUN_00a7dbfc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f948d5c802d98bce49deedef76e0f97ddec7d586985e74771eac4c63a3a91033",
  "source_text_sha256": "f948d5c802d98bce49deedef76e0f97ddec7d586985e74771eac4c63a3a91033"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_00a7dbfc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c8b9a0;
  param_2[1] = uVar1;
  return;
}

~~~
