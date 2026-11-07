# 00bbaf7c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bbae70`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbae70.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bbaf7c",
  "name": "_ZNSt12domain_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d1d98d512c30376917141bf6b8a9822a88916f2e591a68a8926dbc279596f323",
  "source_text_sha256": "d1d98d512c30376917141bf6b8a9822a88916f2e591a68a8926dbc279596f323"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1e70](../00be1/00be1e70.md)

## 疑似コード / UTF-8 108 bytes

~~~c

void _ZNSt12domain_errorD0Ev(void *param_1)

{
  _ZNSt11logic_errorD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
