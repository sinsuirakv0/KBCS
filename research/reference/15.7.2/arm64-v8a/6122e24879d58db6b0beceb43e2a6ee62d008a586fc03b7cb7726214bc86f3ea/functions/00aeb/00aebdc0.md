# 00aebdc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00aebecc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebecc.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00aebdc0",
  "name": "_ZN8firebase4util8iterator10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "732e47a7f9336cf2c2dc92822ffe6a8210af9911982072b063032d03056de93f",
  "source_text_sha256": "732e47a7f9336cf2c2dc92822ffe6a8210af9911982072b063032d03056de93f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde080](../00bde/00bde080.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

## 疑似コード / UTF-8 231 bytes

~~~c

undefined8 _ZN8firebase4util8iterator10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_010a0818 + (ulong)param_1 * 8);
}

~~~
