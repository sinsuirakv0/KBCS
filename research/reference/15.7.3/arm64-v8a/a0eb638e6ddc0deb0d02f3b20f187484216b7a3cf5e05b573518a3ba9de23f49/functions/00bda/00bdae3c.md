# 00bdae3c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bdae3c",
  "name": "FUN_00bdae3c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "944855150ae5497b9dd5a2bc8c67f451d04a8d40d28f3689a49d1b75cb081751",
  "source_text_sha256": "944855150ae5497b9dd5a2bc8c67f451d04a8d40d28f3689a49d1b75cb081751"
}
~~~

## 呼び出し元

- [008d40c0](../008d4/008d40c0.md)

## 呼び出し先

- [008d5008](../008d5/008d5008.md)

## 疑似コード / UTF-8 133 bytes

~~~c

void FUN_00bdae3c(undefined1 param_1 [16])

{
  long in_x9;
  
  FUN_008d5008(param_1,*(undefined8 *)(in_x9 + 0xe10));
  return;
}

~~~
