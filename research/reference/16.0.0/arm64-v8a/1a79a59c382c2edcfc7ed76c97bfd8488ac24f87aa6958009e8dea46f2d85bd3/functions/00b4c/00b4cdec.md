# 00b4cdec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b4cdec",
  "name": "_ZN8firebase4util3set11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e76372127d93a0130895675909aa396ab33c30c078d4759bfcd9cefe3c42f97b",
  "source_text_sha256": "e76372127d93a0130895675909aa396ab33c30c078d4759bfcd9cefe3c42f97b"
}
~~~

## 呼び出し元

- [00c5b100](../00c5b/00c5b100.md)

## 呼び出し先

- [00c5ac00](../00c5a/00c5ac00.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 203 bytes

~~~c

undefined8 _ZN8firebase4util3set11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_01125898)[param_1];
}

~~~
