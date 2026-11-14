# 00aaeff4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aaeff4",
  "name": "FUN_00aaeff4",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5006a51ebfd2805244f4e36d691a9d98056887c0850c67f57b67b95da4cc5d2",
  "source_text_sha256": "e5006a51ebfd2805244f4e36d691a9d98056887c0850c67f57b67b95da4cc5d2"
}
~~~

## 呼び出し元

- [006107ac](../00610/006107ac.md)
- [00624b98](../00624/00624b98.md)

## 呼び出し先

- [00aada58](../00aad/00aada58.md)

## 関連文字列（未確認候補）

~~~text
"BcLogDefeated"
~~~

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_00aaeff4(int param_1)

{
  if (param_1 != 0) {
    return;
  }
  FUN_00aada58("BcLogDefeated");
  return;
}

~~~
