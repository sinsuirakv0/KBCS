# 00bbaeb4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bbada8`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbada8.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bbaeb4",
  "name": "_ZNSt11logic_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be1e18752697c27012042c7b2cb7fa2b10873a604c7f886ff54c13022a3282e0",
  "source_text_sha256": "be1e18752697c27012042c7b2cb7fa2b10873a604c7f886ff54c13022a3282e0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1e60](../00be1/00be1e60.md)

## 疑似コード / UTF-8 107 bytes

~~~c

void _ZNSt11logic_errorD0Ev(void *param_1)

{
  _ZNSt11logic_errorD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
