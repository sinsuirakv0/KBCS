# 00aedfb4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00aedfb4",
  "name": "_ZN8firebase4util3uri10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e63af509c1cb48af34c70bba8a4c9f94b83c68af2008be84c080dfd8e7f683e8",
  "source_text_sha256": "e63af509c1cb48af34c70bba8a4c9f94b83c68af2008be84c080dfd8e7f683e8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde180](../00bde/00bde180.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

## 疑似コード / UTF-8 226 bytes

~~~c

undefined8 _ZN8firebase4util3uri10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_010a0a80 + (ulong)param_1 * 8);
}

~~~
