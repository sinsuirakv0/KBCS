# 00acbd7c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00acbd7c.md)

## 関数情報

~~~json
{
  "address": "00acbd7c",
  "name": "FUN_00acbd7c",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ba6332849756314d8b11ffbfafb6d188eb393de4e6e7bcef94c64d704687231",
  "source_text_sha256": "7ba6332849756314d8b11ffbfafb6d188eb393de4e6e7bcef94c64d704687231"
}
~~~
## 呼び出し元

- [004188e8](../00418/004188e8.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 187 bytes

~~~c

void FUN_00acbd7c(undefined8 param_1,int param_2)

{
  long lVar1;
  
  if (param_2 != 0) {
    return;
  }
  lVar1 = FUN_0081f580();
  *(undefined1 *)(lVar1 + 0x347f) = 1;
  return;
}

~~~
