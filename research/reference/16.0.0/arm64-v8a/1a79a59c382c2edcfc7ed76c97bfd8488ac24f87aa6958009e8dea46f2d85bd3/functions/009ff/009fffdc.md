# 009fffdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "009fffdc",
  "name": "FUN_009fffdc",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77fbe527e088aa149f3e51a5a106d5762fed6770664bc6f0ce8fef1338d1ecb4",
  "source_text_sha256": "77fbe527e088aa149f3e51a5a106d5762fed6770664bc6f0ce8fef1338d1ecb4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 252 bytes

~~~c

void FUN_009fffdc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  *param_2 = &PTR_FUN_00c8a490;
  uVar1 = *(undefined8 *)(param_1 + 8);
  *(undefined4 *)(param_2 + 2) = *(undefined4 *)(param_1 + 0x10);
  param_2[1] = uVar1;
  return;
}

~~~
