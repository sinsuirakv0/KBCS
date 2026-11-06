# 00bdae9c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bdae9c",
  "name": "FUN_00bdae9c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d378de2315dae509f9da866b4583f3081a7ffcbf99acd629b8c63db1a06e998d",
  "source_text_sha256": "d378de2315dae509f9da866b4583f3081a7ffcbf99acd629b8c63db1a06e998d"
}
~~~

## 呼び出し元

- [00b07fc8](../00b07/00b07fc8.md)

## 呼び出し先

- [00b08008](../00b08/00b08008.md)

## 疑似コード / UTF-8 155 bytes

~~~c

void FUN_00bdae9c(undefined8 param_1,undefined8 param_2)

{
  long in_x9;
  
  FUN_00b08008(param_1,param_2,*(undefined8 *)(in_x9 + 0xea8));
  return;
}

~~~
