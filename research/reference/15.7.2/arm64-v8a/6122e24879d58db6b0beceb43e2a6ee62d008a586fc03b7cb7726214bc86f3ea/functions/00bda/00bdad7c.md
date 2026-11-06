# 00bdad7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bdad7c",
  "name": "FUN_00bdad7c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e353ee10cb7a17912b1875ebfb49292d45e8ea77707ffc03e733f53a04fb8d8d",
  "source_text_sha256": "e353ee10cb7a17912b1875ebfb49292d45e8ea77707ffc03e733f53a04fb8d8d"
}
~~~

## 呼び出し元

- [008d40c0](../008d4/008d40c0.md)

## 呼び出し先

- [008d5008](../008d5/008d5008.md)

## 疑似コード / UTF-8 133 bytes

~~~c

void FUN_00bdad7c(undefined1 param_1 [16])

{
  long in_x9;
  
  FUN_008d5008(param_1,*(undefined8 *)(in_x9 + 0xe10));
  return;
}

~~~
