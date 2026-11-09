# 007aecbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007aecbc",
  "name": "FUN_007aecbc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a15d1f6dfa9a8003b73d6fed90f6f1985029a6c564851e69d0f09c4f1fe61051",
  "source_text_sha256": "a15d1f6dfa9a8003b73d6fed90f6f1985029a6c564851e69d0f09c4f1fe61051"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)

## 疑似コード / UTF-8 135 bytes

~~~c

void FUN_007aecbc(void)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  *puVar1 = &PTR_FUN_00c7a298;
  return;
}

~~~
