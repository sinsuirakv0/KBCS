# 006feccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "006feccc",
  "name": "FUN_006feccc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2581447da1fdb12aba165551b4f083ccbacbf28d55ba3727210d1a423d28ecf7",
  "source_text_sha256": "2581447da1fdb12aba165551b4f083ccbacbf28d55ba3727210d1a423d28ecf7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_006feccc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c76c88;
  puVar1[1] = uVar2;
  return;
}

~~~
