# 00adbf5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00adbf5c",
  "name": "FUN_00adbf5c",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b18325893aa22436b32d54703741eb4d8b8d3a3be3af589e917f5221c3212903",
  "source_text_sha256": "b18325893aa22436b32d54703741eb4d8b8d3a3be3af589e917f5221c3212903"
}
~~~

## 呼び出し元

- [0080dd1c](../0080d/0080dd1c.md)
- [00814828](../00814/00814828.md)

## 呼び出し先

- [005c3468](../005c3/005c3468.md)

## 疑似コード / UTF-8 131 bytes

~~~c

void FUN_00adbf5c(undefined4 *param_1)

{
  *param_1 = 0;
  FUN_005c3468();
  *param_1 = 0;
  FUN_005c3468(param_1);
  return;
}

~~~
