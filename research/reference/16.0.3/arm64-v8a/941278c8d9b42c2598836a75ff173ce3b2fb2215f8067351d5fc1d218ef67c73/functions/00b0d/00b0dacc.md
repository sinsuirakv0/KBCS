# 00b0dacc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b0dacc",
  "name": "FUN_00b0dacc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0b85f4f780b7b736025ef6e7358df0edfec5197959f0ebda762e0ee49e03f742",
  "source_text_sha256": "0b85f4f780b7b736025ef6e7358df0edfec5197959f0ebda762e0ee49e03f742"
}
~~~

## 呼び出し元

- [00b0a798](../00b0a/00b0a798.md)
- [00b0bf30](../00b0b/00b0bf30.md)

## 呼び出し先

- [0043bad8](../0043b/0043bad8.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_00b0dacc(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_0043bad8("vector");
}

~~~
