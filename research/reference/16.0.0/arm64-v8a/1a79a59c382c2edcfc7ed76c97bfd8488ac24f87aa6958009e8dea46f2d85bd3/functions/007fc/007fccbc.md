# 007fccbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007fccbc",
  "name": "FUN_007fccbc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5019a43f7e16b215ed9b471587b5532c7df8d845c6432208a1d594505a96d24",
  "source_text_sha256": "e5019a43f7e16b215ed9b471587b5532c7df8d845c6432208a1d594505a96d24"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)

## 疑似コード / UTF-8 242 bytes

~~~c

void FUN_007fccbc(long param_1)

{
  undefined4 uVar1;
  undefined8 *puVar2;
  
  puVar2 = (undefined8 *)_Znwm(0x10);
  uVar1 = *(undefined4 *)(param_1 + 8);
  *puVar2 = &PTR_FUN_00c7d330;
  *(undefined4 *)(puVar2 + 1) = uVar1;
  return;
}

~~~
