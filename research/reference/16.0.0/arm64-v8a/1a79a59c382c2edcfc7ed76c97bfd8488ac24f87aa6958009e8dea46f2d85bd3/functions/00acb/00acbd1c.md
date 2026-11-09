# 00acbd1c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acbd1c",
  "name": "FUN_00acbd1c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ff544342daf40415e7b262f0ff557fe113959549b3762971755b338f45d4db4",
  "source_text_sha256": "0ff544342daf40415e7b262f0ff557fe113959549b3762971755b338f45d4db4"
}
~~~

## 呼び出し元

- [00731e84](../00731/00731e84.md)
- [00935514](../00935/00935514.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 177 bytes

~~~c

void FUN_00acbd1c(long param_1,undefined4 param_2,undefined4 param_3)

{
  *(undefined4 *)(param_1 + 0x10) = param_2;
  *(undefined4 *)(param_1 + 0x14) = param_3;
  return;
}

~~~
